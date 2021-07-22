from snakemd import InlineText


def test_inline_text_empty():
    text = InlineText("")
    assert str(text) == ""


def test_inline_text_str():
    text = InlineText("Hello, World!")
    assert str(text) == "Hello, World!"


def test_inline_text_bold():
    text = InlineText("Hello, World!", bold=True)
    assert str(text) == "**Hello, World!**"


def test_inline_text_bold_method():
    text = InlineText("Hello, World!")
    text.bold()
    assert str(text) == "**Hello, World!**"


def test_inline_text_unbold_method():
    text = InlineText("Hello, World!", bold=True)
    text.unbold()
    assert str(text) == "Hello, World!"


def test_inline_text_italics():
    text = InlineText("Hello, World!", italics=True)
    assert str(text) == "*Hello, World!*"


def test_inline_text_bold_italics():
    text = InlineText("Hello, World!", italics=True, bold=True)
    assert str(text) == "***Hello, World!***"


def test_inline_text_code():
    text = InlineText("x = 7", code=True)
    assert str(text) == "`x = 7`"


def test_inline_text_url():
    text = InlineText("Here", url="https://google.com")
    assert str(text) == "[Here](https://google.com)"


def test_inline_text_image():
    text = InlineText("Here", url="https://google.com", image=True)
    assert str(text) == "![Here](https://google.com)"


def test_inline_text_image_minus_url():
    text = InlineText("Here", image=True)
    assert str(text) == "Here"


def test_inline_text_verify_empty():
    text = InlineText("")
    assert text.verify().passes_inspection()


def test_inline_text_verify_invalid_url():
    text = InlineText("Bad URL Test", url="adlsfhaisu")
    assert not text.verify().passes_inspection()


def test_inline_text_verify_no_image_url():
    text = InlineText("Bad URL Test", image=True)
    assert not text.verify().passes_inspection()
