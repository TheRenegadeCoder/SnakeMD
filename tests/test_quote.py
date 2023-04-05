from snakemd import Quote


def test_quote_one_str():
    quote = Quote("Single Phrase")
    assert str(quote) == "> Single Phrase"
    

def test_quote_multiple_lines():
    quote = Quote(["First", "Second", "Third"])
    assert str(quote) == "> First\n> Second\n> Third"
    

def test_quote_nested():
    quote = Quote([
        "First",
        Quote("Second Nested"),
        "Third"
    ])
    assert str(quote) == "> First\n> \n> > Second Nested\n> \n> Third"
