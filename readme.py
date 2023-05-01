from __future__ import annotations

import inspect
import logging
from typing import Callable

from snakemd import Block, Code, Document, Inline, MDList, Paragraph, Table


def _introduction(doc: Document):
    doc.add_paragraph(
        """
        SnakeMD is your ticket to generating Markdown in Python.
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
    p.insert_link("here", "https://snakemd.io")


def _table_of_contents(doc: Document):
    doc.add_table_of_contents(range(2, 4))


def _ordered_list(doc: Document):
    doc.add_ordered_list(["Deku", "Bakugo", "Uraraka", "Tsuyu"])


def _unordered_list(doc: Document):
    doc.add_unordered_list(["Crosby", "Malkin", "Lemieux"])


def _checklist(doc: Document):
    doc.add_checklist(["Pass the puck", "Shoot the puck", "Score a goal"])


def _nested_list(doc: Document):
    doc.add_block(
        MDList(
            [
                "Apples",
                Inline("Onions", bold=True),
                MDList(["Sweet", "Red"]),
                Paragraph(["This is the end of the list!"]),
            ]
        )
    )


def _table(doc: Document):
    doc.add_table(
        ["Height (cm)", "Weight (kg)", "Age (y)"],
        [["150", "70", "21"], ["164", "75", "19"], ["181", "87", "40"]],
        [Table.Align.LEFT, Table.Align.CENTER, Table.Align.RIGHT],
        0,
    )


def _insert_link(doc: Document):
    doc.add_paragraph(
        "Learn to program with The Renegade Coder (@RenegadeCoder94)."
    ).insert_link("The Renegade Coder", "https://therenegadecoder.com").insert_link(
        "@RenegadeCoder94", "https://twitter.com/RenegadeCoder94"
    )


def _image(doc: Document):
    logo = "https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png"
    doc.add_block(Paragraph([Inline("Logo", image=logo)]))


def _code(doc: Document):
    doc.add_code("x = 5", lang="py")


def _paragraph(doc: Document):
    doc.add_paragraph("I think. Therefore, I am.")


def _quote(doc: Document):
    doc.add_quote("How Now Brown Cow")


def _horizontal_rule(doc: Document):
    doc.add_horizontal_rule()


def _raw(doc: Document):
    doc.add_raw("4<sup>2</sup> = 16<br />How cool is that?")


def _section(doc: Document, title: str, desc: str, func: Callable, level: int = 2):
    doc.add_heading(title, level=level)
    doc.add_paragraph(desc)
    doc.add_block(Paragraph([Inline("SnakeMD Source", italics=True)]))
    doc.add_code(inspect.getsource(func).strip(), lang="py")
    doc.add_block(Paragraph([Inline("Rendered Result", italics=True)]))
    func(doc)
    doc.add_block(Paragraph([Inline("Markdown Source", italics=True)]))
    block: Block = doc._contents[-2]
    doc.add_block(
        Code(block if isinstance(block, Code) else str(block), lang="markdown")
    )
    doc._contents.insert(-3, doc._contents.pop())
    doc._contents.insert(-3, doc._contents.pop())


def main() -> None:
    """Generates the repo README."""
    doc = Document()

    # Introduction
    doc.add_heading("Welcome to SnakeMD")
    _introduction(doc)

    # Table of Contents
    doc.add_heading("Table of Contents", level=2)
    doc.add_paragraph(
        """
        Below you'll find the table of contents, but
        these can also be generated programatically for every Markdown
        document as follows:
        """
    )
    doc.add_code(inspect.getsource(_table_of_contents).strip(), lang="py")
    _table_of_contents(doc)

    # Paragraphs
    _section(
        doc,
        "Paragraphs",
        """
        Paragraphs are the most basic feature of any Markdown file.
        As a result, they are very easy to create using SnakeMD.
        """,
        _paragraph,
    )

    # Insert Links
    _section(
        doc,
        "Links",
        """
        Links are targets to files or web pages and can be embedded
        in paragraphs in a variety of ways, such as with the insert_link()
        method.
        """,
        _insert_link,
    )

    # Images
    _section(
        doc,
        "Images",
        "Images can be added by embedding Inline elements in a paragraph.",
        _image,
    )

    # Lists
    doc.add_heading("Lists", level=2)
    doc.add_paragraph(
        """
        SnakeMD can make a variety of Markdown lists. The three main types
        of lists are ordered, unordered, and checked.
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
        level=3,
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
        level=3,
    )

    # Checklist
    _section(
        doc,
        "Checklist",
        """
        Checklists are lists in which the items themselves can be
        checked on and off. This feature is new as of v0.10.0.
        """,
        _checklist,
        level=3,
    )

    # Nested lists
    _section(
        doc,
        "Nested Lists",
        """
        Nested lists are complex lists that contain lists. Currently,
        SnakeMD does not support any convenience methods to generate nested
        lists, but they can be created manually using the MDList object.
        """,
        _nested_list,
        level=3,
    )

    # Tables
    _section(
        doc,
        "Tables",
        """
        Tables are sets of rows and columns which can display text in a
        grid. To style any of the contents of a table, consider using
        Paragraph or Inline.
        """,
        _table,
    )

    # Code
    _section(
        doc,
        "Code Blocks",
        """
        Code blocks are a form of structured text for sharing code
        snippets with syntax highlighting.
        """,
        _code,
    )

    # Quote
    _section(
        doc,
        "Quotes",
        "Quotes are blocks of text that represent quotes from people.",
        _quote,
    )

    _section(
        doc,
        "Horizontal Rule",
        "Horizontal Rules are visible dividers in a document.",
        _horizontal_rule,
    )

    _section(
        doc,
        "Raw",
        """
        If at any time SnakeMD doesn't meet your needs, you can
        always add your own text using a raw block. These can
        be used to insert any preformatted text you like,
        such as HTML tags, Jekyll frontmatter, and more.
        """,
        _raw,
    )

    doc.dump("README")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
