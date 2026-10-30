"""A consumer checked against the installed wheel, outside the source tree."""

import os
from pathlib import Path
from typing import Iterator

from snakemd import Document, Inline, MDList, Paragraph, Table, new_doc
from snakemd.templates import CSVTable


def use_api(csv: Path, output: Path) -> None:
    class SizedRow:
        def __iter__(self) -> Iterator[str]:
            return iter(("custom",))

        def __len__(self) -> int:
            return 1

    class BytesPath(os.PathLike[bytes]):
        def __fspath__(self) -> bytes:
            return os.fsencode(csv)

    class StringPath(os.PathLike[str]):
        def __fspath__(self) -> str:
            return str(csv)

    doc: Document = new_doc()
    Document(None)
    inline = Inline("hello", image=None, link=None)
    link: str | None = inline.get_link()
    inline.link("https://example.com").unlink().bold()
    paragraph: Paragraph = Paragraph(["hello", inline]).add(" world")
    doc.add_block(paragraph)
    doc.add_ordered_list(["one", "two"])
    MDList(["one"], checked=None)
    doc.add_table(["head"], [["cell"]], align=None)
    table = Table(["head"], body=None, align=None)
    table.add_row(["list"])
    table.add_row(("tuple",))
    table.add_row(SizedRow())
    table.add_row(cell for cell in ["generator"])
    doc.add_table_from_csv(csv)
    doc.add_table_from_csv(str(csv))
    CSVTable(csv)
    CSVTable(str(csv))
    doc.add_table_from_csv(os.fsencode(csv))
    CSVTable(os.fsencode(csv))
    doc.add_table_from_csv(BytesPath())
    doc.add_table_from_csv(StringPath())
    CSVTable(BytesPath())
    CSVTable(StringPath())
    doc.dump("example", directory=output)
    _ = link
