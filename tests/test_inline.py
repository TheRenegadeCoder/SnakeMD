import pytest
import markdown

from snakemd import Inline


# Constructor tests (singles)


def test_inline_empty():
    text = Inline("")
    assert str(text) == ""
    assert markdown.markdown(str(text)) == ""


def test_inline_text():
    text = Inline("Hello, World!")
    assert str(text) == "Hello, World!"
    assert markdown.markdown(str(text)) == "<p>Hello, World!</p>"


def test_inline_image():
    text = Inline("Here", image="https://snakemd.io")
    assert str(text) == "![Here](https://snakemd.io)"
    assert markdown.markdown(str(text)) == '<p><img alt="Here" src="https://snakemd.io" /></p>'


def test_inline_link():
    text = Inline("Here", link="https://snakemd.io")
    assert str(text) == "[Here](https://snakemd.io)"
    assert markdown.markdown(str(text)) == '<p><a href="https://snakemd.io">Here</a></p>'


def test_inline_bold():
    text = Inline("Hello, World!", bold=True)
    assert str(text) == "**Hello, World!**"
    assert markdown.markdown(str(text)) == '<p><strong>Hello, World!</strong></p>'


def test_inline_italics():
    text = Inline("Hello, World!", italics=True)
    assert str(text) == "*Hello, World!*"
    assert markdown.markdown(str(text)) == '<p><em>Hello, World!</em></p>'


def test_inline_strikethrough():
    text = Inline("Hello, World!", strikethrough=True)
    assert str(text) == "~~Hello, World!~~"
    # Strikethrough not supported in python-markdown


def test_inline_code():
    text = Inline("x = 7", code=True)
    assert str(text) == "`x = 7`"
    assert markdown.markdown(str(text)) == '<p><code>x = 7</code></p>'


# Constructor tests (2-combos)


def test_inline_image_linked():
    text = Inline("Here", image="https://snakemd.io", link="https://google.com")
    assert str(text) == "[![Here](https://snakemd.io)](https://google.com)"
    assert markdown.markdown(str(text)) == '<p><a href="https://google.com"><img alt="Here" src="https://snakemd.io" /></a></p>'


def test_inline_image_bolded():
    text = Inline("Here", image="https://snakemd.io", bold=True)
    assert str(text) == "**![Here](https://snakemd.io)**"
    assert markdown.markdown(str(text)) == '<p><strong><img alt="Here" src="https://snakemd.io" /></strong></p>'


def test_inline_image_italicized():
    text = Inline("Here", image="https://snakemd.io", italics=True)
    assert str(text) == "*![Here](https://snakemd.io)*"
    assert markdown.markdown(str(text)) == '<p><em><img alt="Here" src="https://snakemd.io" /></em></p>'


def test_inline_image_strikethroughed():
    text = Inline("Here", image="https://snakemd.io", strikethrough=True)
    assert str(text) == "~~![Here](https://snakemd.io)~~"
    # Strikethrough not supported in python markdown


def test_inline_image_coded():
    text = Inline("Here", image="https://snakemd.io", code=True)
    assert str(text) == "`![Here](https://snakemd.io)`"
    assert markdown.markdown(str(text)) == '<p><code>![Here](https://snakemd.io)</code></p>'


def test_inline_link_bolded():
    text = Inline("Here", link="https://snakemd.io", bold=True)
    assert str(text) == "**[Here](https://snakemd.io)**"


def test_inline_link_italicized():
    text = Inline("Here", link="https://snakemd.io", italics=True)
    assert str(text) == "*[Here](https://snakemd.io)*"


def test_inline_link_strikethroughed():
    text = Inline("Here", link="https://snakemd.io", strikethrough=True)
    assert str(text) == "~~[Here](https://snakemd.io)~~"


def test_inline_link_coded():
    text = Inline("Here", link="https://snakemd.io", code=True)
    assert str(text) == "`[Here](https://snakemd.io)`"


def test_inline_bold_italicized():
    text = Inline("Hello, World!", bold=True, italics=True)
    assert str(text) == "***Hello, World!***"


def test_inline_bold_strikethroughed():
    text = Inline("Hello, World!", bold=True, strikethrough=True)
    assert str(text) == "~~**Hello, World!**~~"


def test_inline_bold_coded():
    text = Inline("Hello, World!", bold=True, code=True)
    assert str(text) == "`**Hello, World!**`"


def test_inline_italics_strikethroughed():
    text = Inline("Hello, World!", italics=True, strikethrough=True)
    assert str(text) == "~~*Hello, World!*~~"


def test_inline_italics_coded():
    text = Inline("Hello, World!", italics=True, code=True)
    assert str(text) == "`*Hello, World!*`"


def test_inline_strikethrough_coded():
    text = Inline("Hello, World!", strikethrough=True, code=True)
    assert str(text) == "`~~Hello, World!~~`"


# Constructor tests (2-combos)


def test_inline_image_linked_bolded():
    text = Inline("Here", image="https://snakemd.io", link="https://google.com", bold=True)
    assert str(text) == "**[![Here](https://snakemd.io)](https://google.com)**"


def test_inline_image_linked_italicized():
    text = Inline("Here", image="https://snakemd.io", link="https://google.com", italics=True)
    assert str(text) == "*[![Here](https://snakemd.io)](https://google.com)*"


def test_inline_image_linked_strikethroughed():
    text = Inline("Here", image="https://snakemd.io", link="https://google.com", strikethrough=True)
    assert str(text) == "~~[![Here](https://snakemd.io)](https://google.com)~~"


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


def test_inline_link_method():
    text = Inline("Here").link("https://snakemd.io")
    assert str(text) == "[Here](https://snakemd.io)"


def test_inline_bold_italics_methods():
    text = Inline("Hello, World!").bold().italicize()
    assert str(text) == "***Hello, World!***"
