import pytest

from snakemd import Inline, Paragraph, Table

# Constructor tests


def test_table_one_col_str():
    table = Table(["Age"], [["37"]])
    assert str(table) == "| Age |\n| --- |\n| 37  |"


def test_table_one_col_inline():
    table = Table([Inline("Age")], [[Inline("37")]])
    assert str(table) == "| Age |\n| --- |\n| 37  |"


def test_table_one_col_paragraph():
    table = Table([Paragraph(["Age"])], [[Paragraph(["37"])]])
    assert str(table) == "| Age |\n| --- |\n| 37  |"


def test_table_one_col_wide_body():
    table = Table(["Age"], [["2337"]])
    assert str(table) == "| Age  |\n| ---- |\n| 2337 |"


def test_table_two_col():
    table = Table(["Age", "Color"], [["37", "Blue"]])
    assert str(table) == "| Age | Color |\n| --- | ----- |\n| 37  | Blue  |"


def test_table_one_col_align_left():
    table = Table(["Age"], [["37"]], [Table.Align.LEFT])
    assert str(table) == "| Age |\n| :-- |\n| 37  |"


def test_table_one_col_align_right():
    table = Table(["Age"], [["37"]], [Table.Align.RIGHT])
    assert str(table) == "| Age |\n| --: |\n| 37  |"


def test_table_one_col_align_center():
    table = Table(["Age"], [["37"]], [Table.Align.CENTER])
    assert str(table) == "| Age |\n| :-: |\n| 37  |"


def test_table_mismatch_header_rows_lengths_exception():
    with pytest.raises(ValueError):
        Table(["Age"], [["2337", "342"]])


def test_table_mismatch_rows_lengths_exception():
    with pytest.raises(ValueError):
        Table(["Age"], [["2337"], ["321", "123"]])


# Method tests


def test_table_no_body_add_row_one():
    table = Table(["Age"])
    table.add_row(["25"])
    assert str(table) == "| Age |\n| --- |\n| 25  |"


def test_table_list_body_add_row_one():
    table = Table(["Age"], [["24"]])
    table.add_row(["25"])
    assert str(table) == "| Age |\n| --- |\n| 24  |\n| 25  |"


def test_table_list_body_add_row_one_wider():
    table = Table(["Age"], [["24"]])
    table.add_row(["2567"])
    assert str(table) == "| Age  |\n| ---- |\n| 24   |\n| 2567 |"


def test_table_generator_body_add_row_one():
    table = Table(["Age"], ([x] for x in ("24",)))
    table.add_row(["25"])
    assert str(table) == "| Age |\n| --- |\n| 24  |\n| 25  |"


def test_table_add_row_exception():
    with pytest.raises(ValueError):
        table = Table(["Age"])
        table.add_row(["25", "55"])


def test_repr_can_create_object():
    table = Table([])
    obj = eval(repr(table))
    assert isinstance(obj, Table)
