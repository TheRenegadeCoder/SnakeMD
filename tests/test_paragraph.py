from snake.md import InlineText, Paragraph


def test_paragraph_empty():
    paragraph = Paragraph([])
    assert str(paragraph) == ""


def test_paragraph_one_inline():
    paragraph = Paragraph([InlineText("Single Phrase")])
    assert str(paragraph) == "Single Phrase"


def test_paragraph_one_str():
    paragraph = Paragraph("Single Phrase")
    assert str(paragraph) == "Single Phrase"


def test_paragraph_many_inline():
    paragraph = Paragraph([InlineText("How"), InlineText(
        "Now"), InlineText("Brown"), InlineText("Cow")])
    assert str(paragraph) == "HowNowBrownCow"


def test_paragraph_many_str():
    paragraph = Paragraph(["How", "Now", "Brown", "Cow"])
    assert str(paragraph) == "HowNowBrownCow"


def test_paragraph_add_inline():
    paragraph = Paragraph(
        [InlineText("How"), InlineText("Now"), InlineText("Brown")])
    paragraph.add(InlineText("Cow"))
    assert str(paragraph) == "HowNowBrownCow"


def test_paragraph_add_str():
    paragraph = Paragraph(
        [InlineText("How"), InlineText("Now"), InlineText("Brown")])
    paragraph.add("Cow")
    assert str(paragraph) == "HowNowBrownCow"


def test_insert_link():
    paragraph = Paragraph([InlineText("Check out Google!")]) \
        .insert_link("Google", "https://google.com")
    assert str(paragraph) == "Check out [Google](https://google.com)!"
