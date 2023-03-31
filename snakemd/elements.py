from __future__ import annotations

import logging
import warnings
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Iterable
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
    

class Element(ABC):
    """
    A generic element interface which provides a framework for all
    types of elements in the collection. In short, elements should
    be able to be verified. 
    """
    
    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def verify(self) -> Verification:
        """
        Verifies that the element is valid markdown.

        :return: a verification object from the violator
        """
        pass
    
    def render(self) -> str:
        """
        Renders the element as a markdown string.
        This function now just calls the __str__
        method directly.
        
        .. deprecated:: 0.14.0
            replaced with the default dunder method :func:`__str__`

        :return: the element as a markdown string
        """
        warnings.warn("render has been replaced by __str__ as of 0.14.0", DeprecationWarning)
        return str(self)


class Inline(Element):
    """
    The basic unit of text in markdown. All components which contain
    text are built using this class instead of strings directly. That
    way, those elements capture all styling information.
    
    .. versionadded:: 0.14.0
        replaced the :class:`InlineText`

    :param str text: the inline text to render
    :param str url: the link associated with the inline text
    :param bool bold: the bold state of the inline text;
        set to True to render bold inline text (i.e., True -> **bold**)
    :param bool italics: the italics state of the inline text;
        set to True to render inline text in italics (i.e., True -> *italics*)
    :param bool strikethrough: the strikethrough state of the inline text;
        set to True to render inline text with a strikethrough (i.e., True -> ~~strikethrough~~)
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
        strikethrough: bool = False,
        code: bool = False,
        image: bool = False
    ) -> None:
        self._text = text
        self._bold = bold
        self._italics = italics
        self._url = url
        self._code = code
        self._image = image
        self._strikethrough = strikethrough

    def __str__(self) -> str:
        """
        Renders self as a string. In this case,
        inline text can represent many different types of data from
        stylized text to inline code to links and images.

        :return: the Inline object as a string
        """
        text = self._text
        if self._bold:
            text = f"**{text}**"
        if self._italics:
            text = f"*{text}*"
        if self._strikethrough:
            text = f"~~{text}~~"
        if self._url:
            text = f"[{text}]({self._url})"
        if self._url and self._image:
            text = f"!{text}"
        if self._code:
            text = f"`{text}`"
        return text

    def render(self) -> str:
        """
        Renders self as a string. In this case,
        inline text can represent many different types of data from
        stylized text to inline code to links and images.
        
        .. deprecated:: 0.14.0
            replaced with the default dunder method :func:`__str__`

        :return: the Inline object as a string
        """
        warnings.warn("render has been replaced by __str__ as of 0.14.0", DeprecationWarning)
        return str(self)

    def verify_url(self) -> bool:
        """
        Verifies that a URL is a valid URL.

        :return: True if the URL is valid; False otherwise
        """
        try:
            req = request.Request(self._url)
            req.get_method = lambda: 'HEAD'
            request.urlopen(req)
            logger.info(f"URL passed verification: {self._url}")
            return True
        except (HTTPError, ValueError):
            logger.info(f"URL failed verification: {self._url}")
            return False

    def verify(self) -> Verification:
        """
        Verifies that the Inline object is valid.

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
        Checks if this Inline is a text-only element. If not, it must
        be an image, a URL, or an inline code snippet.

        .. versionadded:: 0.2.0

        :return: True if this is a text-only element; False otherwise
        """
        return not (self._code or self._image or self._url)

    def is_url(self) -> bool:
        """
        Checks if the Inline object represents a URL.

        :return: True if the object has a URL; False otherwise
        """
        return bool(self._url)

    def bold(self) -> Inline:
        """
        Adds bold styling to self.

        .. versionchanged:: 0.7.0
            Modified to return previous bold state

        :return: self
        """
        self._bold = True
        return self

    def unbold(self) -> Inline:
        """
        Removes bold styling from self.

        .. versionchanged:: 0.7.0
            Modified to return previous bold state

        :return: self
        """
        self._bold = False
        return self

    def italicize(self) -> Inline:
        """
        Adds italics styling to self.

        .. versionadded:: 0.7.0

        :return: self
        """
        self._italics = True
        return self

    def unitalicize(self) -> Inline:
        """
        Removes italics styling from self.

        .. versionadded:: 0.7.0

        :return: self
        """
        self._italics = False
        return self
    
    def strikethrough(self) -> Inline:
        """
        Adds strikethrough styling to self.
        
        .. versionadded:: 0.12.0

        :return: self
        """
        self._strikethrough = True
        return self
    
    def unstrikethrough(self) -> Inline:
        """
        Remove strikethrough styling from self.
        
        .. versionadded:: 0.12.0

        :return: self
        """
        self._strikethrough = False
        return self

    def code(self) -> Inline:
        """
        Adds code style to self.

        .. versionadded:: 0.7.0

        :return: self
        """
        self._code = True
        return self

    def uncode(self) -> Inline:
        """
        Removes code style from self.

        .. versionadded:: 0.7.0

        :return: self
        """
        self._code = False
        return self

    def link(self, url: str) -> Inline:
        """
        Adds URL to self.

        .. versionadded:: 0.7.0

        :param str url: the URL to apply to this Inline element
        :return: self
        """
        self._url = url
        return self

    def unlink(self) -> Inline:
        """
        Removes URL from self.

        .. versionadded:: 0.7.0

        :return: self
        """
        self._url = None
        return self

    def reset(self) -> Inline:
        """
        Removes all settings from self (e.g., bold, code, italics, url, etc.).
        All that will remain is the text itself.

        .. versionadded:: 0.7.0

        :return: self
        """
        self._url = None
        self._code = False
        self._italics = False
        self._bold = False
        self._image = False
        return self
    
    
class InlineText(Inline):
    """
    .. versionchanged:: 0.12.0
        Added strike parameter
    .. deprecated:: 0.14.0
        replaced with :class:`Inline`
    """
    pass


class CheckBox(Inline):
    """
    A checkable box, based of Inline.
    Supports all formats available via Inline (eg. url, bold, italics, etc.)
    
    .. deprecated:: 0.14.0
        checkbox features have moved to the MDList object as the checked parameter

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
    :param bool checked: the checkbox state, checked or not;
        set to True to render checkbox as checked
    """

    def __init__(
        self,
        text: str,
        url: str = None,
        bold: bool = False,
        italics: bool = False,
        code: bool = False,
        image: bool = False,
        checked: bool = False
    ) -> None:
        super().__init__(
            text,
            url=url,
            bold=bold,
            italics=italics,
            code=code,
            image=image
        )
        self.checked = checked
        warnings.warn(
            "CheckBox is replaced by the MDList checked parameter", 
            DeprecationWarning
        )
        
    def __str__(self) -> str:
        """
        Renders the Checkbox.

        :return: the checkbox as a string
        """
        checked_str = "X" if self.checked else " "
        return f"[{checked_str}] {super().__str__()}"

    def render(self) -> str:
        """
        Renders the Checkbox.
        
        .. deprecated:: 0.14.0
            replaced with the default dunder method :func:`__str__`

        :return: the checkbox as a string
        """
        warnings.warn("render has been replaced by __str__ as of 0.14.0", DeprecationWarning)
        return str(self)
    
    
class Block(Element):
    """
    A block element in Markdown. A block is defined as a standalone 
    element starting on a newline. Examples of blocks include paragraphs (i.e., <p>), 
    headings (e.g., <h1>, <h2>, etc.), tables (i.e., <table>), and lists
    (e.g., <ol>, <ul>, etc.).
    
    .. versionadded:: 0.14.0
        replaced the :class:`Element` class
    """
    pass


class HorizontalRule(Block):
    """
    A horizontal rule is a line separating different sections of
    a document. Horizontal rules really only come in one form,
    so there are no settings to adjust.

    .. versionadded:: 0.2.0
    """

    def __init__(self):
        super().__init__()
        
    def __str__(self) -> str:
        """
        Renders the horizontal rule using the three dash syntax.

        .. versionadded:: 0.2.0

        :return: the horizontal rule as a markdown string
        """
        return "---"

    def verify(self) -> Verification:
        """
        Verifies the structure of the HorizontalRule block.
        Because there is no way to customize this object,
        it is always valid. Therefore, this method returns an
        empty Verification object.

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        return Verification()


