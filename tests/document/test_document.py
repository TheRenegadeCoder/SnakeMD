import os

from snakemd import Document, Heading, HorizontalRule, Paragraph, Alert

# Method tests (singles)


def test_document_empty():
    doc = Document()
    assert str(doc) == ""
    assert repr(doc) == "Document(elements=[])"


def test_document_add_heading():
    doc = Document()
    heading = doc.add_heading("Test Document")
    assert isinstance(heading, Heading)
    assert str(heading) == "# Test Document"
    assert str(doc) == "# Test Document"


def test_document_add_paragraph():
    doc = Document()
    paragraph = doc.add_paragraph("Test Document")
    assert isinstance(paragraph, Paragraph)
    assert str(paragraph) == "Test Document"
    assert str(doc) == "Test Document"


def test_add_raw():
    doc = Document()
    doc.add_raw("x: 5\ny: 2")
    assert str(doc) == "x: 5\ny: 2"


def test_add_ordered_list_empty():
    doc = Document()
    doc.add_ordered_list([])
    assert str(doc) == ""


def test_add_ordered_list_one():
    doc = Document()
    doc.add_ordered_list(["Treat"])
    assert str(doc) == "1. Treat"


def test_add_ordered_list_many():
    doc = Document()
    doc.add_ordered_list(["Treat", "Candy", "Food"])
    assert str(doc) == "1. Treat\n2. Candy\n3. Food"


def test_add_unordered_list_empty():
    doc = Document()
    doc.add_unordered_list([])
    assert str(doc) == ""


def test_add_unordered_list_one():
    doc = Document()
    doc.add_unordered_list(["Treat"])
    assert str(doc) == "- Treat"


def test_add_unordered_list_many():
    doc = Document()
    doc.add_unordered_list(["Treat", "Candy", "Food"])
    assert str(doc) == "- Treat\n- Candy\n- Food"


def test_add_checklist_empty():
    doc = Document()
    doc.add_checklist([])
    assert str(doc) == ""


def test_add_checklist_one():
    doc = Document()
    doc.add_checklist(["Treat"])
    assert str(doc) == "- [ ] Treat"


def test_add_checklist_many():
    doc = Document()
    doc.add_checklist(["Treat", "Candy", "Food"])
    assert str(doc) == "- [ ] Treat\n- [ ] Candy\n- [ ] Food"


def test_add_horizontal_rule():
    doc = Document()
    doc.add_horizontal_rule()
    assert str(doc) == "***"


def test_document_add_table_of_contents_empty():
    doc = Document()
    doc.add_table_of_contents()
    assert str(doc) == ""


def test_document_add_table_of_contents_one_section():
    doc = Document()
    doc.add_heading("Section 1", level=2)
    doc.add_table_of_contents()
    assert str(doc) == "## Section 1\n\n" "1. [Section 1](#section-1)"


def test_document_add_table_of_contents_many_section():
    doc = Document()
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Section 2", level=2)
    doc.add_heading("Section 3", level=2)
    doc.add_table_of_contents()
    assert (
        str(doc) == "## Section 1\n\n"
        "## Section 2\n\n"
        "## Section 3\n\n"
        "1. [Section 1](#section-1)\n"
        "2. [Section 2](#section-2)\n"
        "3. [Section 3](#section-3)"
    )


def test_add_quote():
    doc = Document()
    doc.add_quote("Hello, World!")
    assert str(doc) == "> Hello, World!"


def test_add_code():
    doc = Document()
    doc.add_code("y = 15")
    assert str(doc) == """```generic\ny = 15\n```"""


def test_add_table_one_row():
    doc = Document()
    doc.add_table(["x", "y"], [["1", "2"]])
    assert str(doc) == "| x | y |\n| - | - |\n| 1 | 2 |"


def test_add_block_horizontal_rule():
    doc = Document()
    doc.add_block(HorizontalRule())
    assert str(doc) == "***"


def test_add_alert():
    doc = Document()
    doc.add_alert("Do not the cat", Alert.Kind.CAUTION)
    assert str(doc) == "> [!CAUTION]\n> Do not the cat"


def test_scramble_empty():
    doc = Document()
    doc.scramble()
    assert str(doc) == ""


def test_dump_empty():
    doc = Document()
    doc.dump("test")
    with open("test.md") as f:
        contents = "\n".join(f.readlines())
        assert contents == str(doc)
    os.remove("test.md")


# Method tests (2-combos)


def test_document_add_heading_and_paragraph():
    doc = Document()
    doc.add_heading("Test Document")
    doc.add_paragraph("This is a test document.")
    assert str(doc) == "# Test Document\n\nThis is a test document."
