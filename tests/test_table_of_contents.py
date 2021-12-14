from snakemd.generator import Document, TableOfContents

def test_table_of_contents_empty():
    doc = Document("Empty Document")
    toc = TableOfContents(doc)
    assert str(toc) == ""

def test_table_of_contents_one_section():
    doc = Document("One Section")
    toc = TableOfContents(doc)
    doc.add_header("Section", level=2)
    assert str(toc) == "1. [Section](#section)"
