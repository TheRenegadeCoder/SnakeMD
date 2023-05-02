from snakemd import HorizontalRule


def test_horizontal_rule():
    hr = HorizontalRule()
    assert str(hr) == "***"
    assert repr(hr) == "HorizontalRule()"
    

def test_repr_can_create_object():
    horizontal_rule = HorizontalRule()
    obj = eval(repr(horizontal_rule))
    assert isinstance(obj, HorizontalRule) 
