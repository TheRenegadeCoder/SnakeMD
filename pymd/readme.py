from markdown import Document, MDList, Paragraph, InlineText


def main() -> None:
    """
    Generates the repo README.
    """
    doc = Document("README")

    # Introduction
    doc.add_header("Welcome to PyMD!")
    doc.add_paragraph("""PyMD is your ticket to generating markdown in Python. 
    To prove it to you, we've generated this entire README using PyMD.
    See readme.py for how it was done.""")
    doc.add_paragraph("""In the remainder of this document, we'll show you all of
    the things this library can do.""")

    # Table of Contents
    doc.add_header("Table of Contents", level=2)
    doc.add_table_of_contents()

    # Lists
    doc.add_header("Make a List!", level=2)
    doc.add_paragraph("""PyMD can make a variety of markdown lists. 
    The two main types of lists are ordered and unordered.""")

    # Ordered
    doc.add_header("Ordered List", level=3)
    doc.add_paragraph("""Ordered lists are lists in which the order of the 
    items matters. As a result, we number them.""")
    doc.add_code(
        'doc.add_ordered_list(["How", "Now", "Brown", "Cow"])', lang="py")
    doc.add_ordered_list(["How", "Now", "Brown", "Cow"])

    # Unordered
    doc.add_header("Unordered List", level=3)
    doc.add_code('doc.add_unordered_list(["Look", "at", "Me", "Now"])', lang="py")
    doc.add_unordered_list(["Look", "at", "Me", "Now"])

    # Nested
    doc.add_header("Nested Lists", level=3)
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

    # Tables
    doc.add_header("Make a Table!", level=2)
    doc.add_code("""doc.add_table(
    ["height", "weight", "age"], 
    [
        ['1', '2', '3'], 
        ['4', '5', '6'], 
        ['7', '8', '9']
    ]
)
    """,
                 lang="py")
    doc.add_table(
        ["height", "weight", "age"],
        [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
    )

    # Images
    logo = "https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png"
    doc.add_header("Testing image", level=2)
    doc.add_element(
        Paragraph([InlineText("Kitten", url=logo, image=True)])
    )
    doc.add_header("Testing Links", level=2)
    doc.add_element(Paragraph([InlineText("Doggo", url="google.com")]))
    doc.add_header("Testing Code", level=2)
    doc.add_code("x = 5")
    doc.add_header("Testing Quote", level=2)
    doc.add_quote("How Now Brown Cow")
    doc.output_page()


if __name__ == "__main__":
    main()
