from synthdata_engine.providers.ollama import _looks_like_refusal, _repair_json


def test_direct_json_parse():
    assert _repair_json('{"a": 1}') == {"a": 1}


def test_json_fenced_block():
    text = "Sure, here you go:\n```json\n{\"a\": 1}\n```"
    assert _repair_json(text) == {"a": 1}


def test_outer_object_extraction():
    text = 'Some prose. {"label": "x", "text": "y"} tail.'
    assert _repair_json(text) == {"label": "x", "text": "y"}


def test_array_extraction():
    text = "result: [1,2,3]"
    assert _repair_json(text) == [1, 2, 3]


def test_none_on_garbage():
    assert _repair_json("complete garbage no braces") is None


def test_empty_string():
    assert _repair_json("") is None


def test_refusal_detected_short_apology():
    assert _looks_like_refusal("I cannot help with this request.")


def test_refusal_detected_empty():
    assert _looks_like_refusal("")


def test_not_refusal_when_has_json():
    assert not _looks_like_refusal('{"text": "something legitimate"}')


def test_not_refusal_when_long():
    long_text = "This is a long response " * 50 + '{"a": 1}'
    assert not _looks_like_refusal(long_text)
