from snake.md import Table


def test_table_one():
    table = Table(["Age"], [["37"]])
    assert str(table) == "| Age |\n| --- |\n| 37  |"
