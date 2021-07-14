from __future__ import annotations
import os
import pathlib
from typing import Iterable, Union
from urllib.error import HTTPError
from urllib import request



class Text:
    """
    The basic unit of text in markdown. All components which contain
    text are built using this class instead of strings directly. That
    way, those elements capture all styling information. 
    """

    def __init__(self, text, style=None, url=None, code=False, image=False) -> None:
        self.text = text
        self.style = style
        self.url = url
        self.code = code
        self.image = image

    def __str__(self) -> str:
        text = self.text
        if self.style == "bold":
            text = f"**{self.text}**"
        elif self.style == "italics":
            text = f"*{self.text}*"
        if self.url:
            text = f"[{text}]({self.url})"
        if self.image:
            text = f"!{text}"
        if self.code:
            text = f"`{text}`"
        return text

    def _verify_link(self) -> bool:
        """
        Verifies that a URL is a valid URL.
        :return: True if the URL is valid; False otherwise
        """
        req = request.Request(self.url)
        req.get_method = lambda: 'HEAD'
        try:
            request.urlopen(req)
            return True
        except HTTPError:
            return False

    def verify(self) -> bool:
        if self.url:
            assert self._verify_link()

    # TODO: add text processing to avoid issues where asterisks mess up formatting
    # One way to do this would be to backslash special characters in the raw text


class Element:
    """
    An element is defined as a standalone section of a markdown file. 
    All elements are to be surrounded by empty lines. Examples of elements
    include paragraphs, headers, tables, and lists. 
    """

    def __init__(self):
        pass

    def __str__(self) -> str:
        raise NotImplementedError()


class Header(Element):
    def __init__(self, text: Text, level: int) -> None:
        super().__init__()
        self.text: Text = text
        self.level: int = level

    def __str__(self) -> str:
        return f"{'#' * self.level} {self.text}"

    def promote(self):
        if self.level > 1:
            self.level -= 1

    def demote(self):
        if self.level < 6:
            self.level += 1


class Paragraph(Element):
    def __init__(self, content: Iterable[Text]):
        super().__init__()
        self.content = content

    def __str__(self) -> str:
        return " ".join(str(item) for item in self.content)

    def add(self, text: Text):
        self.content.append(text)


class MDList(Element):
    def __init__(self, items: Iterable[Union[Text, MDList]], ordered: bool = False) -> None:
        super().__init__()
        self.items: Iterable = items
        self.ordered = ordered
        self.depth = 0

    def __str__(self) -> str:
        output = list()
        i = 1
        for item in self.items:
            if isinstance(item, MDList):
                item.depth = self.depth + 1
                output.append(str(item))
            else:
                if self.ordered:
                    output.append(f"{'  ' * self.depth}{i}. {item}")
                else:
                    output.append(f"{'  ' * self.depth}- {item}")
            i += 1
        return "\n".join(output)


class Table(Element):
    def __init__(self, header: Iterable[Text], body: Iterable[Iterable[Text]], footer: Iterable[Text]) -> None:
        super().__init__()
        self.header = header
        self.body = body
        self.footer = footer

    def __str__(self) -> str:
        rows = list()
        if self.header:
            rows.append(' | '.join(self.header))
            rows.append(' | '.join("-" for _ in self.header))
        rows.extend(' | '.join(row) for row in self.body)
        if self.footer:
            rows.append(' | '.join("-" for _ in self.footer))
            rows.append(' | '.join(self.footer))
        return '\n'.join(rows)

    def verify(self):
        assert len({len(i) for i in self.body}) == 1
        assert len(self.header) == len(self.footer) == len(self.body[0])


class Document:

    def __init__(self, name: str) -> None:
        self.name = name
        self.ext = ".md"
        self.contents = list()

    def __str__(self):
        return f"{self.name}\n{self._build_page()}"

    def add_element(self, element: Element):
        """
        A generic function for appending elements to the document. 
        Use this function when you want a little more control over
        what the output looks like. 

        :param element: a markdown object (e.g., Table, Header, etc.)
        """
        assert isinstance(element, Element)
        self.contents.append(element)

    def add_header(self, text: str, level: int = 1):
        """
        A convenience method which adds a simple header to the document.

        :param text: the text for the header
        :param level: the level of the header from 1 to 6
        """
        assert 1 <= level <= 6
        self.contents.append(Header(Text(text), level))

    def add_paragraph(self, text: str):
        """
        A convenience method which adds a simple paragraph of text to the document.

        :param text: any arbitrary text
        """
        self.contents.append(Paragraph([Text(text)]))

    def add_ordered_list(self, items: Iterable[str]):
        """
        A convenience method which adds a simple ordered list to the document. 

        :param items: a "list" of strings
        """
        self.contents.append(MDList((Text(item) for item in items), ordered=True))

    def add_unordered_list(self, items: Iterable[str]):
        """
        A convenience method which adds a simple unordered list to the document. 

        :param items: a "list" of strings
        """
        self.contents.append(MDList(Text(item) for item in items))

    def add_table(self, grid: Iterable[Iterable[str]], _header: bool = True, _footer: bool = False):
        head = None
        foot = None
        bounds = [None, None]

        if _header:
            head = grid[0]
            bounds[0] = 1
        if _footer:
            foot = grid[-1]
            bounds[1] = -1

        body = grid[slice(*bounds)]

        self.contents.append(Table(head, body, foot))
            

    def output_page(self, dump_dir):
        pathlib.Path(dump_dir).mkdir(parents=True, exist_ok=True)
        output_file = open(os.path.join(dump_dir, self._get_file_name()), "w+")
        output_file.write(self._build_page())
        output_file.close()

    def _build_page(self):
        return "\n\n".join(str(element) for element in self.contents)

    def _get_file_name(self):
        separator = "-"
        file_name = f"{separator.join(self.name.split())}{self.ext}"
        return file_name

doc = Document("Test")
doc.add_header("All Features of PyMD")
doc.add_paragraph("I love to program code")
doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
doc.add_unordered_list(["Look", "at", "Me", "Now"])
doc.add_header("Testing nesting", level=2)
doc.add_element(
    MDList([
        Text("Outer"), 
        Text("List"),
        MDList([
            Text("Inner"),
            Text("List")
        ]),
        Text("!!!")
    ])
)
doc.add_table([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
doc.add_header("Testing image", level=2)
doc.add_element(Paragraph([Text("Kitten", url="D:\OneDrive\E-Documents\Work\Employers\ME\The Renegade Coder\Assets\Logos\Icon\icon-360x360.png", image=True)]))
doc.add_header("Testing Links", level=2)
doc.add_element(Paragraph([Text("Doggo", url="google.com")]))
doc.output_page("test")
