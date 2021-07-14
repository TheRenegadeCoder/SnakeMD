from markdown import Document, MDList, Paragraph, InlineText


doc = Document("README")
doc.add_header("All Features of PyMD")
doc.add_paragraph("I love to program code")
doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
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
doc.add_table([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
doc.add_header("Testing image", level=2)
doc.add_element(Paragraph([InlineText("Kitten", url="D:\OneDrive\E-Documents\Work\Employers\ME\The Renegade Coder\Assets\Logos\Icon\icon-360x360.png", image=True)]))
doc.add_header("Testing Links", level=2)
doc.add_element(Paragraph([InlineText("Doggo", url="google.com")]))
doc.add_header("Testing Code", level=2)
doc.add_code("x = 5")
doc.output_page("")