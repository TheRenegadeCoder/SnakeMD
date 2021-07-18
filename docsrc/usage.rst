Usage
=====

SnakeMD is a Python library for building markdown documents. 
You can use it by importing the SnakeMD module into your
program directly::

    from snake import md

This way, you'll have access to all of the classes available
in the SnakeMD module. That said, the quickest way to get 
started is to import the Document class::

    from snake.md import Document

From here, you can instantiate the Document class directly::

    doc = Document("README")

The argument we pass to the constructor is the name of the 
document, and we will use that name to reader a document
called README.md::

    doc.output_page()

This will create an empty README.md file in our working
directory. Of course, if we want something more interesting,
we'll have to add some content to our document. To start,
we'll add a title to the document::

    doc.add_header("How to Use SnakeMD")
