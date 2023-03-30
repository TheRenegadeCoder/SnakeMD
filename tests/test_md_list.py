from snakemd import InlineText, MDList, Paragraph, CheckBox


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
        [InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")], 
        ordered=True
    )
    outer_list = MDList(
        [InlineText("Characters"), inner_list, InlineText("Powers")], 
        ordered=True
    )
    assert str(outer_list) == "1. Characters\n   1. Deku\n   2. Bakugo\n   3. Uraraka\n2. Powers"


def test_md_list_checkboxes():
    md_list = MDList([CheckBox("Deku"), CheckBox("Bakugo", checked=True), CheckBox("Uraraka")], ordered=False)
    assert str(md_list) == "- [ ] Deku\n- [X] Bakugo\n- [ ] Uraraka"


def test_md_list_one_str_unchecked():
    md_list = MDList(["Deku"], checked=False)
    assert str(md_list) == "- [ ] Deku"


def test_md_list_one_paragraph_unchecked():
    md_list = MDList([Paragraph(["Deku"])], checked=False)
    assert str(md_list) == "- [ ] Deku"


def test_md_list_many_unchecked():
    md_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=False)
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_many_mixed_syntax_unchecked():
    md_list = MDList(["Deku", "Bakugo", Paragraph(["Uraraka"])], checked=False)
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_many_checked():
    md_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=True)
    assert str(md_list) == "- [X] Deku\n- [X] Bakugo\n- [X] Uraraka"


def test_md_list_nested_unchecked():
    inner_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=False)
    outer_list = MDList(["Characters", inner_list, "Powers"], checked=False)
    assert str(outer_list) == "- [ ] Characters\n  - [ ] Deku\n  - [ ] Bakugo\n  - [ ] Uraraka\n- [ ] Powers"


def test_md_list_nested_checked():
    inner_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=True)
    outer_list = MDList(["Characters", inner_list, "Powers"], checked=True)
    assert str(outer_list) == "- [X] Characters\n  - [X] Deku\n  - [X] Bakugo\n  - [X] Uraraka\n- [X] Powers"
    
    
def test_md_list_many_checked_iterable():
    md_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=[True, True, True])
    assert str(md_list) == "- [X] Deku\n- [X] Bakugo\n- [X] Uraraka"


def test_md_list_many_checked_iterable_mixed():
    md_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=[True, False, True])
    assert str(md_list) == "- [X] Deku\n- [ ] Bakugo\n- [X] Uraraka"
    

def test_md_list_nested_checked_iterable_mixed():
    inner_list = MDList(["Deku", "Bakugo", "Uraraka"], checked=[True, True, False])
    outer_list = MDList(["Characters", inner_list, "Powers"], checked=[False, True])
    assert str(outer_list) == "- [ ] Characters\n  - [X] Deku\n  - [X] Bakugo\n  - [ ] Uraraka\n- [X] Powers"
