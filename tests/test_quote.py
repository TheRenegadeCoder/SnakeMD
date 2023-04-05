from snakemd import Quote, Heading, Code


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
    

def test_quote_heading():
    quote = Quote([Heading("Test", 1)])
    assert str(quote) == "> # Test"
    

def test_quote_heading():
    quote = Quote([Code("x = 7")])
    assert str(quote) == "> ```generic\n> x = 7\n> ```"
