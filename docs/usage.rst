.. _usage_target:

Usage
=====

SnakeMD is a Python library for building markdown documents. 
You can use it by importing the SnakeMD module into your
program directly:

.. code-block:: python

    import snakemd

This way, you'll have access to all of the classes available
in the SnakeMD module. From here, you can take advantage of
a handy function to create a new document:

.. code-block:: python 

    doc = snakemd.new_doc()

This will create a new :py:class:`snakemd.Document` object. Alternatively, you can 
import the Document class directly:

.. code-block:: python

    from snakemd import Document

From here, you can instantiate the Document class:

.. code-block:: python

    doc = Document()

While there is nothing in our document currently, we can render
an empty one as follows:

.. code-block:: python

    doc.dump("README")

This will create an empty README.md file in our working
directory. Of course, if we want something more interesting,
we'll have to add some content to our document. To start,
we'll add a title to the document:

.. code-block:: python 

    doc.add_heading("Why Use SnakeMD?")

From here, we can do pretty much anything we'd like. Some
quick actions might be to include a paragraph about this 
library as well as a list of reasons why you might use it:

.. code-block:: python 

    p = doc.add_paragraph(
      """
      SnakeMD is a library for generating markdown, and here's
      why you might choose to use it:
      """
    )
    doc.add_unordered_list([
        "SnakeMD makes it easy to create markdown files.",
        "SnakeMD has been used to automate documentation for The Renegade Coder projects."
    ])

One thing that's really cool about using SnakeMD is that we can
build out the structure of a document before we modify it to
include any links. For example, you might have noticed that we
saved the output of the add_paragraph() method from above. Well,
as it turns out, all of the document methods return the objects
that are generated as a result of their use. In this case, the
method returns a Paragraph object which we can modify. Here's
how we might insert a link to the docs:

.. code-block:: python 

    p.insert_link("SnakeMD", "https://snakemd.therenegadecoder.com")

And if all goes well, we can output the results by outputting the
document like before. Or, if we just need to see the results as
a string, we can convert the document to a string directly:

.. code-block:: python 

    print(doc)

And this is what we'll get:

.. code-block:: markdown

    # Why Use SnakeMD?

    [SnakeMD](https://snakemd.therenegadecoder.com) is a library for generating markdown, and here's why you might choose to use it:

    - SnakeMD makes it easy to create markdown files.
    - SnakeMD has been used to automate documentation for The Renegade Coder projects.

For completion, here is a working program to generate the document
from above in a file called README.md:

.. code-block:: python
    :linenos:

    import snakemd

    doc = snakemd.new_doc()

    doc.add_heading("Why Use SnakeMD?")
    p = doc.add_paragraph(
      """
      SnakeMD is a library for generating markdown, and here's
      why you might choose to use it:
      """
    )
    doc.add_unordered_list([
        "SnakeMD makes it easy to create markdown files.",
        "SnakeMD has been used to automate documentation for The Renegade Coder projects."
    ])
    p.insert_link("SnakeMD", "https://snakemd.therenegadecoder.com")

    doc.dump("README")

As always, feel free to check out the rest of the usage docs for all
of the ways you can make use of SnakeMD. If you find an issues, make 
sure to head over to the GitHub repo and let us know. 
