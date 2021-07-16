from snake.md import Header


def test_header_empty():
    header = Header("", 1)
    assert str(header) == "# "

def test_header_str_level_one():
    header = Header("Example Header", 1)
    assert str(header) == "# Example Header"

def test_header_str_level_two():
    header = Header("Example Header", 2)
    assert str(header) == "## Example Header"

def test_header_str_level_three():
    header = Header("Example Header", 3)
    assert str(header) == "### Example Header"

def test_header_str_level_four():
    header = Header("Example Header", 4)
    assert str(header) == "#### Example Header"

def test_header_str_level_five():
    header = Header("Example Header", 5)
    assert str(header) == "##### Example Header"

def test_header_str_level_six():
    header = Header("Example Header", 6)
    assert str(header) == "###### Example Header"

def test_header_promote():
    header = Header("Example Header", 2)
    header.promote()
    assert str(header) == "# Example Header"

def test_header_promote_max():
    header = Header("Example Header", 1)
    header.promote()
    assert str(header) == "# Example Header"

def test_header_demote():
    header = Header("Example Header", 2)
    header.demote()
    assert str(header) == "### Example Header"

def test_header_demote_min():
    header = Header("Example Header", 6)
    header.demote()
    assert str(header) == "###### Example Header"
