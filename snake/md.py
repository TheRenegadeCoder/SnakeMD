from __future__ import annotations

import os
import pathlib
import random
import logging
from typing import Iterable, Union
from urllib import request
from urllib.error import HTTPError

logger = logging.getLogger(__name__)


class Verification():
    """
    Verification is a helper object for storing errors generated
    when creating a markdown document. This object is largely used
    internally to verify the contents of a document, but can be 
    accessed through the various verify() methods throughout the 
    library by the user. A convenience method is provided in Document 
    for listing all of the errors. Otherwise, a handful of methods
    are available here for interacting with the Verification object
    directly. 

    .. versionadded:: 0.2.0
    """

    def __init__(self) -> None:
        self._errors = list()

    def __str__(self) -> str:
        output = []
        for error in self._errors:
            output.append(
                f"- {type(error[0]).__name__}: {error[1]}\n{error[0]}\n")
        return "\n".join(output)

    def add_error(self, violator: object, error: str) -> None:
        """
        Documents a verification error.

        :param object violator: the object which produced the error
        :param str error: the error message detailing the error
        """
        self._errors.append((violator, error))
        logger.debug(f"Error logged: {self._errors[-1]}")

    def absorb(self, verification: Verification) -> None:
        """
        Absorbs an existing verification object in self. This is
        helpful when you have many verification objects that you'd
        like to aggregate. 

        :param Verification verification: the verification object to absorb
        """
        self._errors.extend(verification._errors)

    def passes_inspection(self) -> bool:
        """
        Assuming this object has already been used to verify something,
        this function will determine if that verificatioc succeeded.

        :return: True if there are no errors; False otherwise
        """
        return not bool(self._errors)


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

    def verify_url(self) -> bool:
        """
        Verifies that a URL is a valid URL.

        :return: True if the URL is valid; False otherwise
        """
        logger.info(f"Verifying URL: {self._url}")
        try:
            req = request.Request(self._url)
            req.get_method = lambda: 'HEAD'
            request.urlopen(req)
            return True
        except (HTTPError, ValueError):
            logger.exception(f"URL failed verification: {self._url}")
            return False

    def verify(self) -> Verification:
        """
        Verifies that the InlineText object is valid.

        .. versionadded:: 0.2.0

        :return: a verification object containing any errors that may have occured
        """
        verification = Verification()
        if self._url and not (self._url.startswith("#") or self.verify_url()):
            verification.add_error(self, "Invalid URL")
        if self._image and not self._url:
            verification.add_error(self, "Image requested without URL")
        return verification

    def is_text(self) -> bool:
        """
        Checks if this InlineText is a text-only element. If not, it must
        be an image, a URL, or an inline code snippet. 

        .. versionadded:: 0.2.0

        :return: True if this is a text-only element; False otherwise
        """
        return not (self._code or self._image or self._url)

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
        return self.render()

    def render(self) -> str:
        """
        Renders the element as a markdown string.
        This function is called by __str__ for all classes
        which inherit Element. 

        :raises NotImplementedError: interface method never to be implemented
        :return: the element as a markdown string
        """
        raise NotImplementedError()

    def verify(self) -> Verification:
        """
        Verifies that the element is valid markdown.

        :raises NotImplementedError: interface method never to be implemented
        :return: a verification object from the violator
        """
        raise NotImplementedError()


