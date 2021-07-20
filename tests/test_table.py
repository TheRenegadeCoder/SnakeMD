from snake.md import Table


def test_table_one_col():
    table = Table(["Age"], [["37"]])
    assert str(table) == "| Age |\n| --- |\n| 37  |"

def test_table_one_col_wide_body():
    table = Table(["Age"], [["2337"]])
    assert str(table) == "| Age  |\n| ---- |\n| 2337 |"

def test_table_two_col():
    table = Table(["Age", "Color"], [["37", "Blue"]])
    assert str(table) == "| Age | Color |\n| --- | ----- |\n| 37  | Blue  |"
