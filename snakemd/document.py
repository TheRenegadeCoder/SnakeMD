from __future__ import annotations

import logging
import os
import pathlib
import random
from typing import Iterable

from .elements import *
from .templates import *

logger = logging.getLogger(__name__)


class Document:
    """
    A document represents a markdown file. Documents store
    a collection of blocks which are appended with new lines
    between to generate the markdown document. Document methods
    are intended to provided convenience when generating a
    markdown file. However, the functionality is not exhaustive.
    To get the full range of markdown functionality, you can
    take advantage of the :func:`add_block` function to provide
    custom markdown blocks.
    
    All methods described in the Document class include sample
    code. Sample code assumes a generic :code:`doc` object exists,
    which can be created as follows:
    
    .. code-block:: Python

        import snakemd
        doc = snakemd.new_doc()
    """

    def __init__(self) -> None:
        self._contents: list[Block] = list()
        logger.debug("New document initialized")

    def __str__(self):
        """
        Renders the markdown document from a list of blocks.

        :return: the document as a markdown string
        """
        return "\n\n".join(str(block) for block in self._contents)

    def add_block(self, block: Block) -> Block:
        """
        A generic function for appending blocks to the document.
        Use this function when you want a little more control over
        what the output looks like.

        .. code-block:: Python

            doc.add_block(Heading("Python is Cool!"), 2))

        :param Block block: a markdown block (e.g., Table, Heading, etc.)
        :return: the Block added to this Document
        """
        self._contents.append(block)
        logger.debug(f"Added custom block to document\n{block}")
        return block

    def add_raw(self, text: str) -> Raw:
        """
        A convenience method which adds text as-is to the document:

        .. code-block:: Python

            doc.add_raw("X: 5\\nY: 4\\nZ: 3")

        :param str text: some text 
        :return: the Raw block added to this Document
        """
        raw = Raw(text)
        self._contents.append(raw)
        logger.debug(f"Added raw block to document\n{text}")
        return raw

    def add_heading(self, text: str, level: int = 1) -> Heading:
        """
        A convenience method which adds a simple heading to the document:

        .. code-block:: Python

            doc.add_heading("Welcome to SnakeMD!")

        :param str text: the text for the heading
        :param int level: the level of the heading from 1 to 6
        :return: the Heading added to this Document
        """
        heading = Heading(Inline(text), level)
        self._contents.append(heading)
        logger.debug(f"Added heading to document\n{heading}")
        return heading

    def add_paragraph(self, text: str) -> Paragraph:
        """
        A convenience method which adds a simple paragraph of text to the document:

        .. code-block:: Python

            doc.add_paragraph("Mitochondria is the powerhouse of the cell.")

        :param str text: any arbitrary text
        :return: the Paragraph added to this Document
        """
        paragraph = Paragraph([Inline(text)])
        self._contents.append(paragraph)
        logger.debug(f"Added paragraph to document\n{paragraph}")
        return paragraph

    def add_ordered_list(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds a simple ordered list to the document:

        .. code-block:: Python

            doc.add_ordered_list(["Goku", "Piccolo", "Vegeta"])

        :param Iterable[str] items: a "list" of strings
        :return: the MDList added to this Document
        """
        md_list = MDList([Inline(item) for item in items], ordered=True)
        self._contents.append(md_list)
        logger.debug(f"Added ordered list to document\n{md_list}")
        return md_list

    def add_unordered_list(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds a simple unordered list to the document.

        .. code-block:: Python

            doc.add_unordered_list(["Deku", "Bakugo", "Kirishima"])

        :param Iterable[str] items: a "list" of strings
        :return: the MDList added to this Document
        """
        md_list = MDList([Inline(item) for item in items])
        self._contents.append(md_list)
        logger.debug(f"Added unordered list to document\n{md_list}")
        return md_list

    def add_checklist(self, items: Iterable[str]) -> MDList:
        """
        A convenience method which adds a simple checklist to the document.

        .. code-block:: Python

            doc.add_checklist(["Okabe", "Mayuri", "Kurisu"])

        :param Iterable[str] items: a "list" of strings
        :return: the MDCheckList added to this Document
        """
        md_checklist = MDList([Inline(item) for item in items], checked=False)
        self._contents.append(md_checklist)
        logger.debug(f"Added checklist to document\n{md_checklist}")
        return md_checklist

    def add_table(
        self,
        header: Iterable[str],
        data: Iterable[Iterable[str]],
        align: Iterable[Table.Align] = None,
        indent: int = 0
    ) -> Table:
        """
        A convenience method which adds a simple table to the document:

        .. code-block:: Python

            doc.add_table(
                ["Place", "Name"],
                [
                    ["1st", "Robert"],
                    ["2nd", "Rae"]
                ],
                [snakemd.Table.Align.CENTER, snakemd.Table.Align.RIGHT],
                0
            )

        :param Iterable[str] header: a "list" of strings
        :param Iterable[Iterable[str]] data: a "list" of "lists" of strings
        :param Iterable[Table.Align] align: a "list" of column alignment values;
            defaults to None
        :param int indent: indent size for the whole table
        :return: the Table added to this Document
        """
        header = [Paragraph([text]) for text in header]
        data = [[Paragraph([item]) for item in row] for row in data]
        table = Table(header, data, align, indent)
        self._contents.append(table)
        logger.debug(f"Added table to document\n{table}")
        return table

    def add_code(self, code: str, lang: str = "generic") -> Code:
        """
        A convenience method which adds a code block to the document:

        .. code-block:: Python

            doc.add_code("x = 5")

        :param str code: a preformatted code string
        :param str lang: the language for syntax highlighting
        :return: the Code block added to this Document
        """
        code_block = Code(code, lang=lang)
        self._contents.append(code_block)
        logger.debug(f"Added code block to document\n{code_block}")
        return code_block

    def add_quote(self, text: str) -> Quote:
        """
        A convenience method which adds a blockquote to the document:

        .. code-block:: Python

            doc.add_quote("Welcome to the Internet!")

        :param str text: the text to be quoted
        :return: the Quote added to this Document
        """
        quote = Quote(text)
        self._contents.append(quote)
        logger.debug(f"Added quote to document\n{quote}")
        return quote

    def add_horizontal_rule(self) -> HorizontalRule:
        """
        A convenience method which adds a horizontal rule to the document:

        .. code-block:: Python

            doc.add_horizontal_rule()

        :return: the HorizontalRule added to this Document
        """
        hr = HorizontalRule()
        self._contents.append(hr)
        logger.debug(f"Added horizontal rule to document\n{hr}")
        return hr

    def add_table_of_contents(self, levels: range = range(2, 3)) -> TableOfContents:
        """
        A convenience method which creates a table of contents. This function
        can be called where you want to add a table of contents to your
        document. The table itself is lazy loaded, so it always captures
        all of the heading blocks regardless of where the table of contents
        is added to the document.

        .. code-block:: Python

            doc.add_table_of_contents()

        :param range levels: a range of heading levels to be included in the table of contents
        :return: the TableOfContents added to this Document
        """
        toc = TableOfContents(self, levels=levels)
        self._contents.append(toc)
        logger.debug(
            f"Added table of contents to document (unable to render until file is complete)"
        )
        return toc

    def scramble(self) -> None:
        """
        A silly method which mixes all of the blocks in this document in
        a random order.
        
        .. code-block:: Python

            doc.scramble()
        """
        random.shuffle(self._contents)
        logger.debug(f"Scrambled document")

    def dump(self, name: str, dir: str | os.PathLike = "", ext: str = "md", encoding: str = "utf-8") -> None:
        """
        Outputs the markdown document to a file. This method assumes the output directory
        is the current working directory. Any alternative directory provided will be
        made if it does not already exist. This method also assumes a file extension of md
        and a file encoding of utf-8, all of which are configurable through the method
        parameters.

        .. code-block:: Python

            doc.dump("README")

        :param str name: the name of the markdown file to output without the file extension
        :param str | os.PathLike dir: the output directory for the markdown file; defaults to ""
        :param str ext: the output file extension; defaults to "md"
        :param str encoding: the encoding to use; defaults to utf-8
        """
        pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
        with open(
            os.path.join(dir, f"{name}.{ext}"),
            "w+",
            encoding=encoding
        ) as output_file:
            output_file.write(str(self))
        logger.debug(f"Dumped document to {dir} with filename {name}.{ext}")