class Heading(Block):
    """
    A heading is a text block which serves as the title for a new
    section of a document. Headings come in six main sizes which
    correspond to the six headings sizes in HTML (e.g., <h1>).

    :param str | Inline | Iterable[Inline | str] text: the heading text
    :param int level: the heading level between 1 and 6 (rounds to closest bound if out of range)
    """

    def __init__(self, text: str | Inline | Iterable[Inline | str], level: int) -> None:
        super().__init__()
        self._text: list[Inline] = self._process_text(text)
        self._level: int = self._process_level(level)
        
    def __str__(self) -> str:
        """
        Renders the heading in markdown according to
        the level provided.

        :return: the heading as a markdown string
        """
        heading = [str(item) for item in self._text]
        return f"{'#' * self._level} {''.join(heading)}"

    @staticmethod
    def _process_text(text: str | Inline | Iterable[Inline | str]) -> list[Inline]:
        """
        Ensures that Heading objects are composed of a single Inline object.

        :param text: an object to be forced to Inline
        :return: the input text as an Inline
        """
        if isinstance(text, str):
            return [Inline(text)]
        elif isinstance(text, Inline):
            return [text]
        else:
            return [
                item if isinstance(item, Inline) else Inline(item) 
                for item in text
            ]
        
    @staticmethod
    def _process_level(level: int) -> int:
        """
        Restricts the range of possible levels to avoid issues with rendering.

        :param int level: the heading level
        :return: the heading level in the proper range
        """
        if level < 1:
            level = 1
        if level > 6:
            level = 6
        return level

    def verify(self) -> Verification:
        """
        Verifies that the provided heading is valid. This mainly
        returns errors associated with the Inline element
        provided during instantiation.

        .. versionadded:: 0.2.0

        :return: a verification object from the violator
        """
        return self._text.verify()

    def promote(self) -> None:
        """
        Promotes a heading up a level. Fails silently
        if the heading is already at the highest level (i.e., <h1>).
        """
        if self._level > 1:
            self._level -= 1

    def demote(self) -> None:
        """
        Demotes a heading down a level. Fails silently if
        the heading is already at the lowest level (i.e., <h6>).
        """
        if self._level < 6:
            self._level += 1
            
    def get_text(self) -> str:
        """
        Returns the heading text free of any styling.
        
        .. versionadded:: 0.15.0

        :return: the heading as a string
        """
        text_elements = [item._text for item in self._text]
        return ''.join(text_elements)
            

