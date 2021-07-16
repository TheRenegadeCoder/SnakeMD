from __future__ import annotations
import os
import pathlib
from typing import Iterable, Union
from urllib.error import HTTPError
from urllib import request
import random


class InlineText:
    """
    The basic unit of text in markdown. All components which contain
    text are built using this class instead of strings directly. That
    way, those elements capture all styling information. 

    :param str text: the inline text to render
    :param str url: the link associated with the inline text
    :param bool bold: the bold state of the inline text; 
        set to True to render bold inline text (i.e., True -> **bold**)
    :param bool italics: the italics state of the inline text; 
        set to True to render inline text in italics (i.e., True -> *italics*)
    :param bool code: the italics state of the inline text;
        set to True to render inline text as code (i.e., True -> `code`)
    :param bool image: the image state of the inline text;
        set to True to render inline text as an image;
        must include url parameter to render
    """

    def __init__(
        self,
        text: str,
        url: str = None,
        bold: bool = False,
        italics: bool = False,
        code: bool = False,
        image: bool = False
    ) -> None:
        self._text = text
        self._bold = bold
        self._italics = italics
        self._url = url
        self._code = code
        self._image = image

    def __str__(self) -> str:
        return self.render()

    def render(self) -> str:
        """
        Renders self as a string. In this case,
        inline text can represent many different types of data from
        stylized text to inline code to links and images. 

        :return: the InlineText object as a string
        """
        text = self._text
        if self._bold:
            text = f"**{text}**"
        if self._italics:
            text = f"*{text}*"
        if self._url:
            text = f"[{text}]({self._url})"
        if self._url and self._image:
            text = f"!{text}"
        if self._code:
            text = f"`{text}`"
        return text

    def verify_link(self) -> bool:
        """
        Verifies that a URL is a valid URL.

        :return: True if the URL is valid; False otherwise
        """
        req = request.Request(self._url)
        req.get_method = lambda: 'HEAD'
        try:
            request.urlopen(req)
            return True
        except HTTPError:
            return False

    def verify(self) -> bool:
        if self._url:
            assert self._verify_link()

    def bold(self) -> None:
        """
        Adds bold styling to self. 
        """
        self._bold = True

    def unbold(self) -> None:
        """
        Removes bold styling from self. 
        """
        self._bold = False

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

    def render(self) -> str:
        """
        Renders the element as a markdown string.
        This function is to be called by `__str__()` of
        the child class. 

        :raises NotImplementedError: interface method never to be implemented
        :return: the element as a markdown string
        """
        raise NotImplementedError()

    def verify(self) -> list[str]:
        """
        Verifies that the element is valid markdown.

        :raises NotImplementedError: interface method never to be implemented
        :return: a series of errors in the current element
        """
        raise NotImplementedError()


class Header(Element):
    """
    A header is a text element which serves as the title for a new
    section of a document. Headers come in six main sizes which 
    correspond to the six headers sizes in HTML (e.g., <h1>).

    :param InlineText text: the header text
    :param int level: the header level between 1 and 6
    """

    def __init__(self, text: InlineText, level: int) -> None:
        super().__init__()
        self.text: InlineText = text
        self.level: int = level

    def __str__(self) -> str:
        return self.render()

    def render(self) -> str:
        """
        Renders the header in markdown according to
        the level provided. 

        :return: the header as a markdown string
        """
        return f"{'#' * self.level} {self.text}"

    def promote(self) -> None:
        """
        Promotes a header up a level. Fails silently
        if the header is already at the highest level (i.e., <h1>).
        """
        if self.level > 1:
            self.level -= 1

    def demote(self) -> None:
        """
        Demotes a header down a level. Fails silently if
        the header is already at the lowest level (i.e., <h6>).
        """
        if self.level < 6:
            self.level += 1


