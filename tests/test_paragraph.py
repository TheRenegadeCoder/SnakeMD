from snakemd import InlineText, Paragraph


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


def test_insert_link_one():
    paragraph = Paragraph([InlineText("Check out Google!")]) \
        .insert_link("Google", "https://google.com")
    assert str(paragraph) == "Check out [Google](https://google.com)!"


def test_insert_link_two_chained():
    paragraph = Paragraph(["Hello, World!"]) \
        .insert_link("Hello", "A") \
        .insert_link("World", "B")
    assert str(paragraph) == "[Hello](A), [World](B)!"


def test_insert_link_two_same():
    paragraph = Paragraph(["Hello, Hello!"]) \
        .insert_link("Hello", "A")
    assert str(paragraph) == "[Hello](A), [Hello](A)!"


def test_insert_link_two_limit():
    paragraph = Paragraph(["Hello, Hello!"]) \
        .insert_link("Hello", "A", count=1)
    assert str(paragraph) == "[Hello](A), Hello!"


def test_replace_link_one():
    paragraph = Paragraph([InlineText("Hello, World!", url="https://example.com")]) \
        .replace_link("https://example.com", "https://google.com")
    assert str(paragraph) == "[Hello, World!](https://google.com)"


def test_replace_link_two_chained():
    paragraph = Paragraph([
        InlineText("Hello", url="https://example.com"),
        ", ",
        InlineText("World", url="https://example2.com"),
        "!"
    ]) \
        .replace_link("https://example.com", "https://google.com") \
        .replace_link("https://example2.com", "https://google.com")
    assert str(
        paragraph) == "[Hello](https://google.com), [World](https://google.com)!"


def test_replace_link_two_same():
    paragraph = Paragraph([
        InlineText("Hello", url="https://example.com"),
        ", ",
        InlineText("World", url="https://example.com"),
        "!"
    ]) \
        .replace_link("https://example.com", "https://google.com")
    assert str(
        paragraph) == "[Hello](https://google.com), [World](https://google.com)!"


def test_replace_link_two_limit():
    paragraph = Paragraph([
        InlineText("Hello", url="https://example.com"),
        ", ",
        InlineText("World", url="https://example.com"),
        "!"
    ]) \
        .replace_link("https://example.com", "https://google.com", count=1)
    assert str(
        paragraph) == "[Hello](https://google.com), [World](https://example.com)!"
