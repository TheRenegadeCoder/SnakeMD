import markdown
from snakemd import HorizontalRule


# Constructor tests


def test_horizontal_rule():
    hr = HorizontalRule()
    assert str(hr) == "***"
    assert repr(hr) == "HorizontalRule()"
    assert markdown.markdown(str(hr)) == "<hr />"


# Method tests


def test_repr_can_create_object():
    horizontal_rule = HorizontalRule()
    obj = eval(repr(horizontal_rule))
    assert isinstance(obj, HorizontalRule)
