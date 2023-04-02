from snakemd import Document


# Method tests (singles)


def test_document_empty():
    doc = Document()
    assert str(doc) == ""


def test_document_add_heading():
    doc = Document()
    doc.add_heading("Test Document")
    assert str(doc) == "# Test Document"


def test_document_add_paragraph():
    doc = Document()
    doc.add_paragraph("Test Document")
    assert str(doc) == "Test Document"


def test_add_raw():
    doc = Document()
    doc.add_raw("x: 5\ny: 2")
    assert str(doc) == "x: 5\ny: 2"


def test_document_add_table_of_contents_empty():
    doc = Document()
    doc.add_table_of_contents()
    assert str(doc) == ""


def test_document_add_table_of_contents_one_section():
    doc = Document()
    doc.add_heading("Section 1", level=2)
    doc.add_table_of_contents()
    assert str(doc) == "## Section 1\n\n" \
        "1. [Section 1](#section-1)"


def test_document_add_table_of_contents_many_section():
    doc = Document()
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Section 2", level=2)
    doc.add_heading("Section 3", level=2)
    doc.add_table_of_contents()
    assert str(doc) == "## Section 1\n\n" \
        "## Section 2\n\n" \
        "## Section 3\n\n" \
        "1. [Section 1](#section-1)\n" \
        "2. [Section 2](#section-2)\n" \
        "3. [Section 3](#section-3)"


# Method tests (2-combos)


def test_document_add_heading_and_paragraph():
    doc = Document()
    doc.add_heading("Test Document")
    doc.add_paragraph("This is a test document.")
    assert str(doc) == "# Test Document\n\nThis is a test document."