class Paragraph(Element):
    """
    A paragraph is a standalone element of text. Paragraphs can be
    formatted in a variety of ways including as code and blockquotes.

    :param Iterable[InlineText] content: a "list" of text objects to render as a paragraph 
    :param bool code: the code state of the paragraph;
        set True to convert the paragraph to a code block (i.e., True -> ```code```)
    :param str lang: the language of the code snippet;
        invalid without the code flag set to True
    :param bool quote: the quote state of the paragraph;
        set True to convert the paragraph to a blockquote (i.e., True -> > quote)
    """

    def __init__(self, content: Iterable[InlineText], code: bool = False, lang: str = "generic", quote: bool = False):
        super().__init__()
        self._content = content
        self._code = code
        self._lang = lang
        self._quote = quote
        self._backticks = 3

    def __str__(self) -> str:
        return self.render()

    def render(self) -> str:
        """
        Renders the paragraph as markdown according to the settings provided.
        For example, if the code flag is enabled, the paragraph will be
        rendered as a code block. 

        :return: the paragraph as a markdown string
        """
        # TODO: add support for nested code blocks
        paragraph = ' '.join(str(item) for item in self._content)
        if self._code:
            ticks = '`' * self._backticks
            return f"{ticks}{self._lang}\n{paragraph}\n{ticks}"
        elif self._quote:
            return f"> {paragraph}"
        else:
            return " ".join(paragraph.split())

    def add(self, text: InlineText) -> None:
        """
        Adds a text object to the paragraph.

        :param text: a custom text element
        """
        self._content.append(text)


class MDList(Element):
    """
    A markdown list is a standalone list that comes in two varieties: ordered and unordered.

    :param items: a "list" of objects to be rendered as a list
    :param ordered: the ordered state of the list;
        set to True to render an ordered list (i.e., True -> 1. item)
    """

    def __init__(self, items: Iterable[Union[InlineText, MDList]], ordered: bool = False) -> None:
        super().__init__()
        self._items: Iterable = items
        self._ordered = ordered
        self._depth = 0

    def __str__(self) -> str:
        return self.render()

    def render(self) -> str:
        """
        Renders the markdown list according to the settings provided.
        For example, if the the ordered flag is set, an ordered list
        will be rendered in markdown. 

        :return: the list as a markdown string
        """
        output = list()
        i = 1
        for item in self._items:
            if isinstance(item, MDList):
                item._depth = self._depth + 1
                output.append(str(item))
            else:
                if self._ordered:
                    output.append(f"{'  ' * self._depth}{i}. {item}")
                else:
                    output.append(f"{'  ' * self._depth}- {item}")
            i += 1
        return "\n".join(output)


class Table(Element):
    """
    A table is a standalone element of rows and columns. Data is rendered
    according to underlying InlineText items. 

    :param header: the header row of labels
    :param body: the collection of rows of data
    """

    def __init__(self, header: Iterable[InlineText], body: Iterable[Iterable[InlineText]]) -> None:
        super().__init__()
        self.header = header
        self.body = body
        # TODO: add column align

    def __str__(self) -> str:
        return self.render()

    def render(self) -> str:
        """
        Renders a markdown table from a header "list"
        and a data set. 

        :return: a table as a markdown string
        """
        # TODO: make pretty print more robust
        rows = list()
        header = [str(item) for item in self.header]
        body = [
            [str(item).ljust(len(header[i])) for i, item in enumerate(row)]
            for row in self.body
        ]
        rows.append(' | '.join(header))
        rows.append(' | '.join("-" * len(item) for item in header))
        rows.extend(' | '.join(row) for row in body)
        return '\n'.join(rows)

    def verify(self):
        assert len({len(i) for i in self.body}) == 1
        assert len(self.header) == len(self.footer) == len(self.body[0])


