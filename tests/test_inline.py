import pytest
import markdown

from snakemd import Inline


# Constructor tests (singles)


def test_inline_empty():
    """
    Verifies that an empty string Inline object
    properly initializes. Also verifies that
    the repr string is properly formatted
    and that the markdown itself is properly
    rendered.
    """
    text = Inline("")
    assert str(text) == ""
    assert repr(text) == (
        "Inline("
        "text='', "
        "image=None, "
        "link=None, "
        "bold=False, "
        "italics=False, "
        "strikethrough=False, "
        "code=False"
        ")"
    )
    assert markdown.markdown(str(text)) == ""


def test_inline_text():
    """
    Verifies that a small string Inline object
    properly initializes. Also verifies that
    the repr string is properly formatted
    and that the markdown itself is properly
    rendered.
    """
    text = Inline("Hello, World!")
    assert str(text) == "Hello, World!"
    assert repr(text) == (
        "Inline("
        "text='Hello, World!', "
        "image=None, "
        "link=None, "
        "bold=False, "
        "italics=False, "
        "strikethrough=False, "
        "code=False"
        ")"
    )    
    assert markdown.markdown(str(text)) == "<p>Hello, World!</p>"


def test_inline_image():
    """
    Verifies that the Inline image parameter
    properly initializes. Also verifies that
    the repr string is properly formatted
    and that the markdown itself is properly
    rendered.
    """
    text = Inline("Here", image="https://snakemd.io")
    assert str(text) == "![Here](https://snakemd.io)"
    assert repr(text) == (
        "Inline("
        "text='Here', "
        "image='https://snakemd.io', "
        "link=None, "
        "bold=False, "
        "italics=False, "
        "strikethrough=False, "
        "code=False"
        ")"
    )
    assert (
        markdown.markdown(str(text))
        == '<p><img alt="Here" src="https://snakemd.io" /></p>'
    )


def test_inline_link():
    """
    Verifies that the Inline link parameter
    properly initializes. Also verifies that
    the repr string is properly formatted
    and that the markdown itself is properly
    rendered.
    """
    text = Inline("Here", link="https://snakemd.io")
    assert str(text) == "[Here](https://snakemd.io)"
    assert repr(text) == (
        "Inline("
        "text='Here', "
        "image=None, "
        "link='https://snakemd.io', "
        "bold=False, "
        "italics=False, "
        "strikethrough=False, "
        "code=False"
        ")"
    )
    assert (
        markdown.markdown(str(text)) == '<p><a href="https://snakemd.io">Here</a></p>'
    )


def test_inline_bold():
    text = Inline("Hello, World!", bold=True)
    assert str(text) == "**Hello, World!**"
    assert repr(text) == (
        "Inline("
        "text='Hello, World!', "
        "image=None, "
        "link=None, "
        "bold=True, "
        "italics=False, "
        "strikethrough=False, "
        "code=False"
        ")"
    )
    assert markdown.markdown(str(text)) == "<p><strong>Hello, World!</strong></p>"


def test_inline_italics():
    text = Inline("Hello, World!", italics=True)
    assert str(text) == "_Hello, World!_"
    assert repr(text) == (
        "Inline("
        "text='Hello, World!', "
        "image=None, "
        "link=None, "
        "bold=False, "
        "italics=True, "
        "strikethrough=False, "
        "code=False"
        ")"
    )
    assert markdown.markdown(str(text)) == "<p><em>Hello, World!</em></p>"


def test_inline_strikethrough():
    text = Inline("Hello, World!", strikethrough=True)
    assert str(text) == "~~Hello, World!~~"
    assert repr(text) == (
        "Inline("
        "text='Hello, World!', "
        "image=None, "
        "link=None, "
        "bold=False, "
        "italics=False, "
        "strikethrough=True, "
        "code=False"
        ")"
    )
    # Strikethrough not supported in python-markdown


def test_inline_code():
    text = Inline("x = 7", code=True)
    assert str(text) == "`x = 7`"
    assert repr(text) == (
        "Inline("
        "text='x = 7', "
        "image=None, "
        "link=None, "
        "bold=False, "
        "italics=False, "
        "strikethrough=False, "
        "code=True"
        ")"
    )
    assert markdown.markdown(str(text)) == "<p><code>x = 7</code></p>"


