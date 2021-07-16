from snake.md import InlineText, MDList


def test_md_list_empty():
    md_list = MDList([])
    assert str(md_list) == ""

def test_md_list_one():
    md_list = MDList([InlineText("Deku")])
    assert str(md_list) == "- Deku"

def test_md_list_many():
    md_list = MDList([InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")])
    assert str(md_list) == "- Deku\n- Bakugo\n- Uraraka"

def test_md_list_man_ordered():
    md_list = MDList([InlineText("Deku"), InlineText("Bakugo"), InlineText("Uraraka")], ordered=True)
    assert str(md_list) == "1. Deku\n2. Bakugo\n3. Uraraka"
