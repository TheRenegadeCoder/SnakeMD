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
