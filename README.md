# Welcome to PyMD!

PyMD is your ticket to generating markdown in Python. To prove it to you, we've generated this entire README using PyMD. See readme.py for how it was done.

In the remainder of this document, we'll show you all of the things this library can do.

## Table of Contents

Below you'll find the table of contents, but these can also be generated programatically for every markdown document.

```py
def _table_of_contents(doc: Document):
    doc.add_table_of_contents()
```

1. [Table of Contents](#table-of-contents)
2. [Paragraphs](#paragraphs)
3. [Links](#links)
4. [Images](#images)
5. [Lists](#lists)
6. [Tables](#tables)
7. [Code Blocks](#code-blocks)
8. [Quotes](#quotes)

## Paragraphs

Paragraphs are the most basic feature of any markdown file. As a result, they are very easy to create using PyMD.

**PyMD Source**

```py
def _paragraph(doc: Document):
    doc.add_paragraph("I think. Therefore, I am.")
```

**Markdown Source**

```markdown
I think. Therefore, I am.
```

**Rendered Result**

I think. Therefore, I am.

## Links

Links are targets to files or web pages and can be embedded in a Paragraph just like images using InlineText.

**PyMD Source**

```py
def _link(doc: Document):
    doc.add_element(Paragraph([
        InlineText("Learn to program with"),
        InlineText("The Renegade Coder", url="https://therenegadecoder.com")
    ]))
```

**Markdown Source**

```markdown
Learn to program with [The Renegade Coder](https://therenegadecoder.com)
```

**Rendered Result**

Learn to program with [The Renegade Coder](https://therenegadecoder.com)

## Images

Images can be added by embedding InlineText in a Paragraph.

**PyMD Source**

```py
def _image(doc: Document):
    logo = "https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png"
    doc.add_element(Paragraph([InlineText("Logo", url=logo, image=True)]))
```

**Markdown Source**

```markdown
![Logo](https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png)
```

**Rendered Result**

![Logo](https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png)

## Lists

PyMD can make a variety of markdown lists. The two main types of lists are ordered and unordered.

### Ordered List

Ordered lists are lists in which the order of the items matters. As a result, we number them.

**PyMD Source**

```py
def _ordered_list(doc: Document):
    doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
```

**Markdown Source**

```markdown
1. How
2. Now
3. Brown
4. Cow
```

**Rendered Result**

1. How
2. Now
3. Brown
4. Cow

### Unordered List

Unordered lists are lists in which the order of the items does not matter. As a result, we bullet them.

**PyMD Source**

```py
def _unordered_list(doc: Document):
    doc.add_unordered_list(["Look", "at", "Me", "Now"])
```

**Markdown Source**

```markdown
- Look
- at
- Me
- Now
```

**Rendered Result**

- Look
- at
- Me
- Now

### Nested List

Nested lists are complex lists that contain lists. Currently, PyMD does not support any convenience methods to generate nested lists, but they can be created manually using the MDList object.

**PyMD Source**

```py
def _nested_list(doc: Document):
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

**Markdown Source**

```markdown
- Outer
- List
  - Inner
  - List
- !!!
```

**Rendered Result**

- Outer
- List
  - Inner
  - List
- !!!

## Tables

Tables are sets of rows and columns which can display text in a grid. To style any of the contents of a table, consider using InlineText.

**PyMD Source**

```py
def _table(doc: Document):
    doc.add_table(
        ["height", "weight", "age"],
        [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
    )
```

**Markdown Source**

```markdown
height | weight | age
------ | ------ | ---
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
```

**Rendered Result**

height | weight | age
------ | ------ | ---
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

## Code Blocks

Code blocks are a form of structured text for sharing code snippets with syntax highlighting.

**PyMD Source**

```py
def _code(doc: Document):
    doc.add_code("x = 5", lang="py")
```

**Markdown Source**

````markdown
```py
x = 5
```
````

**Rendered Result**

```py
x = 5
```

## Quotes

Quotes are blocks of text that represent quotes from people.

```py
def _quote(doc: Document):
    doc.add_quote("How Now Brown Cow")
```

> How Now Brown Cow