import pytest

from snakemd import Inline


# Constructor tests


def test_inline_empty():
    text = Inline("")
    assert str(text) == ""


def test_inline_str():
    text = Inline("Hello, World!")
    assert str(text) == "Hello, World!"


def test_inline_code():
    text = Inline("x = 7", code=True)
    assert str(text) == "`x = 7`"


def test_inline_bold():
    text = Inline("Hello, World!", bold=True)
    assert str(text) == "**Hello, World!**"


def test_inline_italics():
    text = Inline("Hello, World!", italics=True)
    assert str(text) == "*Hello, World!*"


def test_inline_strikethrough():
    text = Inline("Hello, World!", strikethrough=True)
    assert str(text) == "~~Hello, World!~~"


def test_inline_url():
    text = Inline("Here", url="https://google.com")
    assert str(text) == "[Here](https://google.com)"


def test_inline_image():
    text = Inline("Here", image="https://snakemd.io")
    assert str(text) == "![Here](https://snakemd.io)"


def test_inline_bold_italics():
    text = Inline("Hello, World!", italics=True, bold=True)
    assert str(text) == "***Hello, World!***"


def test_inline_image_linked():
    text = Inline("Here", url="https://google.com", image="https://snakemd.io")
    assert str(text) == "[![Here](https://snakemd.io)](https://google.com)"


# Method tests


def test_inline_bold_method():
    text = Inline("Hello, World!").bold()
    assert str(text) == "**Hello, World!**"


def test_inline_unbold_method():
    text = Inline("Hello, World!", bold=True).unbold()
    assert str(text) == "Hello, World!"


def test_inline_italics_method():
    text = Inline("Hello, World!").italicize()
    assert str(text) == "*Hello, World!*"


def test_inline_unitalics_method():
    text = Inline("Hello, World!", italics=True).unitalicize()
    assert str(text) == "Hello, World!"


def test_inline_strikethrough_method():
    text = Inline("Hello, World!").strikethrough()
    assert str(text) == "~~Hello, World!~~"


def test_inline_unstrikethrough_method():
    text = Inline("Hello, World!", strikethrough=True).unstrikethrough()
    assert str(text) == "Hello, World!"


def test_inline_bold_italics_methods():
    text = Inline("Hello, World!").bold().italicize()
    assert str(text) == "***Hello, World!***"
