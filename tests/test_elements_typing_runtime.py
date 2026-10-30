"""Behavior of element inputs that affect their type contracts."""

from snakemd import Inline, Paragraph, Table


def test_table_keeps_mixed_added_cells_and_renders_them():
    table = Table(["a", "b", "c"], [["first", Inline("b"), Paragraph("c")]])
    table.add_row(["raw", Inline("bold", bold=True), Paragraph("text")])
    assert str(table) == (
        "| a     | b        | c    |\n"
        "| ----- | -------- | ---- |\n"
        "| first | b        | c    |\n"
        "| raw   | **bold** | text |"
    )
    assert "body=[[Paragraph(" in repr(table)
    assert "], ['raw', Inline(" in repr(table)
