from snakemd import Code


def test_code_empty():
    """
    Verifies that code block is correctly instantiated
    for empty input. Also verifies the repr
    representation of the code block. 
    """
    code = Code("")
    assert str(code) == "```generic\n\n```"
    assert repr(code) == r"Code(code='', lang='generic')"


def test_code_empty_java():
    """
    Verifies that code block is correctly instantiated
    for a custom language with empty input. Also verifies
    the repr representation of the code block.
    """
    code = Code("", lang="java")
    assert str(code) == "```java\n\n```"
    assert repr(code) == r"Code(code='', lang='java')"


def test_code_one_line():
    """
    Verifies that a code block is correctly instantiated
    given a single line of sample code. Also verifies
    the repr representation of the code block.
    """
    code = Code("print('Hello, World!')")
    assert str(code) == "```generic\nprint('Hello, World!')\n```"
    assert repr(code) == r"""Code(code="print('Hello, World!')", lang='generic')"""
    
    
def test_code_one_line_nested_single_quotes():
    """
    Verifies the same conditions as test_code_one_line()
    with the quote style swapped. This is primarily a test
    of repr.
    """
    code = Code('print("Hello, World!")')
    assert str(code) == '```generic\nprint("Hello, World!")\n```'
    assert repr(code) == r"""Code(code='print("Hello, World!")', lang='generic')"""


def test_code_two_lines():
    """
    Verifies that a code block is correctly instantiated
    given a pair of lines of sample code. Also verifies
    the repr representation of the code block.
    """
    code = Code("sum = 4 + 5\nprint(sum)")
    print(repr(code))
    assert str(code) == "```generic\nsum = 4 + 5\nprint(sum)\n```"
    assert repr(code) == r"Code(code='sum = 4 + 5\nprint(sum)', lang='generic')"


def test_code_nested():
    nested_code = Code("print('Hello, World!')", lang="python")
    code = Code(nested_code, lang="markdown")
    assert str(code) == "````markdown\n```python\nprint('Hello, World!')\n```\n````"
    assert repr(code) == r"""Code(code=Code(code="print('Hello, World!')", lang='python'), lang='markdown')"""
