"""
The template module houses the Template class
and all of it's children.
"""

from __future__ import annotations

import logging

from .elements import Element, Heading, Inline, MDList

logger = logging.getLogger(__name__)


class Template(Element):
    """
    A template element in Markdown. A template can be thought of as a subdocument or
    collection of blocks. The entire purpose of the Template interface is to provide
    a superclass for a variety of abstractions over the typical markdown features.
    For example, Markdown has no feature for tables of contents, but a template
    could be created to generate one automatically for the user. In other words,
    templates are meant to be conviences objects for our users.
    """

    pass


class TableOfContents(Template):
    """
    A Table of Contents is an block containing an ordered list
    of all the `<h2>` headings in the document by default. A range can be
    specified to customize which headings (e.g., `<h3>`) are included in
    the table of contents. This element can be placed anywhere in the document.

    :param Document doc:
        a reference to the document containing this table of contents
    :param list[int] levels:
        a range of integers representing the sequence of heading levels
        to include in the table of contents; defaults to range(2, 3)
    """

    def __init__(self, doc: "Document", levels: range = range(2, 3)):
        super().__init__()
        self._contents = doc._contents  # DO NOT MODIFY
        self._levels = levels
        logger.debug(f"New table of contents initialized with levels in {range}")

    def __str__(self) -> str:
        """
        Renders the table of contents using the Document reference.

        :return:
            the table of contents as a markdown string
        """
        headings = self._get_headings()
        table_of_contents, _ = self._assemble_table_of_contents(headings, 0)
        return str(table_of_contents)

    def _get_headings(self) -> list[Heading]:
        """
        Retrieves the list of headings from the current document.

        :return:
            a list heading objects
        """
        return [
            heading
            for heading in self._contents
            if isinstance(heading, Heading) and heading._level in self._levels
        ]

    def _assemble_table_of_contents(
        self, headings: list[Heading], position: int
    ) -> tuple(MDList, int):
        """
        Assembles the table of contents from the headings in the document.

        :return:
            a list of strings representing the table of contents
        """
        if not headings:
            return MDList([]), -1

        i = position
        level = headings[i]._level
        table_of_contents = list()
        while i < len(headings) and headings[i]._level >= level:
            if headings[i]._level == level:
                line = Inline(
                    headings[i].get_text(),
                    link=f"#{'-'.join(headings[i].get_text().lower().split())}",
                )
                table_of_contents.append(line)
                i += 1
            else:
                sublevel, size = self._assemble_table_of_contents(headings, i)
                table_of_contents.append(sublevel)
                i += size
        return MDList(table_of_contents, ordered=True), i - position
