"""Consumer examples covering the public SnakeMD classes and methods.

The distribution check type-checks this outside the checkout; the examples
can also be executed against a runtime installation with a real CSV file.
"""

from pathlib import Path

from snakemd import (
    Alert,
    Block,
    Checklist,
    Code,
    CSVTable,
    Document,
    Element,
    Heading,
    HorizontalRule,
    Inline,
    MDList,
    Paragraph,
    Quote,
    Raw,
    Table,
    TableOfContents,
    Template,
    new_doc,
)


class CustomBlock(Block):
    def __str__(self) -> str:
        return "custom"

    def __repr__(self) -> str:
        return "CustomBlock()"


class CustomTemplate(Template):
    def __str__(self) -> str:
        return "custom template"

    def __repr__(self) -> str:
        return "CustomTemplate()"


def exercise_public_api(csv_path: Path, output_dir: Path) -> None:
    initial: list[Element] = [Raw("initial")]
    doc: Document = Document(initial)
    fresh: Document = new_doc()
    block: Block = doc.add_block(CustomBlock())
    raw: Raw = doc.add_raw("raw")
    heading: Heading = doc.add_heading("heading", 2)
    paragraph: Paragraph = doc.add_paragraph("hello")
    ordered: MDList = doc.add_ordered_list(["one", "two"])
    unordered: MDList = doc.add_unordered_list(["one"])
    checklist: Checklist = doc.add_checklist(["task"])
    table: Table = doc.add_table(["header"], [["cell"]], [Table.Align.LEFT])
    csv: CSVTable = doc.add_table_from_csv(csv_path)
    code: Code = doc.add_code("print('hello')", "python")
    quote: Quote = doc.add_quote("quoted")
    rule: HorizontalRule = doc.add_horizontal_rule()
    toc: TableOfContents = doc.add_table_of_contents(range(1, 4))
    alert: Alert = doc.add_alert("note", Alert.Kind.NOTE)
    elements: list[Element] = doc.get_elements()

    inline: Inline = Inline("hello")
    assert inline.is_text()
    assert not inline.is_link()
    text: str = inline.get_text()
    link: str | None = inline.get_link()
    assert text == "hello" and link is None
    styled: Inline = (
        inline.bold()
        .unbold()
        .italicize()
        .unitalicize()
        .strikethrough()
        .unstrikethrough()
        .code()
        .uncode()
        .breakline()
        .unbreakline()
        .link("https://example.com")
        .unlink()
        .reset()
    )
    assert styled is inline

    direct_code: Code = Code(code, "text")
    assert direct_code == Code(code, "text")
    direct_heading: Heading = Heading(["first", Inline("second")], 3)
    assert direct_heading.promote().demote().get_level() == 3
    heading_text: str = direct_heading.get_text()
    assert "first" in heading_text
    direct_list: MDList = MDList(["one", Inline("two"), CustomBlock()], ordered=True)
    checked: MDList = MDList(["one"], checked=True)
    assert "one" in str(direct_list) and "one" in str(checked)
    direct_paragraph: Paragraph = Paragraph(["one", Inline("two")])
    direct_paragraph.add("three").replace("one", "first")
    direct_paragraph.insert_link("first", "https://example.com")
    direct_paragraph.replace_link("https://example.com", "https://example.org")
    assert "example.org" in str(direct_paragraph)
    direct_quote: Quote = Quote(["text", CustomBlock()])
    direct_table: Table = Table(["header"], [["cell"]])
    assert direct_table.add_row(["other"]) is direct_table
    mixed_table: Table = Table(["a", "b", "c"])
    mixed_table.add_row(["text", Inline("inline"), Paragraph("paragraph")])
    assert "paragraph" in str(mixed_table)
    direct_checklist: Checklist = Checklist(["item"], checked=[True])
    direct_csv: CSVTable = CSVTable(csv_path)
    direct_toc: TableOfContents = TableOfContents()
    direct_toc.load([direct_heading])
    custom: Template = CustomTemplate()
    custom.load([direct_heading])

    doc.scramble()
    doc.dump("typed-consumer", directory=output_dir)
    assert (output_dir / "typed-consumer.md").is_file()
    assert all(
        isinstance(str(item), str)
        for item in (
            fresh,
            doc,
            block,
            raw,
            heading,
            paragraph,
            ordered,
            unordered,
            checklist,
            table,
            csv,
            code,
            quote,
            rule,
            toc,
            alert,
            direct_code,
            direct_heading,
            direct_quote,
            direct_table,
            direct_checklist,
            direct_csv,
            direct_toc,
            custom,
        )
    )
    assert elements
    assert repr(doc) and repr(direct_table)
