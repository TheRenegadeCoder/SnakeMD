import markdown
import pytest

from snakemd import Code, Heading, HorizontalRule, Inline, MDList, Paragraph

# Constructor tests (Unordered)


def test_md_list_empty():
    md_list = MDList([])
    assert str(md_list) == ""


def test_md_list_one_inline():
    md_list = MDList([Inline("Deku")])
    assert str(md_list) == "- Deku"


def test_md_list_one_str():
    md_list = MDList(["Deku"])
    assert str(md_list) == "- Deku"


def test_md_list_one_paragraph():
    md_list = MDList([Paragraph(["Deku"])])
    assert str(md_list) == "- Deku"


def test_md_list_many():
    md_list = MDList([
        Inline("Deku"),
        Inline("Bakugo"),
        Inline("Uraraka")
    ])
    assert str(md_list) == "- Deku\n- Bakugo\n- Uraraka"


def test_md_list_many_mixed_syntax():
    md_list = MDList([
        "Deku",
        Inline("Bakugo"),
        Paragraph(["Uraraka"])
    ])
    assert str(md_list) == "- Deku\n- Bakugo\n- Uraraka"


def test_md_list_nested_unordered():
    inner_list = MDList([
        Inline("Deku"),
        Inline("Bakugo"),
        Inline("Uraraka")
    ])
    outer_list = MDList([
        Inline("Characters"),
        inner_list,
        Inline("Powers")
    ])
    assert str(outer_list) == "- Characters\n  - Deku\n  - Bakugo\n  - Uraraka\n- Powers"


def test_md_list_unordered_hr():
    md_list = MDList([
        "This",
        HorizontalRule(),
        "Rules"
    ])
    assert str(md_list) == "- This\n- ***\n- Rules"
    assert markdown.markdown(str(md_list)) == "<ul>\n<li>This</li>\n<li>\n<hr />\n</li>\n<li>Rules</li>\n</ul>"


def test_md_list_unordered_code():
    md_list = MDList([
        "This",
        Code("y = 5\nx = y + 1"),
        "Rules"
    ])
    assert str(md_list) == "- This\n- ```generic\ny = 5\nx = y + 1\n```\n- Rules"


def test_md_list_unordered_heading():
    md_list = MDList([
        "This",
        Heading("Code", 1),
        "Rules"
    ])
    assert str(md_list) == "- This\n- # Code\n- Rules"


# Constructor tests (Ordered)


def test_md_list_man_ordered():
    md_list = MDList(
        [
            Inline("Deku"),
            Inline("Bakugo"),
            Inline("Uraraka")
        ],
        ordered=True
    )
    assert str(md_list) == "1. Deku\n2. Bakugo\n3. Uraraka"


def test_md_list_nested_ordered():
    inner_list = MDList(
        [
            Inline("Deku"),
            Inline("Bakugo"),
            Inline("Uraraka")
        ],
        ordered=True
    )
    outer_list = MDList(
        [
            Inline("Characters"),
            inner_list,
            Inline("Powers")
        ],
        ordered=True
    )
    assert str(outer_list) == "1. Characters\n   1. Deku\n   2. Bakugo\n   3. Uraraka\n2. Powers"


# Constructor tests (checklist)


def test_md_list_one_str_unchecked():
    md_list = MDList(
        ["Deku"],
        checked=False
    )
    assert str(md_list) == "- [ ] Deku"


def test_md_list_one_paragraph_unchecked():
    md_list = MDList(
        [Paragraph(["Deku"])],
        checked=False
    )
    assert str(md_list) == "- [ ] Deku"


def test_md_list_many_unchecked():
    md_list = MDList(
        ["Deku", "Bakugo", "Uraraka"],
        checked=False
    )
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_many_mixed_syntax_unchecked():
    md_list = MDList(
        [
            "Deku",
            "Bakugo",
            Paragraph(["Uraraka"])
        ],
        checked=False
    )
    assert str(md_list) == "- [ ] Deku\n- [ ] Bakugo\n- [ ] Uraraka"


def test_md_list_many_checked():
    md_list = MDList(
        [
            "Deku",
            "Bakugo",
            "Uraraka"
        ],
        checked=True
    )
    assert str(md_list) == "- [X] Deku\n- [X] Bakugo\n- [X] Uraraka"


def test_md_list_nested_unchecked():
    inner_list = MDList(
        [
            "Deku",
            "Bakugo",
            "Uraraka"
        ],
        checked=False
    )
    outer_list = MDList(
        [
            "Characters",
            inner_list,
            "Powers"
        ],
        checked=False
    )
    assert str(outer_list) == "- [ ] Characters\n  - [ ] Deku\n  - [ ] Bakugo\n  - [ ] Uraraka\n- [ ] Powers"


def test_md_list_nested_checked():
    inner_list = MDList(
        [
            "Deku",
            "Bakugo",
            "Uraraka"
        ],
        checked=True
    )
    outer_list = MDList(
        [
            "Characters",
            inner_list,
            "Powers"
        ],
        checked=True
    )
    assert str(outer_list) == "- [X] Characters\n  - [X] Deku\n  - [X] Bakugo\n  - [X] Uraraka\n- [X] Powers"


def test_md_list_many_checked_iterable():
    md_list = MDList(
        [
            "Deku",
            "Bakugo",
            "Uraraka"
        ],
        checked=[True, True, True]
    )
    assert str(md_list) == "- [X] Deku\n- [X] Bakugo\n- [X] Uraraka"


def test_md_list_many_checked_iterable_mixed():
    md_list = MDList(
        [
            "Deku",
            "Bakugo",
            "Uraraka"
        ],
        checked=[True, False, True]
    )
    assert str(md_list) == "- [X] Deku\n- [ ] Bakugo\n- [X] Uraraka"


def test_md_list_nested_checked_iterable_mixed():
    inner_list = MDList(
        [
            "Deku",
            "Bakugo",
            "Uraraka"
        ],
        checked=[True, True, False]
    )
    outer_list = MDList(
        [
            "Characters",
            inner_list,
            "Powers"
        ],
        checked=[False, True]
    )
    assert str(outer_list) == "- [ ] Characters\n  - [X] Deku\n  - [X] Bakugo\n  - [ ] Uraraka\n- [X] Powers"


def test_md_list_checked_exception_list():
    with pytest.raises(ValueError):
        MDList(
            [
                "Deku",
                "Bakugo",
                "Uraraka"
            ],
            checked=[True, True]
        )


def test_md_list_checked_exception_iterable():
    with pytest.raises(ValueError):
        MDList(
            [
                "Deku",
                "Bakugo",
                "Uraraka"
            ],
            checked=(x for x in [True, True])
        )


def test_md_list_nested_checked_nested_exception_list():
    with pytest.raises(ValueError):
        inner_list = MDList(
            [
                "Deku",
                "Bakugo",
                "Uraraka"
            ],
            checked=[True, True, False]
        )
        MDList(
            [
                "Characters",
                inner_list,
                "Powers"
            ],
            checked=[False, True, False]
        )
