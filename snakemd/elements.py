from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Iterable

logger = logging.getLogger(__name__)


class Element(ABC):
    """
    A generic element interface which provides a framework for all
    types of elements in the collection. In short, elements must
    be able to be converted to their markdown representation using
    the built-in :py:class:`str` constructor. 
    """

    @abstractmethod
    def __str__(self) -> str:
        pass


class Inline(Element):
    """
    The basic unit of text in markdown. All components which contain
    text are built using this class instead of strings directly. That
    way, those elements capture all styling information.

    Inline element parameters are in order of precedence. In other words,
    image markdown is applied to the text first while code markdown is
    applied last. Due to this design, some forms of inline text are not
    possible. For example, inline elements can be used to show inline 
    markdown as an inline code element (e.g., :code:`![here](https://example.com)`).
    However, inline elements cannot be used to style inline code (e.g., :code:`**`code`**`).
    If styled code is necessary, it's possible to render the inline element
    as a string and pass the result to another inline element. 

    .. testsetup:: inline
    
        from snakemd import Inline

    :param str text: 
        the inline text to render
    :param None | str image: 
        the source (either url or path) associated with an image
        
        - defaults to :code:`None`
        - set to a string representing a URL or path to render an image (i.e., :code:`![text](image)`)
    :param None | str link: 
        the link (either url or path) associated with the inline element
        
        - defaults to :code:`None`
        - set to a string representing a URL or path to render a link (i.e., :code:`[text](link)`)
    :param bool bold: 
        the bold state of the inline text
        
        - defaults to :code:`False`
        - set to :code:`True` to render bold text (i.e., :code:`**text**`)
    :param bool italics: 
        the italics state of the inline element
        
        - defaults to :code:`False`
        - set to :code:`True` to render text in italics (i.e., :code:`_text_`)
    :param bool strikethrough: 
        the strikethrough state of the inline text
        
        - defaults to :code:`False`
        - set to :code:`True` to render text with a strikethrough 
          (i.e., :code:`~~text~~`)
    :param bool code: 
        the code state of the inline text
        
        - defaults to :code:`False`
        - set to :code:`True` to render text as code (i.e., :code:`\`text\``)
    """

    def __init__(
        self,
        text: str,
        image: None | str = None,
        link: None | str = None,
        bold: bool = False,
        italics: bool = False,
        strikethrough: bool = False,
        code: bool = False
    ) -> None:
        self._text = text
        self._image = image
        self._link = link
        self._bold = bold
        self._italics = italics
        self._strikethrough = strikethrough
        self._code = code

    def __str__(self) -> str:
        """
        Renders self as a string. In this case,
        inline can represent many different types of data from
        stylized text to code, links, and images.
        
        .. doctest:: inline

            >>> inline = Inline("This is formatted text", bold=True, italics=True)
            >>> str(inline)
            '_**This is formatted text**_'

        :return: 
            the Inline object as a string
        """
        text = self._text
        if self._image:
            text = f"![{text}]({self._image})"
        if self._link:
            text = f"[{text}]({self._link})"
        if self._bold:
            text = f"**{text}**"
        if self._italics:
            text = f"_{text}_"
        if self._strikethrough:
            text = f"~~{text}~~"
        if self._code:
            text = f"`{text}`"
        logger.debug(f"Rendered inline text: {text}")
        return text

    def is_text(self) -> bool:
        """
        Checks if this Inline element is a text-only element. If not, it must
        be an image, a link, or a code snippet.

        .. doctest:: inline

            >>> inline = Inline("This is text")
            >>> inline.is_text()
            True

        :return: 
            True if this is a text-only element; False otherwise
        """
        return not (self._code or self._image or self._link)

    def is_link(self) -> bool:
        """
        Checks if the Inline object represents a link.

        .. doctest:: inline

            >>> inline = Inline("This is not a link")
            >>> inline.is_link()
            False

        :return: 
            True if the object has a link; False otherwise
        """
        return bool(self._link)

    def bold(self) -> Inline:
        """
        Adds bold styling to self.

        .. doctest:: inline

            >>> inline = Inline("This is bold text").bold()
            >>> str(inline)
            '**This is bold text**'

        :return: 
            self
        """
        self._bold = True
        return self

    def unbold(self) -> Inline:
        """
        Removes bold styling from self.

        .. doctest:: inline

            >>> inline = Inline("This is normal text", bold=True).unbold()
            >>> str(inline)
            'This is normal text'

        :return: 
            self
        """
        self._bold = False
        return self

    def italicize(self) -> Inline:
        """
        Adds italics styling to self.

        .. doctest:: inline

            >>> inline = Inline("This is italicized text").italicize()
            >>> str(inline)
            '_This is italicized text_'

        :return: 
            self
        """
        self._italics = True
        return self

    def unitalicize(self) -> Inline:
        """
        Removes italics styling from self.

        .. doctest:: inline

            >>> inline = Inline("This is normal text", italics=True).unitalicize()
            >>> str(inline)
            'This is normal text'

        :return: 
            self
        """
        self._italics = False
        return self

    def strikethrough(self) -> Inline:
        """
        Adds strikethrough styling to self.

        .. doctest:: inline

            >>> inline = Inline("This is striked text").strikethrough()
            >>> str(inline)
            '~~This is striked text~~'

        :return: 
            self
        """
        self._strikethrough = True
        return self

    def unstrikethrough(self) -> Inline:
        """
        Remove strikethrough styling from self.

        .. doctest:: inline

            >>> inline = Inline("This is normal text", strikethrough=True).unstrikethrough()
            >>> str(inline)
            'This is normal text'

        :return: 
            self
        """
        self._strikethrough = False
        return self

    def code(self) -> Inline:
        """
        Adds code style to self.

        .. doctest:: inline

            >>> inline = Inline("x = 5").code()
            >>> str(inline)
            '`x = 5`'

        :return: 
            self
        """
        self._code = True
        return self

    def uncode(self) -> Inline:
        """
        Removes code styling from self.

        .. doctest:: inline

            >>> inline = Inline("This is normal text", code=True).uncode()
            >>> str(inline)
            'This is normal text'

        :return: 
            self
        """
        self._code = False
        return self

    def link(self, link: str) -> Inline:
        """
        Adds link to self.

        .. doctest:: inline

            >>> inline = Inline("here").link("https://snakemd.io")
            >>> str(inline)
            '[here](https://snakemd.io)'

        :param str link: 
            the URL or path to apply to this Inline element
        :return: 
            self
        """
        self._link = link
        return self

    def unlink(self) -> Inline:
        """
        Removes link from self.

        .. doctest:: inline

            >>> inline = Inline("This is normal text", link="https://snakemd.io").unlink()
            >>> str(inline)
            'This is normal text'

        :return: 
            self
        """
        self._link = None
        return self

    def reset(self) -> Inline:
        """
        Removes all settings from self (e.g., bold, code, italics, url, etc.).
        All that will remain is the text itself.

        .. doctest:: inline

            >>> inline = Inline("This is normal text", link="https://snakemd.io", bold=True).reset()
            >>> str(inline)
            'This is normal text'

        :return: 
            self
        """
        self._image = None
        self._link = None
        self._code = False
        self._italics = False
        self._bold = False
        self._strikethrough = False
        return self


