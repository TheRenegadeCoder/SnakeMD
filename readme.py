from markdown import Document, MDList, Paragraph, InlineText


doc = Document("README")

# Introduction
doc.add_header("Welcome to PyMD!")
doc.add_paragraph("""PyMD is your ticket to generating markdown in Python. 
To prove it to you, we've generated this entire README using the library.
See readme.py for how it was done.""")
doc.add_paragraph("""In the remainder of this document, we'll show you all of
the things this library can do.""")

# Lists
doc.add_header("Make a list!", level=2)
doc.add_paragraph("""PyMD can make a variety of markdown lists. 
The two main types of lists are ordered and unordered.""")
doc.add_header("Ordered List", level=3)
doc.add_code('doc.add_ordered_list(["How", "Now", "Brown", "Cow"])', lang="py")
doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
doc.add_header("Unordered List", level=3)
doc.add_unordered_list(["Look", "at", "Me", "Now"])
doc.add_header("Testing nesting", level=2)
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
doc.add_table([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
doc.add_header("Testing image", level=2)
doc.add_element(Paragraph([InlineText("Kitten", url="D:\OneDrive\E-Documents\Work\Employers\ME\The Renegade Coder\Assets\Logos\Icon\icon-360x360.png", image=True)]))
doc.add_header("Testing Links", level=2)
doc.add_element(Paragraph([InlineText("Doggo", url="google.com")]))
doc.add_header("Testing Code", level=2)
doc.add_code("x = 5")
doc.add_header("Testing Quote", level=2)
doc.add_quote("How Now Brown Cow")
doc.output_page("")