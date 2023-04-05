# Welcome to SnakeMD

SnakeMD is your ticket to generating Markdown in Python. To prove it to you, we've generated this entire README using SnakeMD. See readme.py for how it was done. To get started, download and install SnakeMD:

```shell
pip install snakemd
```

In the remainder of this document, we'll show you all of the things this library can do. For more information, check out the official documentation [here](https://snakemd.therenegadecoder.com).

## Table of Contents

Below you'll find the table of contents, but these can also be generated programatically for every Markdown document. As of v0.8.0, you can also specify which types of headings are included in the table of contents.

```py
def _table_of_contents(doc: Document):
    doc.add_table_of_contents(range(2, 4))
```

1. [Table of Contents](#table-of-contents)
2. [Paragraphs](#paragraphs)
3. [Links](#links)
4. [Images](#images)
5. [Lists](#lists)
   1. [Ordered List](#ordered-list)
   2. [Unordered List](#unordered-list)
   3. [Checklist](#checklist)
   4. [Nested List](#nested-list)
6. [Tables](#tables)
7. [Code Blocks](#code-blocks)
8. [Quotes](#quotes)
9. [Horizontal Rule](#horizontal-rule)

## Paragraphs

Paragraphs are the most basic feature of any Markdown file. As a result, they are very easy to create using SnakeMD.

_SnakeMD Source_

```py
def _paragraph(doc: Document):
    doc.add_paragraph("I think. Therefore, I am.")
```

_Markdown Source_

```markdown
I think. Therefore, I am.
```

_Rendered Result_

I think. Therefore, I am.

## Links

Links are targets to files or web pages and can be embedded in a Paragraph in a variety of ways. As of v0.2.0, we're able to add links to existing paragraphs using the insert_link() method. Even better, in v0.4.0, we can chain these insert_link() calls.

_SnakeMD Source_

```py
def _insert_link(doc: Document):
    doc.add_paragraph("Learn to program with The Renegade Coder (@RenegadeCoder94).") \
        .insert_link("The Renegade Coder", "https://therenegadecoder.com") \
        .insert_link("@RenegadeCoder94", "https://twitter.com/RenegadeCoder94")
```

_Markdown Source_

```markdown
Learn to program with [The Renegade Coder](https://therenegadecoder.com) ([@RenegadeCoder94](https://twitter.com/RenegadeCoder94)).
```

_Rendered Result_

Learn to program with [The Renegade Coder](https://therenegadecoder.com) ([@RenegadeCoder94](https://twitter.com/RenegadeCoder94)).

## Images

Images can be added by embedding InlineText in a Paragraph.

_SnakeMD Source_

```py
def _image(doc: Document):
    logo = "https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png"
    doc.add_block(Paragraph([Inline("Logo", image=logo)]))
```

_Markdown Source_

```markdown
![Logo](https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png)
```

_Rendered Result_

![Logo](https://therenegadecoder.com/wp-content/uploads/2020/05/header-logo-without-tag-300x75.png)

## Lists

SnakeMD can make a variety of Markdown lists. The three main types of lists are ordered, unordered, and checked.

### Ordered List

Ordered lists are lists in which the order of the items matters. As a result, we number them.

_SnakeMD Source_

```py
def _ordered_list(doc: Document):
    doc.add_ordered_list(["Deku", "Bakugo", "Uraraka", "Tsuyu"])
```

_Markdown Source_

```markdown
1. Deku
2. Bakugo
3. Uraraka
4. Tsuyu
```

_Rendered Result_

1. Deku
2. Bakugo
3. Uraraka
4. Tsuyu

### Unordered List

Unordered lists are lists in which the order of the items does not matter. As a result, we bullet them.

_SnakeMD Source_

```py
def _unordered_list(doc: Document):
    doc.add_unordered_list(["Crosby", "Malkin", "Lemieux"])
```

_Markdown Source_

```markdown
- Crosby
- Malkin
- Lemieux
```

_Rendered Result_

- Crosby
- Malkin
- Lemieux

### Checklist

Checklists are lists in which the items themselves can be checked on and off. This feature is new as of v0.10.0.

_SnakeMD Source_

```py
def _checklist(doc: Document):
    doc.add_checklist(
        [
            "Pass the puck",
            "Shoot the puck",
            "Score a goal"
        ]
    )
```

_Markdown Source_

```markdown
- [ ] Pass the puck
- [ ] Shoot the puck
- [ ] Score a goal
```

_Rendered Result_

- [ ] Pass the puck
- [ ] Shoot the puck
- [ ] Score a goal

### Nested List

Nested lists are complex lists that contain lists. Currently, SnakeMD does not support any convenience methods to generate nested lists, but they can be created manually using the MDList object. As of v0.4.0, you can forego the InlineText elements if you don't need them.

_SnakeMD Source_

```py
def _nested_list(doc: Document):
    doc.add_block(
        MDList([
            "Apples",
            Inline("Onions"),
            MDList([
                "Sweet",
                "Red"
            ]),
            Paragraph(["This is the end of the list!"])
        ])
    )
```

_Markdown Source_

```markdown
- Apples
- Onions
  - Sweet
  - Red
- This is the end of the list!
```

_Rendered Result_

- Apples
- Onions
  - Sweet
  - Red
- This is the end of the list!

## Tables

Tables are sets of rows and columns which can display text in a grid. To style any of the contents of a table, consider using Paragraph or InlineText. As of v0.4.0, you can also align the columns of the table using the Table.Align enum.

_SnakeMD Source_

```py
def _table(doc: Document):
    doc.add_table(
        ["Height (cm)", "Weight (kg)", "Age (y)"],
        [
            ['150', '70', '21'],
            ['164', '75', '19'],
            ['181', '87', '40']
        ],
        [Table.Align.LEFT, Table.Align.CENTER, Table.Align.RIGHT],
        0
    )
```

_Markdown Source_

```markdown
| Height (cm) | Weight (kg) | Age (y) |
| :---------- | :---------: | ------: |
| 150         | 70          | 21      |
| 164         | 75          | 19      |
| 181         | 87          | 40      |
```

_Rendered Result_

| Height (cm) | Weight (kg) | Age (y) |
| :---------- | :---------: | ------: |
| 150         | 70          | 21      |
| 164         | 75          | 19      |
| 181         | 87          | 40      |

## Code Blocks

Code blocks are a form of structured text for sharing code snippets with syntax highlighting.

_SnakeMD Source_

```py
def _code(doc: Document):
    doc.add_code("x = 5", lang="py")
```

_Markdown Source_

````markdown
```py
x = 5
```
````

_Rendered Result_

```py
x = 5
```

## Quotes

Quotes are blocks of text that represent quotes from people.

_SnakeMD Source_

```py
def _quote(doc: Document):
    doc.add_quote("How Now Brown Cow")
```

_Markdown Source_

```markdown
> How Now Brown Cow
```

_Rendered Result_

> How Now Brown Cow

## Horizontal Rule

Horizontal Rules are visible dividers in a document.

_SnakeMD Source_

```py
def _horizontal_rule(doc: Document):
    doc.add_horizontal_rule()
```

_Markdown Source_

```markdown
***
```

_Rendered Result_

***