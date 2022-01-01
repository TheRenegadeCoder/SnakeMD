from snakemd import CheckBox


def test_checkbox_empty():
    text = CheckBox("")
    assert str(text) == "[ ] "


def test_checkbox_str():
    text = CheckBox("Hello, World!")
    assert str(text) == "[ ] Hello, World!"

def test_checkbox_checked():
    text = CheckBox("Hello, World!", checked=True)
    assert str(text) == "[X] Hello, World!"

def test_checkbox_bold():
    text = CheckBox("Hello, World!", bold=True)
    assert str(text) == "[ ] **Hello, World!**"


def test_checkbox_bold_method():
    text = CheckBox("Hello, World!").bold()
    assert str(text) == "[ ] **Hello, World!**"


def test_checkbox_unbold_method():
    text = CheckBox("Hello, World!", bold=True).unbold()
    assert str(text) == "[ ] Hello, World!"


def test_checkbox_italics():
    text = CheckBox("Hello, World!", italics=True)
    assert str(text) == "[ ] *Hello, World!*"


def test_checkbox_italics_method():
    text = CheckBox("Hello, World!").italicize()
    assert str(text) == "[ ] *Hello, World!*"


def test_checkbox_bold_italics():
    text = CheckBox("Hello, World!", italics=True, bold=True)
    assert str(text) == "[ ] ***Hello, World!***"


def test_checkbox_bold_italics_methods():
    text = CheckBox("Hello, World!").bold().italicize()
    assert str(text) == "[ ] ***Hello, World!***"


def test_checkbox_code():
    text = CheckBox("x = 7", code=True)
    assert str(text) == "[ ] `x = 7`"


def test_checkbox_url():
    text = CheckBox("Here", url="https://google.com")
    assert str(text) == "[ ] [Here](https://google.com)"


def test_checkbox_image():
    text = CheckBox("Here", url="https://google.com", image=True)
    assert str(text) == "[ ] ![Here](https://google.com)"


def test_checkbox_image_minus_url():
    text = CheckBox("Here", image=True)
    assert str(text) == "[ ] Here"


def test_checkbox_verify_empty():
    text = CheckBox("")
    assert text.verify().passes_inspection()


def test_checkbox_verify_invalid_url():
    text = CheckBox("Bad URL Test", url="adlsfhaisu")
    assert not text.verify().passes_inspection()


def test_checkbox_verify_no_image_url():
    text = CheckBox("Bad URL Test", image=True)
    assert not text.verify().passes_inspection()


    