class Block(Element):
    """
    A block element in Markdown. A block is defined as a standalone 
    element starting on a newline. Examples of blocks include paragraphs 
    (i.e., :code:`<p>`), headings (e.g., :code:`<h1>`, :code:`<h2>`, etc.), 
    tables (i.e., :code:`<table>`), and lists (e.g., :code:`<ol>`, :code:`<ul>`, etc.).
    """
    pass


class Code(Block):
    """
    A code block is a standalone block of syntax-highlighted code.
    Code blocks can have generic highlighting or highlighting based
    on their language. 
    """

    def __init__(self, code: str | Code, lang: str = "generic"):
        super().__init__()
        self._code = code
        self._lang = lang
        self._backticks = self._process_backticks(code)
        
    def __str__(self) -> str:
        """
        Renders the code block as a markdown string. Markdown code
        blocks are returned with the fenced code block
        format using backticks:
        
        .. code-block:: markdown
        
            ```python
            x = 5
            y = 2 + x
            ```
            
        Code blocks can be nested and will be rendered with
        increasing numbers of backticks.

        :return: 
            the code block as a markdown string
        """
        ticks = '`' * self._backticks
        return f"{ticks}{self._lang}\n{self._code}\n{ticks}"
    
    @staticmethod
    def _process_backticks(code: str | Code) -> int:
        """
        A helper method which processes the potential hierarchy
        that exists for code.

        :param code: code to render
        :return: the number of appropriate backticks for this code block
        """
        if isinstance(code, Code):
            return code._backticks + 1
        else:
            return 3
    
    
