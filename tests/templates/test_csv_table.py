import pytest

from snakemd.templates import CSVTable


def test_csv_table_type_error_none():
    """
    Verifies that None properly throws a TypeError.
    """
    with pytest.raises(TypeError):
        CSVTable(None)


def test_csv_table_file_not_found_error_empty():
    """
    Verifies that an empty string properly throws FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        CSVTable("")
        
def test_csv_table_sample_file():
    """
    Verifies that a sample CSV is properly converted into
    a Markdown table.
    """
    table = CSVTable("tests/resources/python-support.csv")
    table_lines = str(table).splitlines(keepends=True)
    with open("tests/resources/python-support.md") as md:
        for actual, expected in zip(md.readlines(), table_lines):
            assert actual == expected
            
