from snakemd import Code, Heading, HorizontalRule, MDList, Quote, Inline, Raw

# Constructor tests


def test_quote_one_str():
    quote = Quote("Single Phrase")
    assert str(quote) == "> Single Phrase"


def test_quote_one_str_formatted():
    quote = Quote("Single Phrase\n\tLet's go!")
    assert str(quote) == "> Single Phrase\n> \tLet's go!"


def test_quote_multiple_lines():
    quote = Quote(["First", "Second", "Third"])
    assert str(quote) == "> First\n> Second\n> Third"


def test_quote_nested():
    quote = Quote(["First", Quote("Second Nested"), "Third"])
    assert str(quote) == "> First\n> \n> > Second Nested\n> \n> Third"


def test_quote_heading():
    quote = Quote([Heading("Test", 1)])
    assert str(quote) == "> # Test"


def test_quote_code():
    quote = Quote([Code("x = 7")])
    assert str(quote) == "> ```generic\n> x = 7\n> ```"


def test_quote_hr():
    quote = Quote([HorizontalRule()])
    assert str(quote) == "> ***"


def test_quote_mdlist():
    quote = Quote([MDList(["How", "Now", "Brown"])])
    assert str(quote) == "> - How\n> - Now\n> - Brown"
    

def test_quote_inline():
    quote = Quote(["[!NOTE]", Inline("...", bold=True)])
    assert str(quote) == "> [!NOTE]\n> **...**"


# Method tests


def test_repr_can_create_object():
    quote = Quote("")
    obj = eval(repr(quote))
    assert isinstance(obj, Quote)