class HorizontalRule(Element):
    """
    A horizontal rule is a line separating different sections of
    a document. Horizontal rules really only come in one form,
    so there are no settings to adjust. 

    *New in version 0.2.0.*
    """

    def __init__(self):
        super().__init__()

    def render(self) -> str:
        """
        Renders the horizontal rule using the three dash syntax.

        .. versionadded:: 0.2.0

        :return: the horizontal rule as a markdown string
        """
        return "---"

    def verify(self) -> Verification:
        """
        Verifies the structure of the HorizontalRule element.
        Because there is no way to customize this object,
        it is always valid. Therefore, this method returns an
        empty Verification object.

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        return Verification()


class Header(Element):
    """
    A header is a text element which serves as the title for a new
    section of a document. Headers come in six main sizes which 
    correspond to the six headers sizes in HTML (e.g., <h1>).

    :param Union[InlineText, str] text: the header text
    :param int level: the header level between 1 and 6 (rounds to closest bound if out of range)
    """

    def __init__(self, text: Union[InlineText, str], level: int) -> None:
        super().__init__()
        self._text: InlineText = self._process_text(text)
        self._level: int = self._process_level(level)

    @staticmethod
    def _process_text(text) -> InlineText:
        """
        Ensures that Header objects are composed of a single InlineText object.

        :param text: an object to be forced to InlineText
        :return: the input text as an InlineText
        """
        if isinstance(text, str):
            return InlineText(text)
        return text

    @staticmethod
    def _process_level(level: int) -> int:
        """
        Restricts the range of possible levels to avoid issues with rendering.

        :param int level: the header level
        :return: the header level in the proper range
        """
        if level < 1:
            level = 1
        if level > 6:
            level = 6
        return level

    def render(self) -> str:
        """
        Renders the header in markdown according to
        the level provided. 

        :return: the header as a markdown string
        """
        return f"{'#' * self._level} {self._text}"

    def verify(self) -> Verification:
        """
        Verifies that the provided header is valid. This mainly
        returns errors associated with the InlineText element
        provided during instantiation.

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        return self._text.verify()

    def promote(self) -> None:
        """
        Promotes a header up a level. Fails silently
        if the header is already at the highest level (i.e., <h1>).
        """
        if self._level > 1:
            self._level -= 1

    def demote(self) -> None:
        """
        Demotes a header down a level. Fails silently if
        the header is already at the lowest level (i.e., <h6>).
        """
        if self._level < 6:
            self._level += 1


