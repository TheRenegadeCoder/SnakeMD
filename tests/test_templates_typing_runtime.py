"""Runtime contracts represented by template annotations."""

import pytest

from snakemd import Alert, Heading, TableOfContents


def test_alert_retains_iterable_representation():
    assert str(Alert(["one", "two"], Alert.Kind.NOTE)) == (
        "> [!NOTE]\n> ['one', 'two']"
    )


def test_table_of_contents_load_state():
    toc = TableOfContents()
    with pytest.raises(TypeError, match="not iterable"):
        str(toc)
    toc.load([Heading("Section", 2)])
    assert str(toc) == "1. [Section](#section)"
