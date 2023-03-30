from snakemd import MDCheckList, Paragraph, Inline


def test_md_list_empty():
    md_list = MDCheckList([])
    assert str(md_list) == ""


def test_md_list_one_inline():
    md_list = MDCheckList([Inline("Deku")])
    assert str(md_list) == "- [ ] Deku"


def test_md_list_one_str():
    md_list = MDCheckList(["Deku"])
    assert str(md_list) == "- [ ] Deku"


def test_md_list_one_paragraph():
    md_list = MDCheckList([Paragraph(["Deku"])])
    assert str(md_list) == "- [ ] Deku"


def test_md_list_many():
    md_list = MDCheckList([Inline("Deku"), Inline(
        "Bakugo"), Inline("Uraraka")])
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_many_mixed_syntax():
    md_list = MDCheckList([
        "Deku",
        Inline("Bakugo"),
        Paragraph(["Uraraka"])
    ])
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_man_checked():
    md_list = MDCheckList([Inline("Deku"), Inline(
        "Bakugo"), Inline("Uraraka")], checked=True)
    assert str(md_list) == "- [X] Deku\n- [X] Bakugo\n- [X] Uraraka"


def test_md_list_nested_unchecked():
    inner_list = MDCheckList(
        [Inline("Deku"), Inline("Bakugo"), Inline("Uraraka")])
    outer_list = MDCheckList(
        [Inline("Characters"), inner_list, Inline("Powers")])
    assert str(
        outer_list) == "- [ ] Characters\n  - [ ] Deku\n  - [ ] Bakugo\n  - [ ] Uraraka\n- [ ] Powers"


def test_md_list_nested_checked():
    inner_list = MDCheckList(
        [Inline("Deku"), Inline("Bakugo"), Inline("Uraraka")], 
        checked=True
    )
    outer_list = MDCheckList(
        [Inline("Characters"), inner_list, Inline("Powers")], 
        checked=True
    )
    assert str(outer_list) == "- [X] Characters\n  - [X] Deku\n  - [X] Bakugo\n  - [X] Uraraka\n- [X] Powers"
