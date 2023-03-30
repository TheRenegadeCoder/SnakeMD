from snakemd import Heading, InlineText


def test_heading_empty():
    heading = Heading("", 1)
    assert str(heading) == "# "


def test_heading_str_level_sub_one():
    heading = Heading("Example heading", 0)
    assert str(heading) == "# Example heading"


def test_heading_str_level_one():
    heading = Heading("Example heading", 1)
    assert str(heading) == "# Example heading"


def test_heading_inline_level_one():
    heading = Heading(InlineText("Example heading"), 1)
    assert str(heading) == "# Example heading"


def test_heading_str_level_two():
    heading = Heading("Example heading", 2)
    assert str(heading) == "## Example heading"


def test_heading_str_level_three():
    heading = Heading("Example heading", 3)
    assert str(heading) == "### Example heading"


def test_heading_str_level_four():
    heading = Heading("Example heading", 4)
    assert str(heading) == "#### Example heading"


def test_heading_str_level_five():
    heading = Heading("Example heading", 5)
    assert str(heading) == "##### Example heading"


def test_heading_str_level_six():
    heading = Heading("Example heading", 6)
    assert str(heading) == "###### Example heading"


def test_heading_str_level_sup_six():
    heading = Heading("Example heading", 7)
    assert str(heading) == "###### Example heading"


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
