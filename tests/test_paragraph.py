from snake.md import InlineText, Paragraph


def test_paragraph_empty():
    paragraph = Paragraph([])
    assert str(paragraph) == ""

def test_paragraph_one():
    paragraph = Paragraph([InlineText("Single Phrase")])
    assert str(paragraph) == "Single Phrase"

def test_paragraph_many():
    paragraph = Paragraph([InlineText("How"), InlineText("Now"), InlineText("Brown"), InlineText("Cow")])
    assert str(paragraph) == "How Now Brown Cow"
