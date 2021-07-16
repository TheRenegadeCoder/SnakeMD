from snake.md import Document


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