class Header(Heading):
    """
    .. deprecated:: 0.13.0
        renamed to :class:`Heading`
    """
    def __init__(self, text: Inline | str, level: int) -> None:
        super().__init__(text, level)
        warnings.warn(
            "Header has been deprecated as of 0.13.0 and replaced with Heading", 
            DeprecationWarning
        )


class Code(Block):
    """
    A code block is a standalone block of syntax-highlighted code.
    Code blocks can have generic highlighting or highlighting based
    on their language. 

    .. versionadded:: 0.15.0
    """
    
    def __init__(self, code: str | Code, lang: str = "generic"):
        super().__init__()
        self._code = code
        self._lang = lang
        
    def __str__(self) -> str:
        ticks = '`' * 3
        if isinstance(self._code, Code):
            ticks = '`' * 4
        return f"{ticks}{self._lang}\n{self._code}\n{ticks}"
    
    def verify(self) -> Verification:
        return Verification()


class Paragraph(Block):
    """
    A paragraph is a standalone block of text. Paragraphs can be
    formatted in a variety of ways including as code and blockquotes.

    .. versionchanged:: 0.4.0
        Expanded constructor to accept strings directly

    :param Iterable[Inline | str] content: a "list" of text objects to render as a paragraph
    :param bool code: the code state of the paragraph;
        set True to convert the paragraph to a code block (i.e., True -> ```code```)
        
        .. deprecated:: 0.15.0
            replaced in favor of the :class:`Code` block
        
    :param str lang: the language of the code snippet;
        invalid without the code flag set to True
        
        .. deprecated:: 0.15.0
            replaced in favor of the :class:`Code` block
        
    :param bool quote: the quote state of the paragraph;
        set True to convert the paragraph to a blockquote (i.e., True -> > quote)
    """

    def __init__(self, content: Iterable[Inline | str], code: bool = False, lang: str = "generic", quote: bool = False):
        super().__init__()
        self._content: list[Inline] = self._process_content(content)
        self._code = code
        self._lang = lang
        self._quote = quote

    @staticmethod
    def _process_content(content) -> None:
        processed = []
        for item in content:
            if isinstance(item, str):
                processed.append(Inline(item))
            else:
                processed.append(item)
        return processed
    
    def __str__(self) -> str:
        """
        Renders the paragraph as markdown according to the settings provided.
        For example, if the code flag is enabled, the paragraph will be
        rendered as a code block. If both flags are enabled, code takes
        precedence.

        .. versionchanged:: 0.4.0
            No longer assumes spaces between Inline items

        :return: the paragraph as a markdown string
        """
        paragraph = ''.join(str(item) for item in self._content)
        if self._code:
            code_block = Code(self._code, self._lang)
            return str(code_block)
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

        # Inline errors
        for text in self._content:
            verification.absorb(text.verify())

        return verification

    def add(self, text: Inline | str) -> None:
        """
        Adds a text object to the paragraph.

        .. versionchanged:: 0.4.0
            Allows adding of strings directly

        :param text: a custom Inline element
        """
        if isinstance(text, str):
            text = Inline(text)
        self._content.append(text)

    def is_text(self) -> bool:
        """
        Checks if this Paragraph is a text-only block. If not, it must
        be a quote or code block.

        .. versionadded:: 0.3.0

        :return: True if this is a text-only block; False otherwise
        """
        return not (self._code or self._quote)

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

        :param str target: the target string to replace
        :param Inline text: the Inline object to insert in place of the target
        :param int count: the number of links to insert; defaults to -1
        :return: self
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
        the users choice. Like insert_link, this method is modeled after
        :code:`str.replace()` of the standard library. As a result, a count
        can be provided to limit the number of strings replaced in the paragraph.

        .. versionadded:: 0.5.0

        :param str target: the target string to replace
        :param str replacement: the Inline object to insert in place of the target
        :param int count: the number of links to insert; defaults to -1
        :return: self
        """
        return self._replace_any(target, Inline(replacement), count)

    def insert_link(self, target: str, url: str, count: int = -1) -> Paragraph:
        """
        A convenience method which inserts links in the paragraph
        for all matching instances of a target string. This method
        is modeled after :code:`str.replace()`, so a count can be
        provided to limit the number of insertions. This method
        will not replace links of text that have already been linked.
        See replace_link() for that behavior.

        .. code-block:: Python

            paragraph.insert_link("Here", "https://therenegadecoder.com")

        .. versionadded:: 0.2.0
        .. versionchanged:: 0.5.0
            Changed function to insert links at all instances of target
            rather than just the first instance

        :param str target: the string to link
        :param str url: the url to link
        :param int count: the number of links to insert; defaults to -1 (all)
        :return: self
        """
        return self._replace_any(target, Inline(target, url=url), count)

    def replace_link(self, target: str, url: str, count: int = -1) -> Paragraph:
        """
        A convenience method which replaces matching URLs in the paragraph with
        a new url. Like insert_link() and replace(), this method is also
        modeled after :code:`str.replace()`, so a count can be provided to limit
        the number of links replaced in the paragraph. This method is useful
        if you want to replace existing URLs but don't necessarily care what
        the anchor text is.

        .. versionadded:: 0.7.0

        :param str target: the string to link
        :param str url: the url to link
        :param int count: the number of links to replace; defaults to -1 (all)
        :return: self
        """
        i = 0
        for text in self._content:
            if (count == -1 or i < count) and text._url == target:
                text.link(url)
                i += 1
        return self

    def verify_urls(self) -> dict[str, bool]:
        """
        Verifies all URLs in the paragraph. Results are
        returned in a dictionary where the URLs are
        mapped to their validity.

        :return: a dictionary of URLs mapped to their validity
        """
        result = {}
        for item in self._content:
            result[item._url] = item.is_url() and item.verify_url()
        return result


class MDList(Block):
    """
    A markdown list is a standalone list that comes in three varieties: ordered, unordered, and checked.

    .. versionchanged:: 0.4.0
        Expanded constructor to accept strings directly

    :param Iterable[str | Inline | Paragraph | MDList] items:
        a "list" of objects to be rendered as a list
    :param bool ordered: the ordered state of the list;
        set to True to render an ordered list (i.e., True -> 1. item)
    :param None | bool | Iterable[bool] checked: the checked state of the list;
        set to True, False, or an iterable of booleans to enable the checklist feature.
    """

    def __init__(
        self, 
        items: Iterable[str | Inline | Paragraph | MDList], 
        ordered: bool = False, 
        checked: None | bool | Iterable[bool] = None
    ) -> None:
        super().__init__()
        self._items: MDList | Paragraph = self._process_items(items)
        self._ordered = ordered
        self._checked = checked
        self._space = ""
        
    def __str__(self) -> str:
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
    def _process_items(items):
        """
        Given the variety of data that MDList can accept, this function
        forces all possible data types to be either MDLists or Paragraphs.

        :param items: a list of items
        :return: a list of paragraphs and MDLists
        """
        processed = []
        for item in items:
            if isinstance(item, (str, Inline)):
                processed.append(Paragraph([item]))
            else:
                processed.append(item)
        return processed

    def _get_indent_size(self, item_index: int = -1) -> int:
        """
        Returns the number of spaces that any sublists should be indented.

        :param int item_index: the index of the item to check (only used for ordered lists);
            defaults to -1
        :return: the number of spaces
        """
        if not self._ordered:
            return 2
        else:
            # Ordered items vary in length, so we adjust the result based on the index
            return 2 + len(str(item_index))

    def verify(self) -> Verification:
        """
        Verifies that the markdown list is valid. Mainly, this checks the validity
        of the containing Inline items. The MDList class has no way to
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