# Constructor tests (2-combos)


def test_inline_image_linked():
    text = Inline("Here", image="https://snakemd.io", link="https://google.com")
    assert str(text) == "[![Here](https://snakemd.io)](https://google.com)"
    assert (
        markdown.markdown(str(text))
        == '<p><a href="https://google.com"><img alt="Here" src="https://snakemd.io" /></a></p>'
    )


def test_inline_image_bolded():
    text = Inline("Here", image="https://snakemd.io", bold=True)
    assert str(text) == "**![Here](https://snakemd.io)**"
    assert (
        markdown.markdown(str(text))
        == '<p><strong><img alt="Here" src="https://snakemd.io" /></strong></p>'
    )


def test_inline_image_italicized():
    text = Inline("Here", image="https://snakemd.io", italics=True)
    assert str(text) == "_![Here](https://snakemd.io)_"
    assert (
        markdown.markdown(str(text))
        == '<p><em><img alt="Here" src="https://snakemd.io" /></em></p>'
    )


def test_inline_image_strikethroughed():
    text = Inline("Here", image="https://snakemd.io", strikethrough=True)
    assert str(text) == "~~![Here](https://snakemd.io)~~"
    # Strikethrough not supported in python markdown


def test_inline_image_coded():
    text = Inline("Here", image="https://snakemd.io", code=True)
    assert str(text) == "`![Here](https://snakemd.io)`"
    assert (
        markdown.markdown(str(text))
        == "<p><code>![Here](https://snakemd.io)</code></p>"
    )


def test_inline_link_bolded():
    text = Inline("Here", link="https://snakemd.io", bold=True)
    assert str(text) == "**[Here](https://snakemd.io)**"
    assert (
        markdown.markdown(str(text))
        == '<p><strong><a href="https://snakemd.io">Here</a></strong></p>'
    )


def test_inline_link_italicized():
    text = Inline("Here", link="https://snakemd.io", italics=True)
    assert str(text) == "_[Here](https://snakemd.io)_"
    assert (
        markdown.markdown(str(text))
        == '<p><em><a href="https://snakemd.io">Here</a></em></p>'
    )


def test_inline_link_strikethroughed():
    text = Inline("Here", link="https://snakemd.io", strikethrough=True)
    assert str(text) == "~~[Here](https://snakemd.io)~~"
    # Strikethrough not supported by python-markdown


def test_inline_link_coded():
    text = Inline("Here", link="https://snakemd.io", code=True)
    assert str(text) == "`[Here](https://snakemd.io)`"
    assert (
        markdown.markdown(str(text)) == "<p><code>[Here](https://snakemd.io)</code></p>"
    )


def test_inline_bold_italicized():
    text = Inline("Hello, World!", bold=True, italics=True)
    assert str(text) == "_**Hello, World!**_"
    assert (
        markdown.markdown(str(text)) == "<p><em><strong>Hello, World!</strong></em></p>"
    )


def test_inline_bold_strikethroughed():
    text = Inline("Hello, World!", bold=True, strikethrough=True)
    assert str(text) == "~~**Hello, World!**~~"
    # Strikethrough not supported by python-markdown


def test_inline_bold_coded():
    text = Inline("Hello, World!", bold=True, code=True)
    assert str(text) == "`**Hello, World!**`"
    assert markdown.markdown(str(text)) == "<p><code>**Hello, World!**</code></p>"


def test_inline_italics_strikethroughed():
    text = Inline("Hello, World!", italics=True, strikethrough=True)
    assert str(text) == "~~_Hello, World!_~~"
    # Strikethrough not supported by python-markdown


def test_inline_italics_coded():
    text = Inline("Hello, World!", italics=True, code=True)
    assert str(text) == "`_Hello, World!_`"
    assert markdown.markdown(str(text)) == "<p><code>_Hello, World!_</code></p>"


