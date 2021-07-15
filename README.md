# Welcome to PyMD!

PyMD is your ticket to generating markdown in Python. To prove it to you, we've generated this entire README using PyMD. See readme.py for how it was done.

In the remainder of this document, we'll show you all of the things this library can do.

## Table of Contents

```py
def _table_of_contents(doc: Document):
    doc.add_table_of_contents()
```

1. [Table of Contents](#table-of-contents)
2. [Make a List](#make-a-list)
3. [Make a Table](#make-a-table)
4. [Testing image](#testing-image)
5. [Testing Links](#testing-links)
6. [Testing Code](#testing-code)
7. [Testing Quote](#testing-quote)

## Make a List

PyMD can make a variety of markdown lists. The two main types of lists are ordered and unordered.

### Ordered List

```py
def _ordered_list(doc: Document):
    doc.add_paragraph("""Ordered lists are lists in which the order of the 
    items matters. As a result, we number them.""")
    doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
```

Ordered lists are lists in which the order of the items matters. As a result, we number them.

1. How
2. Now
3. Brown
4. Cow

### Unordered List

```py
def _unordered_list(doc: Document):
    doc.add_paragraph("""Unordered lists are lists in which the order of the
    items does not matter. As a result, we bullet them.""")
    doc.add_unordered_list(["Look", "at", "Me", "Now"])
```

Unordered lists are lists in which the order of the items does not matter. As a result, we bullet them.

- Look
- at
- Me
- Now

### Nested Lists

```py
def _nested_list(doc: Document):
    doc.add_paragraph("""Nested lists are complex lists that contain lists.
    Currently, PyMD does not support any convenience methods to generate
    nested lists, but they can be created manually using the MDList object.""")
    doc.add_element(
        MDList([
            InlineText("Outer"),
            InlineText("List"),
            MDList([
                InlineText("Inner"),
                InlineText("List")
            ]),
            InlineText("!!!")
        ])
    )
```

Nested lists are complex lists that contain lists. Currently, PyMD does not support any convenience methods to generate nested lists, but they can be created manually using the MDList object.

- Outer
- List
  - Inner
  - List
- !!!

## Make a Table

```py
def _table(doc: Document):
    doc.add_paragraph("""Tables are sets of rows and columns which
    can display text in a grid.""")
    doc.add_table(
        ["height", "weight", "age"],
        [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
    )
```

Tables are sets of rows and columns which can display text in a grid.

height | weight | age
- | - | -
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

## Testing image

![Kitten](https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png)

## Testing Links

[Doggo](google.com)

## Testing Code

```generic
x = 5
```

## Testing Quote

> How Now Brown Cow