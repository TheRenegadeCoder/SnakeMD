from snakemd import InlineText, Paragraph, Table


def test_table_one_col_str():
    table = Table(["Age"], [["37"]])
    assert str(table) == "| Age |\n| --- |\n| 37  |"


def test_table_one_col_inline():
    table = Table([InlineText("Age")], [[InlineText("37")]])
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
