import pytest
import markdown
from snakemd import Heading, Inline


# Constructor Tests


def test_heading_empty():
    """
    Verifies that an empty string Heading object
    properly initializes. Also verifies that
    the repr string is properly formatted
    and that the markdown itself is properly
    rendered.
    """
    heading = Heading("", 1)
    assert str(heading) == "# "
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=1)"
    )
    assert markdown.markdown(str(heading)) == "<h1></h1>"


def test_heading_str_level_one():
    """
    Verifies that a Heading object properly 
    initializes with a typical string. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading("Example heading", 1)
    assert str(heading) == "# Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=1)"
    )
    assert markdown.markdown(str(heading)) == "<h1>Example heading</h1>"


def test_heading_inline_level_one():
    """
    Verifies that a Heading object properly 
    initializes with an Inline string. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading(Inline("Example heading"), 1)
    assert str(heading) == "# Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=1)"
    )
    assert markdown.markdown(str(heading)) == "<h1>Example heading</h1>"


def test_heading_inline_bold_level_one():
    """
    Verifies that a Heading object properly 
    initializes with a custom Inline string. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading(Inline("Example heading", bold=True), 1)
    assert str(heading) == "# **Example heading**"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=True, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=1)"
    )
    assert markdown.markdown(str(heading)) == "<h1><strong>Example heading</strong></h1>"


def test_heading_str_level_two():
    """
    Verifies that a Heading object properly 
    initializes with as a level 2 heading. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading("Example heading", 2)
    assert str(heading) == "## Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=2)"
    )
    assert markdown.markdown(str(heading)) == "<h2>Example heading</h2>"


def test_heading_str_level_three():
    """
    Verifies that a Heading object properly 
    initializes with as a level 3 heading. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading("Example heading", 3)
    assert str(heading) == "### Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=3)"
    )
    assert markdown.markdown(str(heading)) == "<h3>Example heading</h3>"


def test_heading_str_level_four():
    """
    Verifies that a Heading object properly 
    initializes with as a level 4 heading. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading("Example heading", 4)
    assert str(heading) == "#### Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=4)"
    )
    assert markdown.markdown(str(heading)) == "<h4>Example heading</h4>"


def test_heading_str_level_five():
    """
    Verifies that a Heading object properly 
    initializes with as a level 5 heading. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading("Example heading", 5)
    assert str(heading) == "##### Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=5)"
    )
    assert markdown.markdown(str(heading)) == "<h5>Example heading</h5>"


def test_heading_str_level_six():
    """
    Verifies that a Heading object properly 
    initializes with as a level 6 heading. Also 
    verifies that the repr string is properly 
    formatted and that the markdown itself is 
    properly rendered.
    """
    heading = Heading("Example heading", 6)
    assert str(heading) == "###### Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=[Inline("
            r"text='Example heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
        r")]"
        r", level=6)"
    )
    assert markdown.markdown(str(heading)) == "<h6>Example heading</h6>"


def test_heading_str_level_zero_exception():
    with pytest.raises(ValueError):
        Heading("Example heading", 0)


def test_heading_str_level_seven_exception():
    with pytest.raises(ValueError):
        Heading("Example heading", 7)
        
    
# Method Tests


def test_heading_promote():
    heading = Heading("Example heading", 2)
    heading.promote()
    assert str(heading) == "# Example heading"


def test_heading_promote_max():
    heading = Heading("Example heading", 1)
    heading.promote()
    assert str(heading) == "# Example heading"


def test_heading_demote():
    heading = Heading("Example heading", 2)
    heading.demote()
    assert str(heading) == "### Example heading"


def test_heading_demote_min():
    heading = Heading("Example heading", 6)
    heading.demote()
    assert str(heading) == "###### Example heading"


def test_heading_list():
    heading = Heading(["Example", " heading"], 1)
    assert str(heading) == "# Example heading"


def test_heading_list_styling():
    heading = Heading([Inline("Example", bold=True), " heading"], 1)
    assert str(heading) == "# **Example** heading"
    

def test_repr_can_create_object():
    heading = Heading("", 1)
    obj = eval(repr(heading))
    assert isinstance(obj, Heading) 
