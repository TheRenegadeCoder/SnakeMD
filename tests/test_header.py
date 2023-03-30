from snakemd import Heading, InlineText


def test_header_empty():
    header = Heading("", 1)
    assert str(header) == "# "


def test_header_str_level_sub_one():
    header = Heading("Example Header", 0)
    assert str(header) == "# Example Header"


def test_header_str_level_one():
    header = Heading("Example Header", 1)
    assert str(header) == "# Example Header"


def test_header_inline_level_one():
    header = Heading(InlineText("Example Header"), 1)
    assert str(header) == "# Example Header"


def test_header_str_level_two():
    header = Heading("Example Header", 2)
    assert str(header) == "## Example Header"


def test_header_str_level_three():
    header = Heading("Example Header", 3)
    assert str(header) == "### Example Header"


def test_header_str_level_four():
    header = Heading("Example Header", 4)
    assert str(header) == "#### Example Header"


def test_header_str_level_five():
    header = Heading("Example Header", 5)
    assert str(header) == "##### Example Header"


def test_header_str_level_six():
    header = Heading("Example Header", 6)
    assert str(header) == "###### Example Header"


def test_header_str_level_sup_six():
    header = Heading("Example Header", 7)
    assert str(header) == "###### Example Header"


def test_header_promote():
    header = Heading("Example Header", 2)
    header.promote()
    assert str(header) == "# Example Header"


def test_header_promote_max():
    header = Heading("Example Header", 1)
    header.promote()
    assert str(header) == "# Example Header"


def test_header_demote():
    header = Heading("Example Header", 2)
    header.demote()
    assert str(header) == "### Example Header"


def test_header_demote_min():
    header = Heading("Example Header", 6)
    header.demote()
    assert str(header) == "###### Example Header"
