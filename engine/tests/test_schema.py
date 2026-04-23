from synthdata_engine.schema import DatasetSchema, SchemaField


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
