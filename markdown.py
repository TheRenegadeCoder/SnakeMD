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

    def __init__(self, text, style=None, url=None) -> None:
        self.text = text
        self.style = style
        self.url = url

    def __str__(self) -> str:
        text = self.text
        if self.style == "bold":
            text = f"**{self.text}**"
        elif self.style == "italics":
            text = f"*{self.text}*"
        if self.url:
            text = f"[{text}]({self.url})"
        return text

    def verify_link(self) -> bool:
        """
        Verifies that a URL is a valid URL.
        :return: True if the URL is valid; False otherwise
        """
        req = request.Request(self.url)
        req.get_method = lambda: 'HEAD'
        print(f"Trying: {self.url}")
        try:
            request.urlopen(req)
            print(f"\tVALID")
            return True
        except HTTPError:
            print(f"\tINVALID")
            return False

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

    def __str__(self) -> str:
        if self.ordered:
            return "\n".join([f"{index + 1}. {item}" for index, item in enumerate(self.items)])
        else:
            return "\n".join([f"- {item}" for item in self.items])


class Table:
    def __init__(self, header: Iterable[Text], body: Iterable[Iterable[Text]], footer: Iterable[Text]) -> None:
        self.header = header
        self.body = body
        self.footer = footer

    def __str__(self) -> str:
        rows = list()
        rows.append(self.header)
        rows.extend(self.body)
        rows.append(self.footer)
        return f"{' | '.join(rows)}"

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
doc.add_header("Test")
doc.add_paragraph("I love to program code")
doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
doc.add_unordered_list(["Look", "at", "Me", "Now"])
doc.output_page("test")