class Paragraph(Element):
    """
    A paragraph is a standalone element of text. Paragraphs can be
    formatted in a variety of ways including as code and blockquotes.

    .. versionchanged:: 0.4.0
        Expanded constructor to accept strings directly

    :param Iterable[Union[InlineText, str]] content: a "list" of text objects to render as a paragraph 
    :param bool code: the code state of the paragraph;
        set True to convert the paragraph to a code block (i.e., True -> ```code```)
    :param str lang: the language of the code snippet;
        invalid without the code flag set to True
    :param bool quote: the quote state of the paragraph;
        set True to convert the paragraph to a blockquote (i.e., True -> > quote)
    """

    def __init__(self, content: Iterable[Union[InlineText | str]], code: bool = False, lang: str = "generic", quote: bool = False):
        super().__init__()
        self._content: list[InlineText] = self._process_content(content)
        self._code = code
        self._lang = lang
        self._quote = quote
        self._backticks = 3

    @staticmethod
    def _process_content(content) -> None:
        processed = []
        for item in content:
            if isinstance(item, str):
                processed.append(InlineText(item))
            else:
                processed.append(item)
        return processed
            

    def render(self) -> str:
        """
        Renders the paragraph as markdown according to the settings provided.
        For example, if the code flag is enabled, the paragraph will be
        rendered as a code block. If both flags are enabled, code takes
        precedence. 

        .. versionchanged:: 0.4.0
            No longer assumes spaces between InlineText items

        :return: the paragraph as a markdown string
        """
        # TODO: add support for nested code blocks
        paragraph = ''.join(str(item) for item in self._content)
        if self._code:
            ticks = '`' * self._backticks
            return f"{ticks}{self._lang}\n{paragraph}\n{ticks}"
        elif self._quote:
            return f"> {paragraph}"
        else:
            return " ".join(paragraph.split())

    def verify(self) -> Verification:
        """
        Verifies that the Paragraph is valid. 

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        verification = Verification()

        # Paragraph errors
        if self._code and self._quote:
            verification.add_error(
                self, "Both code and quote are active. Choose one. ")

        # InlineText errors
        for text in self._content:
            verification.absorb(text.verify())

        return verification

    def add(self, text: Union[InlineText, str]) -> None:
        """
        Adds a text object to the paragraph.

        .. versionchanged:: 0.4.0
            Allows adding of strings directly

        :param text: a custom text element
        """
        if isinstance(text, str):
            text = InlineText(text)
        self._content.append(text)
    
    def is_text(self) -> bool:
        """
        Checks if this Paragraph is a text-only element. If not, it must
        be a quote or code block. 

        .. versionadded:: 0.3.0

        :return: True if this is a text-only element; False otherwise
        """
        return not (self._code or self._quote)

    def insert_link(self, target: str, url: str) -> Paragraph:
        """
        A convenience method which inserts a link in the paragraph
        at the first instance of a target string.

        .. versionadded:: 0.2.0

        :param str target: the string to link
        :param str url: the url to link
        :return: self
        """
        content = self._content[:]
        for i, inline_text in enumerate(content):
            if inline_text.is_text() and len(items := inline_text._text.split(target, 1)) > 1:
                self._content.pop(i)
                self._content.insert(i, InlineText(items[1]))
                self._content.insert(i, InlineText(target, url=url))
                self._content.insert(i, InlineText(items[0]))
                break
        return self


class MDList(Element):
    """
    A markdown list is a standalone list that comes in two varieties: ordered and unordered.

    :param items: a "list" of objects to be rendered as a list
    :param ordered: the ordered state of the list;
        set to True to render an ordered list (i.e., True -> 1. item)
    """

    def __init__(self, items: Iterable[Union[str, InlineText, Paragraph, MDList]], ordered: bool = False) -> None:
        super().__init__()
        self._items: Union[MDList, Paragraph] = self._process_items(items)
        self._ordered = ordered
        self._depth = 0

    @staticmethod
    def _process_items(items):
        """
        Given the variety of data that MDList can accept, this function
        forces all possible data types to be either MDLists or Paragraphs.

        :param items: a list of items
        :return: a list of paragraphs and MDLists
        """
        processed = []
        for item in items:
            if isinstance(item, (str, InlineText)):
                processed.append(Paragraph([item]))
            else:
                processed.append(item)
        return processed

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

    def verify(self) -> Verification:
        """
        Verifies that the markdown list is valid. Mainly, this checks the validity
        of the containing InlineText items. The MDList class has no way to
        instantiate it incorrectly, beyond providing the wrong data types. 
            
        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        verification = Verification()
        for item in self._items:
            verification.absorb(item.verify())
            if isinstance(item, Paragraph) and not item.is_text():
                verification.add_error(self, "Child paragraph is not text.")
        return verification


class TableOfContents(Element):
    """
    A Table of Contents is an element containing an ordered list
    of all the <h2> headers in the document. This element can be
    placed in the document. 

    .. versionadded:: 0.2.0

    :param Document doc: a reference to the document containing this table of contents 
    """

    def __init__(self, doc: Document):
        super().__init__()
        self._contents = doc._contents  # DO NOT MODIFY

    def render(self) -> str:
        """
        Renders the table of contents using the Document reference.

        :return: the table of contents as a markdown string
        """
        headers = (
            InlineText(
                header._text._text,
                url=f"#{'-'.join(header._text._text.lower().split())}"
            )
            for header in self._contents
            if isinstance(header, Header) and header._level == 2
        )
        return str(MDList(headers, ordered=True))

    def verify(self) -> Verification:
        """
        A Table of Contents is generated through a circular reference
        to the Document it contains. There is no way to instantiate 
        this incorrectly.

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        return Verification()


class Table(Element):
    """
    A table is a standalone element of rows and columns. Data is rendered
    according to underlying InlineText items. 

    :param header: the header row of labels
    :param body: the collection of rows of data
    """

    def __init__(self, header: Iterable[InlineText], body: Iterable[Iterable[InlineText]]) -> None:
        super().__init__()
        self._header = header
        self._body = body
        # TODO: add column align

    def render(self) -> str:
        """
        Renders a markdown table from a header "list"
        and a data set. 

        :return: a table as a markdown string
        """
        # TODO: make pretty print more robust
        rows = list()
        header = [str(item) for item in self._header]
        body = [
            [str(item).ljust(len(header[i])) for i, item in enumerate(row)]
            for row in self._body
        ]
        rows.append(' | '.join(header))
        rows.append(' | '.join("-" * len(item) for item in header))
        rows.extend(' | '.join(row) for row in body)
        return '\n'.join(rows)

    def verify(self):
        """
        Verifies the integrity of the markdown table. There are various ways
        a user could instantiate this object improperly. For example, they may
        provide a body with roes that are not all equal width. Likewise, the
        header may not match the width of the body. InlineText elements may also 
        be malformed. 

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        verification = Verification()

        # Table errors
        if len({len(row) for row in self._body}) != 1:
            verification.add_error(
                self, "Table body rows are not all the same width.")
        elif len(self._header) != len(self._body[0]):
            verification.add_error(self, "Header does not match width of body")

        # InlineText errors
        # TODO: pass information to verification that signals the location of each item
        # TODO: Mainly we just want more information to help the user debug
        for item in self._header:
            verification.absorb(item.verify())
        for row in self._body:
            for item in row:
                verification.absorb(item.verify())

        return verification


