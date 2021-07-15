# Welcome to PyMD!

PyMD is your ticket to generating markdown in Python. 
    To prove it to you, we've generated this entire README using the library.
    See readme.py for how it was done.

In the remainder of this document, we'll show you all of
    the things this library can do.

## Make a list!

PyMD can make a variety of markdown lists. 
    The two main types of lists are ordered and unordered.

### Ordered List

```py
doc.add_ordered_list(["How", "Now", "Brown", "Cow"])
```

1. How
2. Now
3. Brown
4. Cow

### Unordered List

- Look
- at
- Me
- Now

## Testing nesting

- Outer
- List
  - Inner
  - List
- !!!

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