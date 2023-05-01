from snakemd import Raw


def test_raw_empty():
    raw = Raw("")
    assert str(raw) == ""

def test_raw_one_line():
    raw = Raw("Hello, World!")
    assert str(raw) == "Hello, World!"

def test_raw_two_lines():
    raw = Raw("Hello,\nWorld!")
    assert str(raw) == "Hello,\nWorld!"

def test_raw_user_example():
    raw = Raw("Title: My super title\nDate: 2010-12-03 10:20")
    assert str(raw) == "Title: My super title\nDate: 2010-12-03 10:20"