class Document:
    """
    A document represents a markdown file. Documents store
    a collection of elements which are appended with new lines
    between to generate the markdown document. Document methods
    are intended to provided convenience when generating a 
    markdown file. However, the functionality is not exhaustive.
    To get the full range of markdown functionality, you can
    take advantage of the :code:`add_element()` function to provide
    custom markdown elements. 

    :param name: the name of the document
    """

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._ext: str = ".md"
        self._contents: list[Element] = list()

    def __str__(self):
        return self.render()

    def render(self) -> str:
        """
        Renders the markdown document from a list of elements.

        :return: the document as a markdown string
        """
        return "\n\n".join(str(element) for element in self._contents)

    def check_for_errors(self) -> None:
        """
        A convenience method which can be used to verify the
        integrity of the document. Results will be printed to
        standard out.

        .. versionadded:: 0.2.0
        """
        verification = Verification()
        for element in self._contents:
            verification.absorb(element.verify())
        if verification.passes_inspection():
            print("No errors found!")
        else:
            print(verification)

    def add_element(self, element: Element) -> Element:
        """
        A generic function for appending elements to the document. 
        Use this function when you want a little more control over
        what the output looks like. 
        
        .. code-block:: Python

            doc.add_element(Header(InlineText("Python is Cool!"), 2))

        .. versionchanged:: 0.2.0
           Returns Element generated by this method instead of None. 

        :param Element element: a markdown object (e.g., Table, Header, etc.)
        :return: the Element added to this Document
        """
        assert isinstance(element, Element)
        self._contents.append(element)
        logger.debug(f"Added element to document\n{element}")
        return element

    def add_header(self, text: str, level: int = 1) -> Header:
        """ 
        A convenience method which adds a simple header to the document:

        .. code-block:: Python

            doc.add_header("Welcome to SnakeMD!")

        .. versionchanged:: 0.2.0
           Returns Header generated by this method instead of None. 

        :param str text: the text for the header
        :param int level: the level of the header from 1 to 6
        :return: the Header added to this Document
        """
        assert 1 <= level <= 6
        header = Header(InlineText(text), level)
        self._contents.append(header)
        logger.debug(f"Added header to document\n{header}")
        return header

    def add_paragraph(self, text: str) -> Paragraph:
        """
        A convenience method which adds a simple paragraph of text to the document:
        
        .. code-block:: Python

            doc.add_paragraph("Mitochondria is the powerhouse of the cell.")

        .. versionchanged:: 0.2.0
           Returns Paragraph generated by this method instead of None. 

        :param str text: any arbitrary text
        :return: the Paragraph added to this Document
        """
        paragraph = Paragraph([InlineText(text)])
        self._contents.append(paragraph)
        logger.debug(f"Added paragraph to document\n{paragraph}")
        return paragraph

    def add_ordered_list(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds a simple ordered list to the document: 

        .. code-block:: Python

            doc.add_ordered_list(["Goku", "Piccolo", "Vegeta"])

        .. versionchanged:: 0.2.0
           Returns MDList generated by this method instead of None. 

        :param Iterable[str] items: a "list" of strings
        :return: the MDList added to this Document
        """
        md_list = MDList([InlineText(item) for item in items], ordered=True)
        self._contents.append(md_list)
        logger.debug(f"Added ordered list to document\n{md_list}")
        return md_list

    def add_unordered_list(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds a simple unordered list to the document. 

        .. code-block:: Python

            doc.add_unordered_list(["Deku", "Bakugo", "Kirishima"])

        .. versionchanged:: 0.2.0
           Returns MDList generated by this method instead of None. 

        :param Iterable[str] items: a "list" of strings
        :return: the MDList added to this Document
        """
        md_list = MDList([InlineText(item) for item in items])
        self._contents.append(md_list)
        logger.debug(f"Added unordered list to document\n{md_list}")
        return md_list

    def add_table(self, header: Iterable[str], data: Iterable[Iterable[str]]) -> Table:
        """
        A convenience method which adds a simple table to the document:

        .. code-block:: Python

            doc.add_table(
                ["Place", "Name"],
                [
                    ["1st", "Robert"],
                    ["2nd", "Rae"]
                ]
            )

        .. versionchanged:: 0.2.0
           Returns Table generated by this method instead of None. 

        :param Iterable[str] header: a "list" of strings
        :param Iterable[Iterable[str]] data: a "list" of "lists" of strings
        :return: the Table added to this Document
        """
        header = [InlineText(text) for text in header]
        data = [[InlineText(item) for item in row] for row in data]
        table = Table(header, data)
        self._contents.append(table)
        logger.debug(f"Added table to document\n{table}")
        return table

    def add_code(self, code: str, lang: str = "generic") -> Paragraph:
        """
        A convenience method which adds a code block to the document:

        .. code-block:: Python

            doc.add_code("x = 5")

        .. versionchanged:: 0.2.0
           Returns Paragraph generated by this method instead of None.

        :param str code: a preformatted code string
        :param str lang: the language for syntax highlighting
        :return: the Paragraph added to this Document
        """
        code = Paragraph([InlineText(code)], code=True, lang=lang)
        self._contents.append(code)
        logger.debug(f"Added code block to document\n{code}")
        return code

    def add_quote(self, text: str) -> Paragraph:
        """
        A convenience method which adds a blockquote to the document:

        .. code-block:: Python

            doc.add_quote("Welcome to the Internet!")

        .. versionchanged:: 0.2.0
           Returns Paragraph generated by this method instead of None. 

        :param str text: the text to be quoted
        :return: the Paragraph added to this Document
        """
        paragraph = Paragraph([InlineText(text)], quote=True)
        self._contents.append(paragraph)
        logger.debug(f"Added code block to document\n{paragraph}")
        return paragraph

    def add_horizontal_rule(self) -> HorizontalRule:
        """
        A convenience method which adds a horizontal rule to the document:

        .. code-block:: Python

            doc.add_horizontal_rule()

        .. versionadded:: 0.2.0

        :return: the HorizontalRule added to this Document
        """
        hr = HorizontalRule()
        self._contents.append(hr)
        logger.debug(f"Added code block to document\n{hr}")
        return hr

    def add_table_of_contents(self) -> TableOfContents:
        """
        A convenience method which creates a table of contents. This function
        can be called where you want to add a table of contents to your
        document. The table itself is lazy loaded, so it always captures
        all of the header elements regardless of when the document is
        rendered. 

        .. code-block:: Python

            doc.add_table_of_contents()

        .. versionchanged:: 0.2.0
           Fixed a bug where table of contents could only be rendered once.

        :return: the TableOfContents added to this Document
        """
        toc = TableOfContents(self)
        self._contents.append(toc)
        logger.debug(f"Added code block to document (unable to render until file is complete)")
        return toc

    def scramble(self) -> None:
        """
        A silly method which mixes all of the elements in this document in 
        a random order.
        """
        random.shuffle(self._contents)
        logger.debug(f"Scrambled document")

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
        file_name = f"{separator.join(self._name.split())}{self._ext}"
        return file_name