class Document:
    """
    A document represents a markdown file. Documents store
    a collection of elements which are appended with new lines
    between to generate the markdown document. Document methods
    are intended to provided convenience when generating a 
    markdown file. However, the functionality is not exhaustive.
    To get the full range of markdown functionality, you can
    take advantage of the `add_element()` function to provide
    custom markdown elements. 

    :param name: the name of the document
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ext: str = ".md"
        self.contents: list[Element] = list()

    def __str__(self):
        return self.render()

    def render(self) -> str:
        """
        Renders the markdown document from a list of elements.

        :return: the document as a markdown string
        """
        return "\n\n".join(str(element) for element in self.contents)

    def add_element(self, element: Element) -> None:
        """
        A generic function for appending elements to the document. 
        Use this function when you want a little more control over
        what the output looks like. 

        :param Element element: a markdown object (e.g., Table, Header, etc.)
        """
        assert isinstance(element, Element)
        self.contents.append(element)

    def add_header(self, text: str, level: int = 1) -> None:
        """ 
        A convenience method which adds a simple header to the document.

        :param str text: the text for the header
        :param int level: the level of the header from 1 to 6
        """
        assert 1 <= level <= 6
        self.contents.append(Header(InlineText(text), level))

    def add_paragraph(self, text: str) -> None:
        """
        A convenience method which adds a simple paragraph of text to the document.

        :param str text: any arbitrary text
        """
        self.contents.append(Paragraph([InlineText(text)]))

    def add_ordered_list(self, items: Iterable[str]) -> None:
        """
        A convenience method which adds a simple ordered list to the document. 

        :param Iterable[str] items: a "list" of strings
        """
        self.contents.append(MDList(
            [InlineText(item) for item in items],
            ordered=True
        ))

    def add_unordered_list(self, items: Iterable[str]) -> None:
        """
        A convenience method which adds a simple unordered list to the document. 

        :param Iterable[str] items: a "list" of strings
        """
        self.contents.append(MDList([InlineText(item) for item in items]))

    def add_table(self, header: Iterable[str], data: Iterable[Iterable[str]]) -> None:
        """
        A convenience method which adds a simple table to the document.

        :param Iterable[str] header: a "list" of strings
        :param Iterable[Iterable[str]] data: a "list" of "lists" of strings
        """
        header = [InlineText(text) for text in header]
        data = [[InlineText(item) for item in row] for row in data]
        self.contents.append(Table(header, data))

    def add_code(self, code: str, lang: str = "generic") -> None:
        """
        A convenience method which adds a code block to the document.

        :param str code: a preformatted code string
        :param str lang: the language for syntax highlighting
        """
        self.contents.append(
            Paragraph([InlineText(code)], code=True, lang=lang))

    def add_quote(self, text: str) -> None:
        """
        A convenience method which adds a blockquote to the document.

        :param str text: the text to be quoted
        """
        self.contents.append(Paragraph([InlineText(text)], quote=True))

    def add_table_of_contents(self) -> None:
        """
        A convenience method which creates a table of contents. This function
        can be called where you want to add a table of contents to your
        document. However, be aware that the table of contents uses lazy 
        loading, so it can only be rendered once. 
        """
        headers = (
            InlineText(header.text.text,
                       url=f"#{'-'.join(header.text.text.lower().split())}")
            for header in self.contents
            if isinstance(header, Header) and header.level == 2
        )
        self.contents.append(MDList(headers, ordered=True))

    def scramble(self) -> None:
        """
        A silly method which mixes all of the elements in this document in 
        a random order.
        """
        random.shuffle(self.contents)

    def output_page(self, dump_dir: str = "") -> None:
        """
        Generates the markdown file.

        :param str dump_dir: the path to where you want to dump the file
        """
        pathlib.Path(dump_dir).mkdir(parents=True, exist_ok=True)
        output_file = open(os.path.join(dump_dir, self._get_file_name()), "w+")
        output_file.write(str(self))
        output_file.close()

    def _get_file_name(self) -> str:
        """
        A helper function for generating the file name.
        """
        separator = "-"
        file_name = f"{separator.join(self.name.split())}{self.ext}"
        return file_name
