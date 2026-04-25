import pytest
from synthdata_engine.schema import DatasetSchema, EnumValue, SchemaField, extract_strings


def _hr_schema() -> DatasetSchema:
    return DatasetSchema(
        fields=[
            SchemaField(name="text", type="string", description="msg"),
            SchemaField(
                name="label",
                type="enum",
                values=["create_jd", "refine_jd", "delete_jd", "hide_jd"],
            ),
            SchemaField(name="confidence", type="float", min=0.7, max=1.0),
            SchemaField(name="source", type="enum", values=["synthetic"]),
        ]
    )


def test_valid_row():
    s = _hr_schema()
    ok, errs = s.validate_row(
        {"text": "hi", "label": "create_jd", "confidence": 0.9, "source": "synthetic"}
    )
    assert ok, errs


def test_missing_field():
    s = _hr_schema()
    ok, errs = s.validate_row({"text": "hi", "label": "create_jd", "source": "synthetic"})
    assert not ok
    assert any("confidence" in e for e in errs)


def test_bad_enum():
    s = _hr_schema()
    ok, errs = s.validate_row(
        {"text": "hi", "label": "apply_for_job", "confidence": 0.9, "source": "synthetic"}
    )
    assert not ok
    assert any("label" in e for e in errs)


def test_out_of_range_float():
    s = _hr_schema()
    ok, errs = s.validate_row(
        {"text": "hi", "label": "create_jd", "confidence": 0.5, "source": "synthetic"}
    )
    assert not ok
    assert any("confidence" in e for e in errs)


def test_extra_fields_flagged():
    s = _hr_schema()
    ok, errs = s.validate_row(
        {"text": "hi", "label": "create_jd", "confidence": 0.9, "source": "synthetic", "junk": 1}
    )
    assert not ok
    assert any("junk" in e for e in errs)


def test_duplicate_field_names_rejected():
    try:
        DatasetSchema(
            fields=[
                SchemaField(name="text", type="string"),
                SchemaField(name="text", type="string"),
            ]
        )
    except ValueError:
        return
    raise AssertionError("expected ValueError on duplicate field names")


def test_enum_requires_values():
    try:
        SchemaField(name="label", type="enum")
    except ValueError:
        return
    raise AssertionError("expected ValueError on enum without values")


# --- array type ---

def _ner_schema() -> DatasetSchema:
    return DatasetSchema(fields=[
        SchemaField(name="text", type="string"),
        SchemaField(
            name="spans",
            type="array",
            description="Named entity spans",
            items=SchemaField(
                type="object",
                fields=[
                    SchemaField(name="start", type="integer", min=0),
                    SchemaField(name="end", type="integer", min=0),
                    SchemaField(name="label", type="enum", values=["PER", "ORG", "LOC"]),
                ],
            ),
        ),
    ])


def test_array_valid_row():
    s = _ner_schema()
    ok, errs = s.validate_row({
        "text": "Apple hired Tim Cook.",
        "spans": [{"start": 0, "end": 5, "label": "ORG"}, {"start": 13, "end": 21, "label": "PER"}],
    })
    assert ok, errs


def test_array_wrong_type():
    s = _ner_schema()
    ok, errs = s.validate_row({"text": "hi", "spans": "not a list"})
    assert not ok
    assert any("array" in e for e in errs)


def test_array_item_validation_error():
    s = _ner_schema()
    ok, errs = s.validate_row({
        "text": "hi",
        "spans": [{"start": 0, "end": 5, "label": "UNKNOWN_LABEL"}],
    })
    assert not ok
    assert any("label" in e for e in errs)


def test_array_requires_items():
    with pytest.raises(ValueError, match="items"):
        SchemaField(name="tags", type="array")


# --- object type ---

def _meta_schema() -> DatasetSchema:
    return DatasetSchema(fields=[
        SchemaField(name="text", type="string"),
        SchemaField(
            name="metadata",
            type="object",
            fields=[
                SchemaField(name="source", type="enum", values=["twitter", "reddit", "news"]),
                SchemaField(name="confidence", type="float", min=0.0, max=1.0),
            ],
        ),
    ])


def test_object_valid_row():
    s = _meta_schema()
    ok, errs = s.validate_row({
        "text": "Great product!",
        "metadata": {"source": "twitter", "confidence": 0.95},
    })
    assert ok, errs


def test_object_wrong_type():
    s = _meta_schema()
    ok, errs = s.validate_row({"text": "hi", "metadata": "not an object"})
    assert not ok
    assert any("object" in e for e in errs)


def test_object_nested_field_error():
    s = _meta_schema()
    ok, errs = s.validate_row({
        "text": "hi",
        "metadata": {"source": "facebook", "confidence": 0.9},  # facebook not in enum
    })
    assert not ok
    assert any("source" in e for e in errs)


def test_object_requires_fields():
    with pytest.raises(ValueError, match="fields"):
        SchemaField(name="meta", type="object")


def test_object_missing_nested_required_field():
    s = _meta_schema()
    ok, errs = s.validate_row({"text": "hi", "metadata": {"confidence": 0.9}})
    assert not ok
    assert any("source" in e for e in errs)


# --- json_example shape ---

def test_json_example_nested():
    s = _ner_schema()
    ex = s.json_example()
    assert isinstance(ex["spans"], list)
    assert isinstance(ex["spans"][0], dict)
    assert "start" in ex["spans"][0]
    assert "label" in ex["spans"][0]


def test_json_example_object():
    s = _meta_schema()
    ex = s.json_example()
    assert isinstance(ex["metadata"], dict)
    assert "source" in ex["metadata"]
    assert "confidence" in ex["metadata"]


# --- extract_strings ---

def test_extract_strings_flat():
    fields = [SchemaField(name="text", type="string"), SchemaField(name="label", type="enum", values=["a"])]
    row = {"text": "hello world", "label": "a"}
    assert extract_strings(row, fields) == ["hello world"]


def test_extract_strings_nested_object():
    s = _meta_schema()
    row = {"text": "hello", "metadata": {"source": "twitter", "confidence": 0.9}}
    result = extract_strings(row, s.fields)
    assert "hello" in result


def test_extract_strings_nested_array():
    s = _ner_schema()
    row = {"text": "Apple hired Tim.", "spans": [{"start": 0, "end": 5, "label": "ORG"}]}
    result = extract_strings(row, s.fields)
    assert "Apple hired Tim." in result


# --- string_field_paths ---

def test_string_field_paths_flat():
    s = _hr_schema()
    assert s.string_field_paths() == ["text"]


def test_string_field_paths_nested():
    s = _ner_schema()
    paths = s.string_field_paths()
    assert "text" in paths


def test_string_field_paths_object():
    s = DatasetSchema(fields=[
        SchemaField(name="data", type="object", fields=[
            SchemaField(name="body", type="string"),
            SchemaField(name="title", type="string"),
        ]),
    ])
    paths = s.string_field_paths()
    assert "data.body" in paths
    assert "data.title" in paths
