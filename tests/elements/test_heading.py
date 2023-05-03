import pytest

from snakemd import Heading, Inline


# Constructor Tests


def test_heading_empty():
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


def test_heading_str_level_one():
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


def test_heading_inline_level_one():
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


def test_heading_inline_bold_level_one():
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


def test_heading_str_level_two():
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


def test_heading_str_level_three():
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


def test_heading_str_level_four():
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


def test_heading_str_level_five():
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


def test_heading_str_level_six():
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
