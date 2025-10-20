"""
The template module houses the Template class
and all of it's children.
"""

from __future__ import annotations

import csv
import logging
import os
import re
from typing import Iterable
from enum import Enum, auto

from .elements import Block, Element, Heading, Inline, MDList, Quote, Table

logger = logging.getLogger(__name__)


class Template(Element):  # pylint: disable=too-few-public-methods
    """
    A template element in Markdown. A template can be thought of as a subdocument or
    collection of blocks. The entire purpose of the Template interface is to provide
    a superclass for a variety of abstractions over the typical markdown features.
    For example, Markdown has no feature for tables of contents, but a template
    could be created to generate one automatically for the user. In other words,
    templates are meant to be convience objects for our users.

    One cool feature of templates is that they are lazy loaded. Unlike traditional
    elements, this means templates aren't fully loaded until they are about to
    be rendered. The benefit is that we can place templates in our documents as
    placeholders without much configuration. Then, right before the document is
    rendered, the template will be injected with a reference to the contents
    of the document. As a result, templates are able to take advantage of the
    final contents of the document, such as being able to generate a word count
    from the words in the document or generate a table of contents from the
    headings in the document.

    Note that the user does not have to worry about lazy loading at all.
    The document will take care of the dependency injection. If, however,
    the user needs to render a template outside the context of a document,
    they must call the load function manually.
    """

    def __init__(self) -> None:
        self._elements: list[Element] = None  # DO NOT MODIFY

    def load(self, elements: list[Element]) -> None:
        """
        Loads the template with a list of elements, presumably
        from an existing document.

        :param elements: a list of document elements
        """
        self._elements = elements


class Alerts(Template):
    """
    Alerts are a wrapper of the Quote object to provide
    support for the alerts Markdown extension. While
    quotes can be nested in each other, alerts cannot.  

    .. versionadded:: 2.4
        Included for user convenience

    :param Kind kind: 
        the kind of alert; limited to:

        - NOTE
        - TIP
        - IMPORTANT 
        - WARNING
        - CAUTION
    :param str | Iterable[str | Inline | Block] message:
        the message you would like to show with the alert
    """

    class Kind(Enum):
        NOTE = auto()
        TIP = auto()
        IMPORTANT = auto()
        WARNING = auto()
        CAUTION = auto()

    def __init__(self, kind: Kind, message: str | Iterable[str | Inline | Block]) -> None:
        super().__init__()
        self._kind = kind
        self._message = message
        self._alert = Quote([f"[!{self._kind.name}]", self._message])

    def __str__(self) -> str:
        """
        Renders self as a markdown ready string. See
        :class:`snakemd.Quote` for more details.

        :return:
            the Alert as a markdown string
        """
        return str(self._alert)

    def __repr__(self) -> str:
        """
        Renders self as an unambiguous string for development.
        See :class:`snakemd.Quote` for more details.

        :return:
            the Alert as a development string
        """
        return repr(self._alert)
    
    
class Checklist(Template):
    """
    Checklist is an MDList extension to provide support
    for Markdown checklists, which are a Markdown
    extension. Previously, this feature was baked
    directly into MDList. However, because checklists
    are not a vanilla Markdown feature, they were
    moved here.
    
    .. versionadded:: 2.4
        Included for user convenience
    
    :raises ValueError:
        when the checked argument is an Iterable[bool] that does not
        match the number of top-level elements in the list
    :param Iterable[str | Inline | Block] items:
        a "list" of objects to be rendered as a list
    :param bool | Iterable[bool] checked:
        the checked state of the list

        - defaults to :code:`False` which renders a series of unchecked 
          boxes (i.e., :code:`- [ ]`)
        - set to :code:`True` to render a series of checked boxes
          (i.e., :code:`- [x]`)
        - set to :code:`Iterable[bool]` to render the checked
          status of the top-level list elements directly
    """
    def __init__(
        self, 
        items: Iterable[str | Inline | Block], 
        checked: bool | Iterable[bool] = False
    ) -> None:
        super().__init__()
        self._items: list[Block] = MDList._process_items(items)
        self._checked: bool | list[bool] = (
            checked if checked is None or isinstance(checked, bool) else list(checked)
        )
        self._space = ""
        if isinstance(self._checked, list) and MDList._top_level_count(self._items) != len(
            self._checked
        ):
            raise ValueError(
                "Number of top-level elements in checklist does not "
                "match number of booleans supplied by checked parameter: "
                f"{self._checked}"
            )
    
    def __str__(self):
        output = []
        i = 1
        for item in self._items:
            if isinstance(item, Checklist | MDList):
                item._space = self._space + " " * 2
                output.append(str(item))
            else:
                row = f"{self._space}-"
                
                if isinstance(self._checked, bool):
                    checked_str = "X" if self._checked else " "
                    row = f"{row} [{checked_str}] {item}"
                else:
                    checked_str = "X" if self._checked[i - 1] else " "
                    row = f"{row} [{checked_str}] {item}"
                
                output.append(row)
            i += 1
        
        checklist = "\n".join(output)
        logger.debug("Rendered markdown list: %r", checklist)
        return checklist
    
    def __repr__(self) -> str:
        """
        Renders self as an unambiguous string for development.
        In this case, it displays in the style of a dataclass,
        where instance variables are listed with their
        values. Unlike many of the other templates, Checklists
        aren't a direct wrapper of MDList, and therefore cannot
        be represented as MDList alone. 

        .. doctest:: checklist

            >>> checklist = Checklist(["Do Homework"], True)
            >>> repr(checklist)
            "Checklist(items=[Paragraph(...)], checked=True)"

        :return:
            the Checklist object as a development string
        """
        return (
            f"Checklist("
            f"items={self._items!r}, "
            f"checked={self._checked!r}"
            f")"
        )