class Heading(Block):
    """
    A heading is a text block which serves as the title for a new
    section of a document. Headings come in six main sizes which
    correspond to the six headings sizes in HTML (e.g., :code:`<h1>`).
    
    .. testsetup:: heading
    
        from snakemd import Heading

    :raises ValueError: 
        when level < 1 or level > 6
    :param str | Inline | Iterable[Inline | str] text: 
        the heading text
    :param int level: 
        the heading level between 1 and 6
    """

    def __init__(self, text: str | Inline | Iterable[Inline | str], level: int) -> None:
        if level < 1 or level > 6:
            raise ValueError(
                f"Heading level must be between 1 and 6 but was {level}"
            )
        super().__init__()
        self._text: list[Inline] = self._process_text(text)
        self._level: int = level

    def __str__(self) -> str:
        """
        Renders the heading as a markdown string. Markdown headings
        are returned using the :code:`#` syntax where the number of
        :code:`#` symbols corresponds to the heading level:
        
        .. code-block:: markdown
        
            # This is an H1
            ## This is an H2
            ### This is an H3

        :return: 
            the heading as a markdown string
        """
        heading = [str(item) for item in self._text]
        return f"{'#' * self._level} {''.join(heading)}"

    @staticmethod
    def _process_text(text: str | Inline | Iterable[Inline | str]) -> list[Inline]:
        """
        Ensures that Heading objects are composed of a single Inline object.

        :param str | Inline | Iterable[Inline | str] text: 
            an object to be forced to Inline
        :return: 
            the input text as an Inline
        """
        logger.debug(f"Processing heading text: {text}")
        if isinstance(text, str):
            return [Inline(text)]
        elif isinstance(text, Inline):
            return [text]
        else:
            return [
                item if isinstance(item, Inline) else Inline(item)
                for item in text
            ]

    def promote(self) -> Heading:
        """
        Promotes a heading up a level. Fails silently
        if the heading is already at the highest level (i.e., :code:`<h1>`).
        
        .. doctest:: heading

            >>> heading = Heading("This is an H2 heading", 3).promote()
            >>> str(heading)
            '## This is an H2 heading'
            
        :return:
            self
        """
        if self._level > 1:
            self._level -= 1
        return self

    def demote(self) -> Heading:
        """
        Demotes a heading down a level. Fails silently if
        the heading is already at the lowest level (i.e., :code:`<h6>`).

        .. doctest:: heading

            >>> heading = Heading("This is an H2 heading", 1).demote()
            >>> str(heading)
            '## This is an H2 heading'
            
        :return:
            self
        """
        if self._level < 6:
            self._level += 1
        return self

    def get_text(self) -> str:
        """
        Returns the heading text free of any styling. Useful
        when the heading is composed of various Inline elements,
        and the raw text is needed without styling or linking.

        .. doctest:: heading

            >>> heading = Heading("This is the heading text", 1)
            >>> heading.get_text()
            'This is the heading text'

        :return: 
            the heading as a string
        """
        text_elements = [item._text for item in self._text]
        return ''.join(text_elements)


class HorizontalRule(Block):
    """
    A horizontal rule is a line separating different sections of
    a document. Horizontal rules only come in one form,
    so there are no settings to adjust.
    """

    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        """
        Renders the horizontal rule as a markdown string. Markdown
        horizontal rules come in a variety of flavors, but the
        format used in this repo is the triple asterisk 
        (i.e., :code:`***`) to avoid clashes with list formatting.

        :return: 
            the horizontal rule as a markdown string
        """
        return "***"
    
    
