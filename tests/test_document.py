from snakemd import Document


def test_document_empty():
    doc = Document("Test")
    assert str(doc) == ""


def test_document_add_header():
    doc = Document("Test")
    doc.add_header("Test Document")
    assert str(doc) == "# Test Document"


def test_document_add_paragraph():
    doc = Document("Test")
    doc.add_paragraph("Test Document")
    assert str(doc) == "Test Document"


def test_document_add_header_and_paragraph():
    doc = Document("Test")
    doc.add_header("Test Document")
    doc.add_paragraph("This is a test document.")
    assert str(doc) == "# Test Document\n\nThis is a test document."

def test_document_add_table_of_contents_empty():
    doc = Document("Test")
    doc.add_table_of_contents()
    assert str(doc) == ""

def test_document_add_table_of_contents_one_section():
    doc = Document("Test")
    doc.add_header("Section 1", level=2)
    doc.add_table_of_contents()
    print(str(doc))
    assert str(doc) == "## Section 1\n\n" \
        "1. [Section 1](#section-1)"
