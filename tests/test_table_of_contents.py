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


def test_table_of_contents_many_sections():
    doc = Document("Many Sections")
    toc = TableOfContents(doc)
    doc.add_header("Section 1", level=2)
    doc.add_header("Section 2", level=2)
    doc.add_header("Section 3", level=2)
    assert str(toc) == "1. [Section 1](#section-1)\n" \
        "2. [Section 2](#section-2)\n" \
        "3. [Section 3](#section-3)"


def test_table_of_contents_many_sections_and_subsections_limit_h2():
    doc = Document("Many Sections and Subsections")
    toc = TableOfContents(doc)
    doc.add_header("Section 1", level=2)
    doc.add_header("Subsection 1", level=3)
    doc.add_header("Subsection 2", level=3)
    doc.add_header("Section 2", level=2)
    doc.add_header("Subsection 3", level=3)
    assert str(toc) == "1. [Section 1](#section-1)\n" \
        "2. [Section 2](#section-2)"


def test_table_of_contents_many_sections_and_subsections_limit_h2_h3():
    doc = Document("Many Sections and Subsections")
    toc = TableOfContents(doc, levels=range(2, 4))
    doc.add_header("Section 1", level=2)
    doc.add_header("Subsection 1", level=3)
    doc.add_header("Subsection 2", level=3)
    doc.add_header("Section 2", level=2)
    doc.add_header("Subsection 3", level=3)
    assert str(toc) == "1. [Section 1](#section-1)\n" \
        "   1. [Subsection 1](#subsection-1)\n" \
        "   2. [Subsection 2](#subsection-2)\n" \
        "2. [Section 2](#section-2)\n" \
        "   1. [Subsection 3](#subsection-3)"
