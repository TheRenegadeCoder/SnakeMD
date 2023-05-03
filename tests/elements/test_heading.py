import markdown
import pytest

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
    initializes as a level 2 heading. Also 
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
    initializes as a level 3 heading. Also 
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
    initializes as a level 4 heading. Also 
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
    initializes as a level 5 heading. Also 
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
    initializes as a level 6 heading. Also 
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
    
    
def test_heading_list():
    """
    Verifies that a Heading object properly 
    initializes with a list of Inline objects. 
    Also verifies that the repr string is 
    properly formatted and that the markdown 
    itself is properly rendered.
    """
    heading = Heading(["Example", " heading"], 1)
    assert str(heading) == "# Example heading"
    assert repr(heading) == (
        r"Heading("
        r"text=["
            r"Inline("
            r"text='Example', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
            r"), "
            r"Inline("
            r"text=' heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
            r")"
        r"]"
        r", level=1)"
    )
    assert markdown.markdown(str(heading)) == "<h1>Example heading</h1>"


def test_heading_list_styling():
    """
    Verifies that a Heading object properly 
    initializes with a list of Inline objects
    to allow for custom styling. Also verifies 
    that the repr string is properly formatted 
    and that the markdown itself is properly 
    rendered.
    """
    heading = Heading([Inline("Example", bold=True), " heading"], 1)
    assert str(heading) == "# **Example** heading"
    assert repr(heading) == (
        r"Heading("
        r"text=["
            r"Inline("
            r"text='Example', "
            r"image=None, "
            r"link=None, "
            r"bold=True, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
            r"), "
            r"Inline("
            r"text=' heading', "
            r"image=None, "
            r"link=None, "
            r"bold=False, "
            r"italics=False, "
            r"strikethrough=False, "
            r"code=False"
            r")"
        r"]"
        r", level=1)"
    )
    assert markdown.markdown(str(heading)) == "<h1><strong>Example</strong> heading</h1>"


def test_heading_str_level_zero_exception():
    """
    Verifies that a level provided below 1
    causes an exception to be thrown.
    """
    with pytest.raises(ValueError):
        Heading("Example heading", 0)


def test_heading_str_level_seven_exception():
    """
    Verifies that a level provided above 6
    causes an exception to be thrown.
    """
    with pytest.raises(ValueError):
        Heading("Example heading", 7)
        
    
# Method Tests


def test_heading_promote():
    """
    Verifies that heading can be correctly
    promoted from lower level to higher level.
    """
    heading = Heading("Example heading", 2)
    heading.promote()
    assert str(heading) == "# Example heading"


def test_heading_promote_max():
    """
    Verifies that heading at maximum level (i.e., 1)
    silently fails to promote.
    """
    heading = Heading("Example heading", 1)
    heading.promote()
    assert str(heading) == "# Example heading"


def test_heading_demote():
    """
    Verifies that heading can be correctly
    demoted from higher level to lower level.
    """
    heading = Heading("Example heading", 2)
    heading.demote()
    assert str(heading) == "### Example heading"


def test_heading_demote_min():
    """
    Verifies that heading at minimum level (i.e., 6)
    silently fails to demote.
    """
    heading = Heading("Example heading", 6)
    heading.demote()
    assert str(heading) == "###### Example heading"
    

def test_repr_can_create_object():
    """
    Verifies that the __repr__ method can correctly
    generate a string that can be used to create
    an identical code block.
    """
    heading = Heading("", 1)
    obj = eval(repr(heading))
    assert isinstance(obj, Heading) 
