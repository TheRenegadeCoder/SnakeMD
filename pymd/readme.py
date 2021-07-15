from markdown import Document, MDList, Paragraph, InlineText
import inspect


def _introduction(doc: Document):
    doc.add_paragraph("""PyMD is your ticket to generating markdown in Python. 
    To prove it to you, we've generated this entire README using PyMD.
    See readme.py for how it was done.""")
    doc.add_paragraph("""In the remainder of this document, we'll show you all of
    the things this library can do.""")


def _table_of_contents(doc: Document):
    doc.add_table_of_contents()


def _ordered_list(doc: Document):
    doc.add_ordered_list(["How", "Now", "Brown", "Cow"])


def _unordered_list(doc: Document):
    doc.add_unordered_list(["Look", "at", "Me", "Now"])


def _nested_list(doc: Document):
    doc.add_element(
        MDList([
            InlineText("Outer"),
            InlineText("List"),
            MDList([
                InlineText("Inner"),
                InlineText("List")
            ]),
            InlineText("!!!")
        ])
    )


def _table(doc: Document):
    doc.add_table(
        ["height", "weight", "age"],
        [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
    )


def _link(doc: Document):
    doc.add_element(Paragraph([
        InlineText("Learn to program with"),
        InlineText("The Renegade Coder", url="https://therenegadecoder.com")
    ]))


def _image(doc: Document):
    logo = "https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png"
    doc.add_element(Paragraph([InlineText("Logo", url=logo, image=True)]))


def _code(doc: Document):
    doc.add_code("x = 5", lang="py")


def _paragraph(doc: Document):
    doc.add_paragraph("I think. Therefore, I am.")


def _quote(doc: Document):
    doc.add_quote("How Now Brown Cow")


def _section(doc: Document, title: str, desc: str, func, level: int=2):
    doc.add_header(title, level=level)
    doc.add_paragraph(desc)
    doc.add_element(Paragraph([InlineText("PyMD Source", bold=True)]))
    doc.add_code(inspect.getsource(func).strip(), lang="py")
    doc.add_element(Paragraph([InlineText("Rendered Result", bold=True)]))
    func(doc)
    doc.add_element(Paragraph([InlineText("Markdown Source", bold=True)]))
    doc.add_code(str(doc.contents[-2]), lang="markdown")
    doc.contents.insert(-3, doc.contents.pop())
    doc.contents.insert(-3, doc.contents.pop())

def main() -> None:
    """
    Generates the repo README.
    """
    doc = Document("README")

    # Introduction
    doc.add_header("Welcome to PyMD!")
    _introduction(doc)

    # Table of Contents
    doc.add_header("Table of Contents", level=2)
    doc.add_paragraph("""Below you'll find the table of contents, but
    these can also be generated programatically for every markdown
    document.""")
    doc.add_code(inspect.getsource(_table_of_contents).strip(), lang="py")
    _table_of_contents(doc)

    # Paragraphs
    _section(
        doc,
        "Paragraphs",
        """Paragraphs are the most basic feature of any markdown file. 
        As a result, they are very easy to create using PyMD.""",
        _paragraph
    )

    # Links
    _section(
        doc,
        "Links",
        """Links are targets to files or web pages and can be embedded 
        in a Paragraph just like images using InlineText.""",
        _link
    )

    # Images
    _section(
        doc,
        "Images",
        """Images can be added by embedding InlineText in a Paragraph.""",
        _image
    )

    # Lists
    doc.add_header("Lists", level=2)
    doc.add_paragraph("""PyMD can make a variety of markdown lists. 
    The two main types of lists are ordered and unordered.""")

    # Ordered lists
    _section(
        doc,
        "Ordered List",
        """Ordered lists are lists in which the order of the items 
        matters. As a result, we number them.""",
        _ordered_list,
        level=3
    )

    # Unordered lists
    _section(
        doc,
        "Unordered List",
        """Unordered lists are lists in which the order of the items 
        does not matter. As a result, we bullet them.""",
        _unordered_list,
        level=3
    )

    # Nested lists
    _section(
        doc,
        "Nested List",
        """Nested lists are complex lists that contain lists. Currently, 
        PyMD does not support any convenience methods to generate nested 
        lists, but they can be created manually using the MDList object.""",
        _nested_list,
        level=3
    )

    # Tables
    _section(
        doc,
        "Tables",
        """Tables are sets of rows and columns which can display text in a 
        grid. To style any of the contents of a table, consider using 
        InlineText.""",
        _table
    )

    # Code
    _section(
        doc,
        "Code Blocks",
        """Code blocks are a form of structured text for sharing code 
        snippets with syntax highlighting.""",
        _code
    )

    # ERROR: patch code block
    doc.contents[-3].backticks = 4

    # Quote
    doc.add_header("Quotes", level=2)
    doc.add_paragraph("""Quotes are blocks of text that represent
    quotes from people.""")
    doc.add_code(inspect.getsource(_quote).strip(), lang="py")
    _quote(doc)

    doc.output_page()


if __name__ == "__main__":
    main()
