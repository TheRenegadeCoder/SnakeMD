from snakemd import InlineText, MDList, Paragraph


def test_md_list_empty():
    md_list = MDList([])
    assert str(md_list) == ""


def test_md_list_one_inline():
    md_list = MDList([InlineText("Deku")])
    assert str(md_list) == "- Deku"


def test_md_list_one_str():
    md_list = MDList(["Deku"])
    assert str(md_list) == "- Deku"


def test_md_list_one_paragraph():
    md_list = MDList([Paragraph(["Deku"])])
    assert str(md_list) == "- Deku"


def test_md_list_many():
    md_list = MDList([InlineText("Deku"), InlineText(
        "Bakugo"), InlineText("Uraraka")])
    assert str(md_list) == "- Deku\n- Bakugo\n- Uraraka"


def test_md_list_many_mixed_syntax():
    md_list = MDList([
        "Deku", 
        InlineText("Bakugo"), 
        Paragraph(["Uraraka"])
    ])
    assert str(md_list) == "- Deku\n- Bakugo\n- Uraraka"


def test_md_list_man_ordered():
    md_list = MDList([InlineText("Deku"), InlineText(
        "Bakugo"), InlineText("Uraraka")], ordered=True)
    assert str(md_list) == "1. Deku\n2. Bakugo\n3. Uraraka"


def test_md_list_nested_unordered():
    inner_list = MDList(
        [InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")])
    outer_list = MDList(
        [InlineText("Characters"), inner_list, InlineText("Powers")])
    assert str(
        outer_list) == "- Characters\n  - Deku\n  - Bakugo\n  - Uraraka\n- Powers"

def test_md_list_nested_ordered():
    inner_list = MDList(
        [InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")], ordered=True)
    outer_list = MDList(
        [InlineText("Characters"), inner_list, InlineText("Powers")], ordered=True)
    assert str(outer_list) == "1. Characters\n   1. Deku\n   2. Bakugo\n   3. Uraraka\n2. Powers"
