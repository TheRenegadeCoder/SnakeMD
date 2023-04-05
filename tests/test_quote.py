from snakemd import Quote

def test_paragraph_one_str_quote():
    paragraph = Quote("Single Phrase")
    assert str(paragraph) == "> Single Phrase"