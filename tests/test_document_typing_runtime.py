"""Runtime behavior of the iterable inputs exposed by Document.add_table."""

from snakemd import Document, Table


def test_add_table_consumes_iterators_and_preserves_alignment():
    doc = Document()
    header = iter(("name", "value"))
    data = (iter(row) for row in (("one", "1"), ("two", "2")))
    table = doc.add_table(header, data, align=(Table.Align.LEFT, Table.Align.RIGHT))

    assert str(table) == (
        "| name | value |\n"
        "| :--- | ----: |\n"
        "| one  | 1     |\n"
        "| two  | 2     |"
    )
    assert str(doc) == str(table)