class CSVTable(Template):
    """
    A CSV Table is a wrapper for the Table Block,
    which provides a seamless way to load CSV data
    into Markdown. Because Markdown tables are
    required to have headers, the first row of
    the CSV is assumed to be a header. Future
    iterations of this template may allow users
    to select the exact row for their header.
    Future iterations may also allow for different
    CSV dialects like Excel.

    .. versionadded:: 2.2
        Included to showcase the possibilities of
        templates

    :param os.Pathlike path:
        the path to a CSV file
    :param str encoding:
        the encoding of the CSV file; defaults to utf-8
    """

    def __init__(self, path: os.PathLike, encoding: str = "utf-8") -> None:
        super().__init__()
        self._path = path
        self._encoding = encoding
        self._table = self._process_csv(path, encoding)

    def __str__(self) -> str:
        """
        Renders self as a markdown ready string. See
        :class:`snakemd.Table` for more details.

        :return:
            the CSVTable as a markdown string
        """
        return str(self._table)

    def __repr__(self) -> str:
        """
        Renders self as an unambiguous string for development.
        See :class:`snakemd.Table` for more details.

        :return:
            the CSVTable as a development string
        """
        return repr(self._table)

    @staticmethod
    def _process_csv(path: os.PathLike, encoding: str) -> Table:
        """
        A helper method for processing the CSV file into
        a Table object.

        :param os.Pathlike path:
            the path to the CSV file
        :param str encoding:
            the encoding of the CSV file
        :return:
            the CSV file as a markdown Table
        """
        with open(path, encoding=encoding) as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            table = Table(header=header)
            for row in csv_reader:
                table.add_row(row=row)
            return table


class TableOfContents(Template):
    """
    A Table of Contents is an element containing an ordered list
    of all the `<h2>` headings in the document by default. A range can be
    specified to customize which headings (e.g., `<h3>`) are included in
    the table of contents. This element can be placed anywhere in the document.

    .. versionchanged:: 2.2
        Removed the doc parameter

    :param range[int] levels:
        a range of integers representing the sequence of heading levels
        to include in the table of contents; defaults to range(2, 3)
    """

    def __init__(self, levels: range = range(2, 3)) -> None:
        super().__init__()
        self._levels: range = levels
        logger.debug(
            "New table of contents initialized with levels in %s", levels)

    def __str__(self) -> str:
        """
        Renders self as a markdown ready string. See :class:`snakemd.MDList`
        for more details.

        :return:
            the table of contents as a markdown string
        """
        headings = self._get_headings()
        table_of_contents, _ = self._assemble_table_of_contents(headings, 0)
        return str(table_of_contents)

    def __repr__(self) -> str:
        return f"TableOfContents(levels={self._levels!r})"

    @staticmethod
    def _convert_heading_to_anchor(text: str):
        """
        A helper method for generating anchor text. 
        Technique is borrowed from the python markdown's
        toc extension.
        """
        anchor = re.sub(r'[^\w\s-]', '', text).strip().lower()
        return re.sub(r'[-\s]+', "-", anchor)

    def _get_headings(self) -> list[Heading]:
        """
        Retrieves the list of headings from the current document.

        :return:
            a list heading objects
        """
        return [
            heading
            for heading in self._elements
            if isinstance(heading, Heading) and heading.get_level() in self._levels
        ]

    def _assemble_table_of_contents(
        self, headings: list[Heading], position: int
    ) -> tuple[MDList, int]:
        """
        Assembles the table of contents from the headings in the document.

        :return:
            a list of strings representing the table of contents
        """
        if not headings:
            return MDList([]), -1

        i = position
        level = headings[i].get_level()
        table_of_contents = []
        while i < len(headings) and headings[i].get_level() >= level:
            heading_text: str = headings[i].get_text()
            heading_level: int = headings[i].get_level()
            if heading_level == level:
                line = Inline(
                    heading_text,
                    link=f"#{self._convert_heading_to_anchor(heading_text)}",
                )
                table_of_contents.append(line)
                i += 1
            else:
                sublevel, size = self._assemble_table_of_contents(headings, i)
                table_of_contents.append(sublevel)
                i += size
        return MDList(table_of_contents, ordered=True), i - position
