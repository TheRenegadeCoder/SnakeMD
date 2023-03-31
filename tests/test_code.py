from snakemd import Code


def test_code_empty():
    code = Code("")
    assert str(code) == "```generic\n\n```"


def test_code_empty_java():
    code = Code("", lang="java")
    assert str(code) == "```java\n\n```"


def test_code_one_line():
    code = Code("print('Hello, World!')")
    assert str(code) == "```generic\nprint('Hello, World!')\n```"


def test_code_two_lines():
    code = Code("sum = 4 + 5\nprint(sum)")
    assert str(code) == "```generic\nsum = 4 + 5\nprint(sum)\n```"


def test_code_nested():
    nested_code = Code("print('Hello, World!')", lang="python")
    code = Code(nested_code, lang="markdown")
    assert str(code) == "````markdown\n```python\nprint('Hello, World!')\n```\n````"
