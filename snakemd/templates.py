"""
The template module houses the Template class
and all of it's children.
"""

from __future__ import annotations

import logging


from .elements import Element, Heading, Inline, MDList, Block

logger = logging.getLogger(__name__)


class Template(Element):
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
        self._elements: list[Element] = None

    def load(self, elements: list[Element]) -> None:
        self._elements = elements


class TableOfContents(Template):
    """
    A Table of Contents is an block containing an ordered list
    of all the `<h2>` headings in the document by default. A range can be
    specified to customize which headings (e.g., `<h3>`) are included in
    the table of contents. This element can be placed anywhere in the document.

    .. versionchanged:: 2.2
        Removed the doc parameter

    :param range[int] levels:
        a range of integers representing the sequence of heading levels
        to include in the table of contents; defaults to range(2, 3)
    """

    def __init__(self, levels: range = range(2, 3)):
        super().__init__()
        self._levels: range = levels
        logger.debug("New table of contents initialized with levels in %s", levels)

    def __str__(self) -> str:
        """
        Renders the table of contents using the Document reference.

        :return:
            the table of contents as a markdown string
        """
        headings = self._get_headings()
        table_of_contents, _ = self._assemble_table_of_contents(headings, 0)
        return str(table_of_contents)

    def __repr__(self) -> str:
        return f"TableOfContents(levels={self._levels!r})"

    def _get_headings(self) -> list[Heading]:
        """
        Retrieves the list of headings from the current document.

        :return:
            a list heading objects
        """
        return [
            heading
            for heading in self._elements
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
        table_of_contents = []
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