class MDList(Block):
    """
    A markdown list is a standalone list that comes in three varieties: ordered, unordered, and checked.

    :raises ValueError: 
        when the checked parameter is provided an Iterable[bool] that does not 
        match the number of top-level elements in the list
    :param Iterable[str | Inline | Block] items:
        a "list" of objects to be rendered as a list
    :param bool ordered: 
        the ordered state of the list
        
        - defaults to :code:`False` which renders an unordered list (i.e., :code:`-`)
        - set to :code:`True` to render an ordered list (i.e., :code:`1.`)
    :param None | bool | Iterable[bool] checked: 
        the checked state of the list
        
        - defaults to :code:`None` which excludes checkboxes from being rendered
        - set to :code:`False` for a series of unchecked boxes (i.e., :code:`- [ ]`)
        - set to :code:`True` for a series of checked boxes (i.e., :code:`- [x]`)
        - set to :code:`Iterable[bool]` to configure the checked 
          status of the top-level list elements directly
    """

    def __init__(
        self,
        items: Iterable[str | Inline | Block],
        ordered: bool = False,
        checked: None | bool | Iterable[bool] = None
    ) -> None:
        super().__init__()
        self._items: list[Block] = self._process_items(items)
        self._ordered: bool = ordered
        self._checked: bool | list[bool] = checked \
            if checked is None or isinstance(checked, bool) \
            else [_ for _ in checked]
        self._space = ""
        if isinstance(self._checked, list) and self._top_level_count() != len(self._checked):
            raise ValueError(
                f"Number of top-level elements in checklist does not match number of booleans supplied by checked parameter: {self._checked}"
            )

    def __str__(self) -> str:
        """
        Renders the markdown list as a markdown string. Markdown lists
        come in a variety of flavors and are customized according to 
        the settings provided. For example, if the the ordered flag is 
        set, an ordered list will be rendered in markdown. Unordered
        lists and checklists both use the hyphen syntax for markdown
        (i.e., :code:`-`) to avoid clashes with horizontal rules: 
        
        .. code-block:: markdown
        
            - This is an unordered list item
            - So, is this
        
        Ordered lists use numbers for each list item:
        
        .. code-block:: markdown
        
            1. This is an ordered list item
            2. So, is this

        :return: 
            the list as a markdown string
        """
        output = list()
        i = 1
        for item in self._items:
            if isinstance(item, MDList):
                item._space = self._space + " " * self._get_indent_size(i)
                output.append(str(item))
            else:
                # Create the start of the row based on `order` parameter
                if self._ordered:
                    row = f"{self._space}{i}."
                else:
                    row = f"{self._space}-"

                # Add checkbox based on `checked` parameter
                if isinstance(self._checked, bool):
                    checked_str = "X" if self._checked else " "
                    row = f"{row} [{checked_str}] {item}"
                elif self._checked is not None:
                    checked_str = "X" if self._checked[i - 1] else " "
                    row = f"{row} [{checked_str}] {item}"
                else:
                    row = f"{row} {item}"

                output.append(row)
                i += 1
        return "\n".join(output)

    @staticmethod
    def _process_items(items) -> list[Block]:
        """
        Given the variety of data that MDList can accept, this function
        forces all possible data types to be Blocks.

        :param items: 
            a list of items
        :return: 
            a list of Blocks
        """
        processed = []
        for item in items:
            if isinstance(item, (str, Inline)):
                processed.append(Paragraph([item]))
            else:
                processed.append(item)
        return processed
    
    def _top_level_count(self) -> int:
        """
        Given that MDList can accept a variety of blocks,
        we need to know how many items in the provided list
        are top-level elements (i.e., not nested list elements).
        We use this number to throw errors if this count does
        not match up with the checklist count.

        :return: 
            a count of top-level elements
        """
        count = 0
        for item in self._items:
            if not isinstance(item, MDList):
                count += 1
        return count

    def _get_indent_size(self, item_index: int = -1) -> int:
        """
        Returns the number of spaces that any sublists should be indented.

        :param int item_index: 
            the index of the item to check (only used for ordered lists);
            defaults to -1
        :return: 
            the number of spaces
        """
        if not self._ordered:
            return 2
        else:
            # Ordered items vary in length, so we adjust the result based on the index
            return 2 + len(str(item_index))


