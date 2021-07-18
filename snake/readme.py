from snake.md import Document, MDList, Paragraph, InlineText
import inspect


def _introduction(doc: Document):
    doc.add_paragraph(
        """
        SnakeMD is your ticket to generating markdown in Python. 
        To prove it to you, we've generated this entire README using SnakeMD.
        See readme.py for how it was done. To get started, download and install SnakeMD:
        """
    )
    doc.add_code("pip install snakemd", lang="shell")
    p = doc.add_paragraph(
        """
        In the remainder of this document, we'll show you all of
        the things this library can do. For more information, check
        out the official documentation here.
        """
    )
    p.insert_link("here", "https://snakemd.therenegadecoder.com")


def _table_of_contents(doc: Document):
    doc.add_table_of_contents()


def _ordered_list(doc: Document):
    doc.add_ordered_list(["Deku", "Bakugo", "Uraraka", "Tsuyu"])


def _unordered_list(doc: Document):
    doc.add_unordered_list(["Crosby", "Malkin", "Lemieux"])


def _nested_list(doc: Document):
    doc.add_element(
        MDList([
            InlineText("Apples"),
            InlineText("Onions"),
            MDList([
                InlineText("Sweet"),
                InlineText("Red")
            ]),
            InlineText("Grapes")
        ])
    )


def _table(doc: Document):
    doc.add_table(
        ["Height (cm)", "Weight (kg)", "Age (y)"],
        [
            ['150', '70', '21'],
            ['164', '75', '19'],
            ['181', '87', '40']
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


def _horizontal_rule(doc: Document):
    doc.add_horizontal_rule()


def _section(doc: Document, title: str, desc: str, func, level: int = 2):
    doc.add_header(title, level=level)
    doc.add_paragraph(desc)
    doc.add_element(Paragraph([InlineText("SnakeMD Source", italics=True)]))
    doc.add_code(inspect.getsource(func).strip(), lang="py")
    doc.add_element(Paragraph([InlineText("Rendered Result", italics=True)]))
    func(doc)
    doc.add_element(Paragraph([InlineText("Markdown Source", italics=True)]))
    doc.add_code(str(doc._contents[-2]), lang="markdown")
    doc._contents.insert(-3, doc._contents.pop())
    doc._contents.insert(-3, doc._contents.pop())


def main() -> None:
    """
    Generates the repo README.
    """
    doc = Document("README")

    # Introduction
    doc.add_header("Welcome to SnakeMD!")
    _introduction(doc)

    # Table of Contents
    doc.add_header("Table of Contents", level=2)
    doc.add_paragraph(
        """
        Below you'll find the table of contents, but
        these can also be generated programatically for every markdown
        document.
        """
    )
    doc.add_code(inspect.getsource(_table_of_contents).strip(), lang="py")
    _table_of_contents(doc)

    # Paragraphs
    _section(
        doc,
        "Paragraphs",
        """
        Paragraphs are the most basic feature of any markdown file. 
        As a result, they are very easy to create using SnakeMD.
        """,
        _paragraph
    )

    # Links
    _section(
        doc,
        "Links",
        """
        Links are targets to files or web pages and can be embedded 
        in a Paragraph using InlineText.
        """,
        _link
    )

    # Images
    _section(
        doc,
        "Images",
        "Images can be added by embedding InlineText in a Paragraph.",
        _image
    )

    # Lists
    doc.add_header("Lists", level=2)
    doc.add_paragraph(
        """
        SnakeMD can make a variety of markdown lists. The two main types 
        of lists are ordered and unordered.
        """
    )

    # Ordered lists
    _section(
        doc,
        "Ordered List",
        """
        Ordered lists are lists in which the order of the items 
        matters. As a result, we number them.
        """,
        _ordered_list,
        level=3
    )

    # Unordered lists
    _section(
        doc,
        "Unordered List",
        """
        Unordered lists are lists in which the order of the items 
        does not matter. As a result, we bullet them.
        """,
        _unordered_list,
        level=3
    )

    # Nested lists
    _section(
        doc,
        "Nested List",
        """
        Nested lists are complex lists that contain lists. Currently, 
        SnakeMD does not support any convenience methods to generate nested 
        lists, but they can be created manually using the MDList object.
        """,
        _nested_list,
        level=3
    )

    # Tables
    _section(
        doc,
        "Tables",
        """
        Tables are sets of rows and columns which can display text in a 
        grid. To style any of the contents of a table, consider using 
        InlineText.
        """,
        _table
    )

    # Code
    _section(
        doc,
        "Code Blocks",
        """
        Code blocks are a form of structured text for sharing code 
        snippets with syntax highlighting.
        """,
        _code
    )

    # ERROR: patch code block
    doc._contents[-3]._backticks = 4

    # Quote
    _section(
        doc,
        "Quotes",
        "Quotes are blocks of text that represent quotes from people.",
        _quote
    )

    _section(
        doc,
        "Horizontal Rule",
        "Horizontal Rules are visible dividers in a document.",
        _horizontal_rule
    )

    doc.check_for_errors()
    doc.output_page()


if __name__ == "__main__":
    main()