def test_inline_strikethrough_coded():
    text = Inline("Hello, World!", strikethrough=True, code=True)
    assert str(text) == "`~~Hello, World!~~`"
    assert markdown.markdown(str(text)) == "<p><code>~~Hello, World!~~</code></p>"


# Constructor tests (3-combos)


def test_inline_image_linked_bolded():
    text = Inline(
        "Here", image="https://snakemd.io", link="https://google.com", bold=True
    )
    assert str(text) == "**[![Here](https://snakemd.io)](https://google.com)**"
    assert (
        markdown.markdown(str(text))
        == '<p><strong><a href="https://google.com"><img alt="Here" src="https://snakemd.io" /></a></strong></p>'
    )


def test_inline_image_linked_italicized():
    text = Inline(
        "Here", image="https://snakemd.io", link="https://google.com", italics=True
    )
    assert str(text) == "_[![Here](https://snakemd.io)](https://google.com)_"


def test_inline_image_linked_strikethroughed():
    text = Inline(
        "Here",
        image="https://snakemd.io",
        link="https://google.com",
        strikethrough=True,
    )
    assert str(text) == "~~[![Here](https://snakemd.io)](https://google.com)~~"


def test_inline_image_linked_coded():
    text = Inline(
        "Here", image="https://snakemd.io", link="https://google.com", code=True
    )
    assert str(text) == "`[![Here](https://snakemd.io)](https://google.com)`"


def test_inline_image_bolded_italicized():
    text = Inline("Here", image="https://snakemd.io", bold=True, italics=True)
    assert str(text) == "_**![Here](https://snakemd.io)**_"


# Method tests


def test_inline_bold_method():
    text = Inline("Hello, World!").bold()
    assert isinstance(text, Inline)
    assert str(text) == "**Hello, World!**"


def test_inline_unbold_method():
    text = Inline("Hello, World!", bold=True).unbold()
    assert isinstance(text, Inline)
    assert str(text) == "Hello, World!"


def test_inline_italics_method():
    text = Inline("Hello, World!").italicize()
    assert isinstance(text, Inline)
    assert str(text) == "_Hello, World!_"


def test_inline_unitalics_method():
    text = Inline("Hello, World!", italics=True).unitalicize()
    assert isinstance(text, Inline)
    assert str(text) == "Hello, World!"


def test_inline_strikethrough_method():
    text = Inline("Hello, World!").strikethrough()
    assert isinstance(text, Inline)
    assert str(text) == "~~Hello, World!~~"


def test_inline_unstrikethrough_method():
    text = Inline("Hello, World!", strikethrough=True).unstrikethrough()
    assert isinstance(text, Inline)
    assert str(text) == "Hello, World!"


def test_inline_code_method():
    text = Inline("x = 5").code()
    assert isinstance(text, Inline)
    assert str(text) == "`x = 5`"


def test_inline_uncode_method():
    text = Inline("x = 5", code=True).uncode()
    assert isinstance(text, Inline)
    assert str(text) == "x = 5"


def test_inline_link_method():
    text = Inline("Here").link("https://snakemd.io")
    assert isinstance(text, Inline)
    assert str(text) == "[Here](https://snakemd.io)"


def test_inline_link_method():
    text = Inline("Here").unlink()
    assert isinstance(text, Inline)
    assert str(text) == "Here"


def test_reset_method():
    text = Inline("Howdy").reset()
    assert isinstance(text, Inline)
    assert not text._image
    assert not text._link
    assert not text._code
    assert not text._bold
    assert not text._italics
    assert not text._strikethrough


def test_reset_image_method():
    text = Inline("Howdy", image="https://snakemd.io").reset()
    assert isinstance(text, Inline)
    assert not text._image
    assert not text._link
    assert not text._code
    assert not text._bold
    assert not text._italics
    assert not text._strikethrough


def test_inline_is_text_text_method():
    is_text = Inline("Here").is_text()
    assert is_text


def test_inline_is_text_code_method():
    is_text = Inline("Here", code=True).is_text()
    assert not is_text


def test_inline_is_link_method():
    is_link = Inline("Hello", link="https://snakemd.io").is_link()
    assert is_link


def test_inline_is_link_method():
    is_link = Inline("Hello").is_link()
    assert not is_link