class Paragraph(Block):
    """
    A paragraph is a standalone block of text. 
    
    .. testsetup:: paragraph
    
        from snakemd import Paragraph

    :param str | Iterable[Inline | str] content: 
        a single string or a "list" of text objects to render as a paragraph        
    """

    def __init__(self, content: str | Iterable[Inline | str]):
        super().__init__()
        self._content: list[Inline] = self._process_content(content)

    @staticmethod
    def _process_content(content) -> list[Inline]:
        """
        Processes the incoming content for the Paragraph.

        :param content: 
            an iterable of various text items
        :return: 
            the processed iterable as a list of Inline items
        """
        logger.debug(f"Processing paragraph content: {content}")
        if isinstance(content, str):
            processed = [Inline(content)]
        else:
            processed = []
            for item in content:
                if isinstance(item, str):
                    processed.append(Inline(item))
                else:
                    processed.append(item)
        return processed

    def __str__(self) -> str:
        """
        Renders the paragraph as a markdown string. Markdown paragraphs
        are returned as a singular line of text with all of the
        underlying elements rendered as expected:
        
        .. code-block:: markdown
        
            This is an example of a **paragraph** with _formatting_

        :return: 
            the paragraph as a markdown string
        """
        paragraph = ''.join(str(item) for item in self._content)
        return " ".join(paragraph.split())

    def add(self, text: str | Inline) -> Paragraph:
        """
        Adds a text object to the paragraph.
        
        .. doctest:: paragraph
        
            >>> paragraph = Paragraph("Hello! ").add("I come in peace")
            >>> str(paragraph)
            'Hello! I come in peace'

        :param str | Inline text: 
            a custom Inline element
        :return:
            self
        """
        if isinstance(text, str):
            text = Inline(text)
        self._content.append(text)
        return self

    def _replace_any(self, target: str, text: Inline, count: int = -1) -> Paragraph:
        """
        Given a target string, this helper method replaces it with the specified
        Inline object. This method was created because insert_link and
        replace were literally one line different. This method serves as the
        mediator. Note that using this method will introduce several new
        underlying Inline objects even if they could be aggregated.
        At some point, we may just expose this method because it seems handy.
        For example, I foresee a need for a function where all the person wants
        to do is add italics for every instance of a particular string.
        Though, I suppose we could include all of that in the default replace
        method.

        :param str target: 
            the target string to replace
        :param Inline text: 
            the Inline object to insert in place of the target
        :param int count: 
            the number of links to insert; defaults to -1
        :return: 
            self
        """
        i = 0
        content = []
        for inline_text in self._content:
            if inline_text.is_text() and len(items := inline_text._text.split(target)) > 1:
                for item in items:
                    content.append(Inline(item))
                    if count == -1 or i < count:
                        content.append(text)
                        i += 1
                    else:
                        content.append(Inline(target))
                content.pop()
            else:
                content.append(inline_text)
        self._content = content
        return self

    def replace(self, target: str, replacement: str, count: int = -1) -> Paragraph:
        """
        A convenience method which replaces a target string with a string of
        the users choice. Like :meth:`insert_link`, this method is modeled after
        :py:meth:`str.replace` of the standard library. As a result, a count
        can be provided to limit the number of strings replaced in the paragraph.
        
        .. doctest:: paragraph
        
            >>> paragraph = Paragraph("I come in piece").replace("piece", "peace")
            >>> str(paragraph)
            'I come in peace'

        :param str target: 
            the target string to replace
        :param str replacement: 
            the Inline object to insert in place of the target
        :param int count: 
            the number of targets to replace; defaults to -1 (all)
        :return: 
            self
        """
        return self._replace_any(target, Inline(replacement), count)

    def insert_link(self, target: str, link: str, count: int = -1) -> Paragraph:
        """
        A convenience method which inserts links in the paragraph
        for all matching instances of a target string. This method
        is modeled after :py:meth:`str.replace`, so a count can be
        provided to limit the number of insertions. This method
        will not replace links of text that have already been linked.
        See :meth:`snakemd.Paragraph.replace_link` for that behavior.
        
        .. doctest:: paragraph
        
            >>> paragraph = Paragraph("Go here for docs").insert_link("here", "https://snakemd.io")
            >>> str(paragraph)
            'Go [here](https://snakemd.io) for docs'

        :param str target: 
            the string to link
        :param str link: 
            the url or path
        :param int count: 
            the number of links to insert; defaults to -1 (all)
        :return: 
            self
        """
        return self._replace_any(target, Inline(target, link=link), count)

    def replace_link(self, target_link: str, replacement_link: str, count: int = -1) -> Paragraph:
        """
        A convenience method which replaces matching URLs in the paragraph with
        a new url. Like :meth:`insert_link` and :meth:`replace`, this method is also
        modeled after :py:meth:`str.replace`, so a count can be provided to limit
        the number of links replaced in the paragraph. This method is useful
        if you want to replace existing URLs but don't necessarily care what
        the anchor text is.
        
        .. doctest:: paragraph
        
            >>> old = "https://therenegadecoder.com"
            >>> new = "https://snakemd.io"
            >>> paragraph = Paragraph("Go here for docs").insert_link("here", old).replace_link(old, new) 
            >>> str(paragraph)
            'Go [here](https://snakemd.io) for docs'

        :param str target_link: 
            the link to replace
        :param str replacement_link: 
            the link to swap in
        :param int count: 
            the number of links to replace; defaults to -1 (all)
        :return: 
            self
        """
        i = 0
        for text in self._content:
            if (count == -1 or i < count) and text._link == target_link:
                text.link(replacement_link)
                i += 1
        return self
    
    
