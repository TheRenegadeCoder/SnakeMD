from snakemd import MDCheckList, Paragraph, InlineText

def test_md_list_empty():
    md_list = MDCheckList([])
    assert str(md_list) == ""


def test_md_list_one_inline():
    md_list = MDCheckList([InlineText("Deku")])
    assert str(md_list) == "- [ ] Deku"


def test_md_list_one_str():
    md_list = MDCheckList(["Deku"])
    assert str(md_list) == "- [ ] Deku"


def test_md_list_one_paragraph():
    md_list = MDCheckList([Paragraph(["Deku"])])
    assert str(md_list) == "- [ ] Deku"


def test_md_list_many():
    md_list = MDCheckList([InlineText("Deku"), InlineText(
        "Bakugo"), InlineText("Uraraka")])
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_many_mixed_syntax():
    md_list = MDCheckList([
        "Deku", 
        InlineText("Bakugo"), 
        Paragraph(["Uraraka"])
    ])
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_man_checked():
    md_list = MDCheckList([InlineText("Deku"), InlineText(
        "Bakugo"), InlineText("Uraraka")], checked=True)
    assert str(md_list) == "- [X] Deku\n- [X] Bakugo\n- [X] Uraraka"


def test_md_list_nested_unordered():
    inner_list = MDCheckList(
        [InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")])
    outer_list = MDCheckList(
        [InlineText("Characters"), inner_list, InlineText("Powers")])
    assert str(
        outer_list) == "- [ ] Characters\n  - [ ] Deku\n  - [ ] Bakugo\n  - [ ] Uraraka\n- [ ] Powers"

def test_md_list_nested_checked():
    inner_list = MDCheckList(
        [InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")], checked=True)
    outer_list = MDCheckList(
        [InlineText("Characters"), inner_list, InlineText("Powers")], checked=True)
    assert str(outer_list) == "- [X] Characters\n  - [X] Deku\n  - [X] Bakugo\n  - [X] Uraraka\n- [X] Powers"
