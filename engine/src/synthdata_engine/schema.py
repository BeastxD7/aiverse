"""User-defined dataset schema.

The user declares the shape of their dataset (field names, types, enums, ranges)
in a YAML config. Enum values can be plain strings or {name, description} objects
so the user can attach usage guidance per value — this flows into generation and
judge prompts to reduce label drift.

Supported types: string, integer, float, boolean, enum, array, object.
Arrays and objects can be nested to arbitrary depth.
"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator, model_validator

FieldType = Literal["string", "integer", "float", "boolean", "enum", "array", "object"]


class EnumValue(BaseModel):
    """One allowed value for an enum field, with optional usage description."""

    name: str
    description: str = ""


class SchemaField(BaseModel):
    name: str = ""
    type: FieldType
    description: str = ""
    values: list[EnumValue] | None = None    # enum
    min: float | None = None                  # integer / float bounds
    max: float | None = None
    required: bool = True
    items: SchemaField | None = None          # array element type
    fields: list[SchemaField] | None = None   # object sub-fields

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
    def _validate_type_constraints(self):
        if self.type == "enum" and not self.values:
            raise ValueError("enum field must declare 'values'")
        if self.type == "array" and self.items is None:
            raise ValueError("array field must declare 'items'")
        if self.type == "object" and not self.fields:
            raise ValueError("object field must declare 'fields'")
        return self

    def value_names(self) -> list[str]:
        """Just the allowed value strings, preserving order."""
        return [v.name for v in (self.values or [])]


# Required for self-referential Pydantic models.
SchemaField.model_rebuild()


def _field_example(f: SchemaField) -> Any:
    """Shape hint for a single field — embedded in generation prompts."""
    if f.type == "enum":
        return f"one of {f.value_names()}"
    elif f.type == "string":
        return f"string ({f.description})" if f.description else "string"
    elif f.type == "integer":
        bounds = ""
        if f.min is not None and f.max is not None:
            bounds = f" between {int(f.min)} and {int(f.max)}"
        elif f.min is not None:
            bounds = f" >= {int(f.min)}"
        elif f.max is not None:
            bounds = f" <= {int(f.max)}"
        return f"integer{bounds}"
    elif f.type == "float":
        bounds = f" between {f.min} and {f.max}" if (f.min is not None or f.max is not None) else ""
        return f"float{bounds}"
    elif f.type == "boolean":
        return "boolean"
    elif f.type == "object":
        return {sub.name: _field_example(sub) for sub in (f.fields or [])}
    elif f.type == "array":
        return [_field_example(f.items)] if f.items else []
    return "unknown"


class DatasetSchema(BaseModel):
    fields: list[SchemaField] = Field(min_length=1, max_length=20)

    @field_validator("fields")
    @classmethod
    def _at_least_one_string(cls, fields):
        def _has_text(flist: list[SchemaField]) -> bool:
            for f in flist:
                if f.type in ("string", "enum"):
                    return True
                if f.type == "object" and f.fields and _has_text(f.fields):
                    return True
                if f.type == "array" and f.items and _has_text([f.items]):
                    return True
            return False

        if not _has_text(fields):
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
            err = _check_type(f, row[f.name])
            if err:
                errors.append(err)

        extra = set(row.keys()) - {f.name for f in self.fields}
        if extra:
            errors.append(f"unexpected fields: {sorted(extra)}")

        return (not errors), errors

    def json_example(self) -> dict[str, Any]:
        """Shape hint embedded in prompts — shows full nested structure."""
        return {f.name: _field_example(f) for f in self.fields}

    def string_field_paths(self) -> list[str]:
        """Dot-separated paths to every string-typed leaf field (for dedup/quality)."""
        return list(_string_paths(self.fields))


def _string_paths(fields: list[SchemaField], prefix: str = "") -> list[str]:
    paths: list[str] = []
    for f in fields:
        path = f"{prefix}.{f.name}" if prefix else f.name
        if f.type == "string":
            paths.append(path)
        elif f.type == "object" and f.fields:
            paths.extend(_string_paths(f.fields, path))
        elif f.type == "array" and f.items:
            if f.items.type == "string":
                paths.append(f"{path}[]")
            elif f.items.type == "object" and f.items.fields:
                paths.extend(_string_paths(f.items.fields, f"{path}[]"))
    return paths


def extract_strings(row: dict, fields: list[SchemaField]) -> list[str]:
    """Recursively collect all string-typed leaf values from a row."""
    result: list[str] = []
    for f in fields:
        val = row.get(f.name)
        if val is None:
            continue
        if f.type == "string" and isinstance(val, str):
            result.append(val)
        elif f.type == "object" and isinstance(val, dict) and f.fields:
            result.extend(extract_strings(val, f.fields))
        elif f.type == "array" and isinstance(val, list) and f.items:
            if f.items.type == "string":
                result.extend(v for v in val if isinstance(v, str))
            elif f.items.type == "object" and f.items.fields:
                for item in val:
                    if isinstance(item, dict):
                        result.extend(extract_strings(item, f.items.fields))
    return result


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
    elif f.type == "object":
        if not isinstance(val, dict):
            return f"field '{f.name}' must be object, got {type(val).__name__}"
        for sub in (f.fields or []):
            if sub.name not in val:
                if sub.required:
                    return f"field '{f.name}.{sub.name}' is missing"
                continue
            sub_err = _check_type(sub, val[sub.name])
            if sub_err:
                return sub_err
    elif f.type == "array":
        if not isinstance(val, list):
            return f"field '{f.name}' must be array, got {type(val).__name__}"
        if f.items:
            for i, item in enumerate(val):
                item_field = f.items.model_copy(update={"name": f"{f.name}[{i}]"})
                item_err = _check_type(item_field, item)
                if item_err:
                    return item_err
    return None