class Quote(Block):
    """
    A quote is a standalone block of emphasized text. Quotes can be
    nested and can contain other blocks. 

    :param str | Iterable[str | Inline | Block] lines: 
        a single string or a "list" of text objects to be formatted as a quote
    """

    def __init__(self, lines: str | Iterable[str | Inline | Block]) -> None:
        super().__init__()
        self._lines: list[Block] = self._process_content(lines)
        self._depth = 1

    @staticmethod
    def _process_content(lines) -> list[Block]:
        """
        Converts the raw input lines to something that is
        a bit easier to work with. In this case, the lines
        are converted to blocks.

        :param lines: 
            a "list" of text objects or a string
        :return: 
            a list of Blocks
        """
        logger.debug(f"Processing quote lines: {lines}")
        if isinstance(lines, str):
            processed_lines = [Paragraph(lines)]
        else:
            processed_lines = []
            for line in lines:
                if isinstance(line, (str, Inline)):
                    processed_lines.append(Paragraph(line))
                else:
                    processed_lines.append(line)
        return processed_lines

    def __str__(self) -> str:
        """
        Renders the quote as a markdown string. Markdown quotes
        vary in syntax, but the general approach in this repo is
        to apply the quote symbol (i.e., :code:`>`) to the front
        of each line in the quote:
        
        .. code-block:: markdown
        
            > this
            > is
            > a quote
            
        Quotes can also be nested. To make this possible, nested
        quotes are padded by empty quote lines:
        
        .. code-block:: markdown
        
            > Outer quote
            > 
            > > Inner quote
            >
            > Outer quote
            
        It's unclear what is the correct way to handle nested
        quotes, but this format seems to be the most friendly
        for GitHub markdown. Future work may involve including
        the option to removing the padding. 

        :return: 
            the quote formatted as a markdown string
        """
        formatted_lines: list[str] = []
        quote_markers = f"{'> ' * self._depth}"
        for line in self._lines:
            if isinstance(line, Quote):
                line._depth = self._depth + 1
                formatted_lines.extend([
                    quote_markers,
                    str(line),
                    quote_markers
                ])
            else:
                split = f"\n{quote_markers}".join(str(line).splitlines())
                formatted_lines.append(f"{quote_markers}{split}")
        return "\n".join(formatted_lines)


class Raw(Block):
    """
    Raw blocks allow a user to insert text into a Markdown
    document without any processing. Use this block to insert
    raw Markdown or other types of text (e.g., Jekyll frontmatter)
    into a document.
    
    :param str text: the raw text to append to a Document
    """

    def __init__(self, text: str) -> None:
        super().__init__()
        self._text = text

    def __str__(self) -> str:
        """
        Renders the raw block as a markdown string. 
        Raw markdown is unprocessed and passes directly
        through to the document. 

        :return: the raw block as a markdown string
        """
        return self._text