class MDCheckList(MDList):
    """
    A markdown CheckBox list has boxes that can be clicked.

    .. versionadded:: 0.10.0
    
    .. deprecated:: 0.14.0
        MDChecklist has been replaced with preference for the MDList checked parameter

    :param Iterable[str | Inline | Paragraph | MDList] items:
        a "list" of objects to be rendered as a Checkbox list
    :param bool checked: the state of the checkbox;
        set to True to render a checked box (i.e., True -> - [x] item)
    """

    def __init__(self,  items: Iterable[str | Inline | Paragraph | MDList], checked: bool = False) -> None:
        super().__init__(items, False)
        self.checked = checked
        warnings.warn(
            "MDChecklist is replaced by the MDList checked parameter", 
            DeprecationWarning
        )
        
    def __str__(self) -> str:
        """
        Renders the markdown Check Box list according to the settings provided.
        For example, if the the checked flag is set, a checked list
        will be rendered in markdown.

        :return: the list as a markdown string
        """
        output = list()
        i = 1
        for item in self._items:
            if isinstance(item, MDList):
                item._space = self._space + " " * self._get_indent_size(i)
                output.append(str(item))
            else:
                checked_str = "X" if self.checked else " "
                output.append(f"{self._space}- [{checked_str}] {item}")

        return "\n".join(output)


