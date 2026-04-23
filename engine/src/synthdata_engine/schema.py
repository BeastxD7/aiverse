"""User-defined dataset schema.

The user declares the shape of their dataset (field names, types, enums, ranges)
in a YAML config. Enum values can be plain strings or {name, description} objects
so the user can attach usage guidance per value — this flows into generation and
judge prompts to reduce label drift.
"""

from __future__ import annotations

from typing import Any, Literal, Union

from pydantic import BaseModel, Field, field_validator, model_validator

FieldType = Literal["string", "integer", "float", "boolean", "enum"]


class EnumValue(BaseModel):
    """One allowed value for an enum field, with optional usage description."""

    name: str
    description: str = ""


class SchemaField(BaseModel):
    name: str
    type: FieldType
    description: str = ""
    values: list[EnumValue] | None = None
    min: float | None = None
    max: float | None = None
    required: bool = True

    @field_validator("values", mode="before")
    @classmethod
    def _normalize_values(cls, v):
        """Accept list[str] or list[{name, description}] — normalize to EnumValue."""
        if v is None:
            return v
        out: list[dict | EnumValue] = []
        for item in v:
            if isinstance(item, str):
                out.append({"name": item, "description": ""})
            else:
                out.append(item)
        return out

    @model_validator(mode="after")
    def _enum_needs_values(self):
        if self.type == "enum" and not self.values:
            raise ValueError("enum field must declare 'values'")
        return self

    def value_names(self) -> list[str]:
        """Just the allowed value strings, preserving order."""
        return [v.name for v in (self.values or [])]


class DatasetSchema(BaseModel):
    fields: list[SchemaField] = Field(min_length=1, max_length=10)

    @field_validator("fields")
    @classmethod
    def _at_least_one_string(cls, fields):
        if not any(f.type in ("string", "enum") for f in fields):
            raise ValueError("schema must have at least one string or enum field")
        names = [f.name for f in fields]
        if len(set(names)) != len(names):
            raise ValueError("duplicate field names")
        return fields

    def field(self, name: str) -> SchemaField | None:
        return next((f for f in self.fields if f.name == name), None)

    def validate_row(self, row: Any) -> tuple[bool, list[str]]:
        """Return (is_valid, list_of_errors)."""
        errors: list[str] = []
        if not isinstance(row, dict):
            return False, ["row is not a dict"]

        for f in self.fields:
            if f.name not in row:
                if f.required:
                    errors.append(f"missing required field '{f.name}'")
                continue

            val = row[f.name]
            err = _check_type(f, val)
            if err:
                errors.append(err)

        extra = set(row.keys()) - {f.name for f in self.fields}
        if extra:
            errors.append(f"unexpected fields: {sorted(extra)}")

        return (not errors), errors

    def json_example(self) -> dict[str, str]:
        """Shape hint embedded in prompts — type descriptors, not real values."""
        out: dict[str, str] = {}
        for f in self.fields:
            if f.type == "enum":
                out[f.name] = f"one of {f.value_names()}"
            elif f.type == "string":
                hint = "string"
                if f.description:
                    hint = f"string ({f.description})"
                out[f.name] = hint
            elif f.type == "integer":
                out[f.name] = "integer"
            elif f.type == "float":
                rng = ""
                if f.min is not None or f.max is not None:
                    rng = f" between {f.min} and {f.max}"
                out[f.name] = f"float{rng}"
            elif f.type == "boolean":
                out[f.name] = "boolean"
        return out


def _check_type(f: SchemaField, val: Any) -> str | None:
    if val is None:
        return f"field '{f.name}' is null"

    if f.type == "string":
        if not isinstance(val, str):
            return f"field '{f.name}' must be string, got {type(val).__name__}"
    elif f.type == "enum":
        if not isinstance(val, str):
            return f"field '{f.name}' must be string (enum), got {type(val).__name__}"
        if val not in f.value_names():
            return f"field '{f.name}' value '{val}' not in allowed {f.value_names()}"
    elif f.type == "integer":
        if isinstance(val, bool) or not isinstance(val, int):
            return f"field '{f.name}' must be integer"
        if f.min is not None and val < f.min:
            return f"field '{f.name}'={val} below min {f.min}"
        if f.max is not None and val > f.max:
            return f"field '{f.name}'={val} above max {f.max}"
    elif f.type == "float":
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            return f"field '{f.name}' must be number"
        if f.min is not None and val < f.min:
            return f"field '{f.name}'={val} below min {f.min}"
        if f.max is not None and val > f.max:
            return f"field '{f.name}'={val} above max {f.max}"
    elif f.type == "boolean":
        if not isinstance(val, bool):
            return f"field '{f.name}' must be boolean"
    return None