class Table(Block):
    """
    A table is a standalone block of rows and columns. Data is rendered
    according to underlying Inline items.

    All methods described in the Table class include sample
    code. Sample code assumes a generic :code:`table` object exists,
    which can be created as follows:

    .. code-block:: Python

        from snakemd import Table
        table = Table(["Place", "Name"], [["1st", "Crosby"], ["2nd", "McDavid"]])

    :raises ValueError: 
    
        - when rows of table are of varying lengths
        - when lengths of header and rows of table do not match
    :param Iterable[str | Inline | Paragraph] header: 
        the header row of labels
    :param Iterable[Iterable[str | Inline | Paragraph]] body: 
        the collection of rows of data; defaults to an empty list
    :param None | Iterable[Align] align: 
        the column alignment; defaults to None
    :param int indent: 
        indent size for the whole table; defaults to 0
    """

    def __init__(
        self,
        header: Iterable[str | Inline | Paragraph],
        body: Iterable[Iterable[str | Inline | Paragraph]] = [],
        align: None | Iterable[Align] = None,
        indent: int = 0
    ) -> None:
        logger.debug(f"Initializing table\n{(header, body, align)}")
        super().__init__()
        self._header: list[Paragraph]
        self._body: list[list[Paragraph]]
        self._header, self._body = self._process_table(header, body)
        if len(self._body) > 1 and not all(len(self._body[0]) == len(x) for x in self._body[1:]):
            raise ValueError("Table rows are not all the same length")
        elif body and len(self._header) != len(self._body[0]):
            raise ValueError("Table header and rows have different lengths")
        self._widths: list[int] = self._process_widths(
            self._header,
            self._body
        )
        self._align = align
        self._indent = indent

    def __str__(self) -> str:
        """
        Renders the table as a markdown string. Table markdown
        follows the standard pipe syntax:
        
        .. code-block:: 

            | Header 1 | Header 2 |
            | -------- | -------- |
            | Item 1A  | Item 2A  |
            | Item 1B  | Item 2B  |
            
        Alignment code adds colons in the appropriate locations.
        Final tables are rendered according to the widest
        items in each column for readability.

        :return: 
            a table as a markdown string
        """
        rows = list()
        header = [
            str(item).ljust(self._widths[i])
            for i, item in enumerate(self._header)
        ]
        body = [
            [str(item).ljust(self._widths[i]) for i, item in enumerate(row)]
            for row in self._body
        ]
        rows.append(f"{' ' * self._indent}| {' | '.join(header)} |")
        if not self._align:
            rows.append(
                f"{' ' * self._indent}| {' | '.join('-' * width for width in self._widths)} |")
        else:
            meta = []
            for align, width in zip(self._align, self._widths):
                if align == Table.Align.LEFT:
                    meta.append(f":{'-' * (width - 1)}")
                elif align == Table.Align.RIGHT:
                    meta.append(f"{'-' * (width - 1)}:")
                else:
                    meta.append(f":{'-' * (width - 2)}:")
            rows.append(f"{' ' * self._indent}| {' | '.join(meta)} |")
        rows.extend(
            (f"{' ' * self._indent}| {' | '.join(row)} |" for row in body))
        return '\n'.join(rows)

    class Align(Enum):
        """
        Align is an enum only used by the Table class to specify the alignment
        of various columns in the table.
        """
        LEFT = auto()
        RIGHT = auto()
        CENTER = auto()

    @staticmethod
    def _process_table(header, body) -> tuple(list[Paragraph], list[list[Paragraph]], list[int]):
        """
        Processes the table inputs to ensure header and body only contain paragraph blocks.
        Also, this computes the max width of each row to ensure pretty print works every time.

        :param header: 
            the header row in its various forms
        :param body: 
            the table body in its various forms
        :return: 
            the table containing only Paragraph blocks and a list of the widest items in each row
        """
        processed_header = []
        processed_body = []

        # Process header
        for item in header:
            if isinstance(item, (str, Inline)):
                processed_header.append(Paragraph([item]))
            else:
                processed_header.append(item)
        logger.debug(f"Processed header input\n{processed_header}")

        # Process body
        for row in body:
            processed_row = []
            for item in row:
                if isinstance(item, (str, Inline)):
                    processed_row.append(Paragraph([item]))
                else:
                    processed_row.append(item)
            processed_body.append(processed_row)
        logger.debug(f"Processed table body\n{processed_body}")

        return processed_header, processed_body

    @staticmethod
    def _process_widths(header, body) -> list[int]:
        """
        Traverses the table looking to determine the appropriate
        widths for each column. 

        :param header: 
            the header row
        :param body: 
            the rows of data
        :return: 
            a list of column widths
        """
        widths = [len(str(word)) for word in header]
        for row in body:
            for i, item in enumerate(row):
                if (width := len(str(item))) > widths[i]:
                    widths[i] = width
        return widths

    def add_row(self, row: Iterable[str | Inline | Paragraph]) -> None:
        """
        A convenience method which adds a row to the end of table.
        Use this method to build a table row-by-row rather than constructing
        the table rows upfront.  

        .. code-block:: Python

            table.add_row(["3rd", "Matthews"])

        :raises ValueError: 
            when row is not the same width as the table header
        :param Iterable[str | Inline | Paragraph] row: 
            a row of data
        """
        if len(row) != len(self._header):
            raise ValueError(
                f"Unable to add row with width {len(row)} to table with header of width {len(self._header)}"
            )
        logger.debug(f"Adding row to table: {row}")
        self._body.append(row)
