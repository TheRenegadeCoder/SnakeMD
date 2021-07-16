from snake.md import InlineText


def test_inline_text_empty():
    text = InlineText("")
    assert text.text == ""
    assert str(text) == ""

def test_inline_text_str():
    text = InlineText("Hello, World!")
    assert text.text == "Hello, World!"
    assert str(text) == "Hello, World!"

def test_inline_text_bold():
    text = InlineText("Hello, World!", bold=True)
    assert text.text == "Hello, World!"
    assert str(text) == "**Hello, World!**"

def test_inline_text_italics():
    text = InlineText("Hello, World!", italics=True)
    assert text.text == "Hello, World!"
    assert str(text) == "*Hello, World!*"

def test_inline_text_bold_italics():
    text = InlineText("Hello, World!", italics=True, bold=True)
    assert text.text == "Hello, World!"
    assert str(text) == "***Hello, World!***"
