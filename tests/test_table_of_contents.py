from snakemd.generator import Document, TableOfContents


def test_table_of_contents_empty():
    doc = Document()
    toc = TableOfContents(doc)
    assert str(toc) == ""


def test_table_of_contents_one_section():
    doc = Document()
    toc = TableOfContents(doc)
    doc.add_heading("Section", level=2)
    assert str(toc) == "1. [Section](#section)"


def test_table_of_contents_many_sections():
    doc = Document()
    toc = TableOfContents(doc)
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Section 2", level=2)
    doc.add_heading("Section 3", level=2)
    assert str(toc) == \
        "1. [Section 1](#section-1)\n" \
        "2. [Section 2](#section-2)\n" \
        "3. [Section 3](#section-3)"


def test_table_of_contents_many_sections_and_subsections_limit_h2():
    doc = Document()
    toc = TableOfContents(doc)
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Subsection 1", level=3)
    doc.add_heading("Subsection 2", level=3)
    doc.add_heading("Section 2", level=2)
    doc.add_heading("Subsection 3", level=3)
    assert str(toc) == \
        "1. [Section 1](#section-1)\n" \
        "2. [Section 2](#section-2)"


def test_table_of_contents_many_sections_and_subsections_limit_h2_h3():
    doc = Document()
    toc = TableOfContents(doc, levels=range(2, 4))
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Subsection 1", level=3)
    doc.add_heading("Subsection 2", level=3)
    doc.add_heading("Section 2", level=2)
    doc.add_heading("Subsection 3", level=3)
    assert str(toc) == \
        "1. [Section 1](#section-1)\n" \
        "   1. [Subsection 1](#subsection-1)\n" \
        "   2. [Subsection 2](#subsection-2)\n" \
        "2. [Section 2](#section-2)\n" \
        "   1. [Subsection 3](#subsection-3)"


def test_table_of_contents_double_digit_sections():
    doc = Document()
    toc = TableOfContents(doc, levels=range(2, 4))
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Subsection 1A", level=3)
    doc.add_heading("Subsection 1B", level=3)
    doc.add_heading("Section 2", level=2)
    doc.add_heading("Subsection 2A", level=3)
    doc.add_heading("Section 3", level=2)
    doc.add_heading("Section 4", level=2)
    doc.add_heading("Section 5", level=2)
    doc.add_heading("Section 6", level=2)
    doc.add_heading("Section 7", level=2)
    doc.add_heading("Section 8", level=2)
    doc.add_heading("Section 9", level=2)
    doc.add_heading("Section 10", level=2)
    doc.add_heading("Subsection 10A", level=3)
    assert str(toc) == \
        "1. [Section 1](#section-1)\n" \
        "   1. [Subsection 1A](#subsection-1a)\n" \
        "   2. [Subsection 1B](#subsection-1b)\n" \
        "2. [Section 2](#section-2)\n" \
        "   1. [Subsection 2A](#subsection-2a)\n" \
        "3. [Section 3](#section-3)\n" \
        "4. [Section 4](#section-4)\n" \
        "5. [Section 5](#section-5)\n" \
        "6. [Section 6](#section-6)\n" \
        "7. [Section 7](#section-7)\n" \
        "8. [Section 8](#section-8)\n" \
        "9. [Section 9](#section-9)\n" \
        "10. [Section 10](#section-10)\n" \
        "    1. [Subsection 10A](#subsection-10a)"


def test_table_of_contents_triple_nesting():
    doc = Document()
    toc = TableOfContents(doc, levels=range(2, 5))
    doc.add_heading("Section 1", level=2)
    doc.add_heading("Subsection 1A", level=3)
    doc.add_heading("Subsubsection 1Ai", level=4)
    assert str(toc) == \
        "1. [Section 1](#section-1)\n" \
        "   1. [Subsection 1A](#subsection-1a)\n" \
        "      1. [Subsubsection 1Ai](#subsubsection-1ai)"
