from synthdata_engine.stages.dedup import dedupe


def test_dedup_catches_case_variants():
    rows = [
        {"text": "Create a JD"},
        {"text": "create a jd"},
        {"text": "Create a JD."},
        {"text": "Create  a  JD"},
        {"text": "Please delete this posting"},
    ]
    unique, removed = dedupe(rows, text_fields=["text"])
    assert removed >= 2, f"expected case variants to collapse, got removed={removed}"
    assert any("delete" in r["text"] for r in unique)


def test_dedup_keeps_paraphrases():
    rows = [
        {"text": "I want to create a JD"},
        {"text": "I need to make a new job post"},
    ]
    unique, removed = dedupe(rows, text_fields=["text"])
    assert removed == 0
    assert len(unique) == 2


def test_dedup_empty_input():
    unique, removed = dedupe([], text_fields=["text"])
    assert unique == []
    assert removed == 0


def test_dedup_ignores_empty_text():
    rows = [{"text": ""}, {"text": "   "}, {"text": "real content here"}]
    unique, removed = dedupe(rows, text_fields=["text"])
    assert len(unique) == 3
    assert removed == 0
