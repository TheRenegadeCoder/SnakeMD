import pytest
from snakemd.templates import CSVTable


def test_csv_table_type_error_none():
    with pytest.raises(TypeError):
        CSVTable(None)


def test_csv_table_file_not_found_error_empty():
    with pytest.raises(FileNotFoundError):
        CSVTable("")
        
def test_csv_table_sample_file():
    table = CSVTable("tests/resources/python-support.csv")
    table_lines = str(table).splitlines(keepends=True)
    with open("tests/resources/python-support.md") as md:
        for actual, expected in zip(md.readlines(), table_lines):
            assert actual == expected
            
