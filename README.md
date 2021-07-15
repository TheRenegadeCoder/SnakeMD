# Welcome to PyMD!

PyMD is your ticket to generating markdown in Python. 
    To prove it to you, we've generated this entire README using PyMD.
    See readme.py for how it was done.

In the remainder of this document, we'll show you all of
    the things this library can do.

## Table of Contents

1. [Table of Contents](#Table-of-Contents)
2. [Make a List](#Make-a-List)
3. [Make a Table](#Make-a-Table)
4. [Testing image](#Testing-image)
5. [Testing Links](#Testing-Links)
6. [Testing Code](#Testing-Code)
7. [Testing Quote](#Testing-Quote)

## Make a List

PyMD can make a variety of markdown lists. 
    The two main types of lists are ordered and unordered.

### Ordered List

Ordered lists are lists in which the order of the 
    items matters. As a result, we number them.

```py
doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
```

1. How
2. Now
3. Brown
4. Cow

### Unordered List

Unordered lists are lists in which the order of the
    items does not matter. As a result, we bullet them.

```py
doc.add_unordered_list(["Look", "at", "Me", "Now"])
```

- Look
- at
- Me
- Now

### Nested Lists

- Outer
- List
  - Inner
  - List
- !!!

## Make a Table

```py
doc.add_table(
    ["height", "weight", "age"], 
    [
        ['1', '2', '3'], 
        ['4', '5', '6'], 
        ['7', '8', '9']
    ]
)
    
```

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