class Table(Block):
    """
    A table is a standalone block of rows and columns. Data is rendered
    according to underlying Inline items.

    .. versionchanged:: 0.4.0
        Added optional alignment parameter and expanded constructor to accept strings
    .. versionchanged:: 0.11.0
        Added optional indentation parameter for the whole table
    .. versionchanged:: 0.12.0
        Made body parameter optional

    :param header: the header row of labels
    :param body: the collection of rows of data
    :param align: the column alignment
    :param indent: indent size for the whole table
    """

    def __init__(
        self,
        header: Iterable[str | Inline | Paragraph],
        body: Iterable[Iterable[str | Inline | Paragraph]] = [],
        align: Iterable[Align] = None,
        indent: int = 0
    ) -> None:
        logger.debug(f"Initializing table\n{(header, body, align)}")
        super().__init__()
        self._header: list[Paragraph]
        self._body: list[list[Paragraph]]
        self._widths: list[int]
        self._header, self._body, self._widths = self._process_table(header, body)
        self._align = align
        self._indent = indent
        
    def __str__(self) -> str:
        """
        Renders a markdown table from a header "list"
        and a data set.

        .. versionchanged:: 0.4.0
            Modified to support column alignment and pipes on both sides of the table

        :return: a table as a markdown string
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

        .. versionadded:: 0.4.0
        """
        LEFT = auto()
        RIGHT = auto()
        CENTER = auto()

    @staticmethod
    def _process_table(header, body) -> tuple(list[Paragraph], list[list[Paragraph]], list[int]):
        """
        Processes the table inputs to ensure header and body only contain paragraph blocks.
        Also, this computes the max width of each row to ensure pretty print works every time.

        .. versionadded:: 0.4.0

        :param header: the header row in its various forms
        :param body: the table body in its various forms
        :return: the table containing only Paragraph blocks and a list of the widest items in each row
        """

        processed_header = []
        processed_body = []
        widths = []

        # Process header
        for item in header:
            if isinstance(item, (str, Inline)):
                processed_header.append(Paragraph([item]))
            else:
                processed_header.append(item)
            widths.append(len(str(item)))
        logger.debug(f"Processed header input\n{processed_header}")
        logger.debug(f"Computed initial column widths\n{widths}")

        # Process body
        for row in body:
            processed_row = []
            for i, item in enumerate(row):
                if isinstance(item, (str, Inline)):
                    processed_row.append(Paragraph([item]))
                else:
                    processed_row.append(item)
                if (width := len(str(item))) > widths[i]:
                    widths[i] = width
            processed_body.append(processed_row)
        logger.debug(f"Processed table body\n{processed_body}")

        return processed_header, processed_body, widths

    def add_row(self, row: Iterable[str | Inline | Paragraph]) -> None:
        """
        Adds a row to the end of table. 

        .. versionadded:: 0.12.0
        """
        self._body.append(row)

    def verify(self):
        """
        Verifies the integrity of the markdown table. There are various ways
        a user could instantiate this object improperly. For example, they may
        provide a body with roes that are not all equal width. Likewise, the
        header may not match the width of the body. Inline elements may also
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

        for item in self._header:
            verification.absorb(item.verify())
        for row in self._body:
            for item in row:
                verification.absorb(item.verify())

        return verification
    
    
class Raw(Block):
    """
    Raw blocks allow a user to insert text into the Markdown
    document without an processing. Use this block to insert
    raw Markdown or other types of text (e.g., Jekyll frontmatter).
    
    .. versionadded:: 0.14.0
    """
    def __init__(self, text: str) -> None:
        super().__init__()
        self._text = text
        
    def __str__(self) -> str:
        return self._text
    
    def verify(self) -> Verification:
        return Verification()

