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
    doc.add_element(Paragraph([InlineText("Kitten", url=logo, image=True)]))


def _code(doc: Document):
    doc.add_code("x = 5", lang="py")


def _paragraph(doc: Document):
    doc.add_paragraph("I think. Therefore, I am.")


def _quote(doc: Document):
    doc.add_quote("How Now Brown Cow")


def _section(doc: Document, title: str, desc: str, func):
    doc.add_header(title, level=2)
    doc.add_paragraph(desc)
    doc.add_code(inspect.getsource(func).strip(), lang="py")
    func(doc)

def main() -> None:
    """
    Generates the repo README.
    """
    doc = Document("README")

    # Introduction
    doc.add_header("Welcome to PyMD!")
    _introduction(doc)

    # Table of Contents
    _section(
        doc, 
        "Table of Contents",
        """Below you'll find the table of contents, but
        these can also be generated programatically for every markdown
        document.""",
        _table_of_contents
    )

    # Paragraphs
    doc.add_header("Paragraphs", level=2)
    doc.add_paragraph("""Paragraphs are the most basic feature of
    any markdown file. As a result, there very easy to create using
    PyMD.""")
    doc.add_code(inspect.getsource(_paragraph).strip(), lang="py")
    _paragraph(doc)

    # Links
    doc.add_header("Links", level=2)
    doc.add_paragraph("""Links are targets to files or web pages and
    can be embedded in a Paragraph just like images using InlineText.""")
    doc.add_code(inspect.getsource(_link).strip(), lang="py")
    _link(doc)

    # Images
    doc.add_header("Images", level=2)
    doc.add_paragraph("""Images can be added by embedding InlineText 
    in a Paragraph.""")
    doc.add_code(inspect.getsource(_image).strip(), lang="py")
    _image(doc)

    # Lists
    doc.add_header("Lists", level=2)
    doc.add_paragraph("""PyMD can make a variety of markdown lists. 
    The two main types of lists are ordered and unordered.""")

    # Ordered lists
    doc.add_header("Ordered List", level=3)
    doc.add_paragraph("""Ordered lists are lists in which the order of the 
    items matters. As a result, we number them.""")
    doc.add_code(inspect.getsource(_ordered_list).strip(), lang="py")
    _ordered_list(doc)

    # Unordered lists
    doc.add_header("Unordered List", level=3)
    doc.add_paragraph("""Unordered lists are lists in which the order of the
    items does not matter. As a result, we bullet them.""")
    doc.add_code(inspect.getsource(_unordered_list).strip(), lang="py")
    _unordered_list(doc)

    # Nested lists
    doc.add_header("Nested List", level=3)
    doc.add_paragraph("""Nested lists are complex lists that contain lists.
    Currently, PyMD does not support any convenience methods to generate
    nested lists, but they can be created manually using the MDList object.""")
    doc.add_code(inspect.getsource(_nested_list).strip(), lang="py")
    _nested_list(doc)

    # Tables
    doc.add_header("Tables", level=2)
    doc.add_paragraph("""Tables are sets of rows and columns which
    can display text in a grid. To style any of the contents of a
    table, consider using InlineText.""")
    doc.add_code(inspect.getsource(_table).strip(), lang="py")
    _table(doc)

    # Code
    doc.add_header("Code Blocks", level=2)
    doc.add_paragraph("""Code blocks are a form of structured text
    for sharing code snippets with syntax highlighting.""")
    doc.add_code(inspect.getsource(_code).strip(), lang="py")
    _code(doc)

    # Quote
    doc.add_header("Quotes", level=2)
    doc.add_paragraph("""Quotes are blocks of text that represent
    quotes from people.""")
    doc.add_code(inspect.getsource(_quote).strip(), lang="py")
    _quote(doc)

    doc.output_page()


if __name__ == "__main__":
    main()
