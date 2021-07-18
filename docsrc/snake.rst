Documentation
=====================

The snake package is a collection of submodules for generating
markdown files with Python. 

Submodules
----------

The snake package contains two main submodules: md and readme.
The readme submodule is what is used to generate the project README.
The md submodule provides all the markdown utilities needed to 
create a markdown file using Python only. 

snake.md module
---------------

The md submodule contains all of the functionality for
generating markdown files with Python. In general, library
is straightforward to use. To create a new markdown file, 
create a Document as follows:

.. code-block::Python

   from snake.md import Document
   doc = Document("MyProject")

From there, any number of document methods can be used to
generate a markdown file. For example, we can create a
header and a paragraph as follows:

.. code-block::Python

   doc.add_header("Welcome to MyProject!")
   doc.add_paragraph("Learn about MyProject here.")

Then, when you're ready to output your document, you can do
that as follows:

.. code-block::Python

   doc.output_page()

See the remainder of this section for details on all the 
functionality provided in snake.md. 

.. automodule:: snake.md
   :members:
   :undoc-members:
   :show-inheritance:

snake.readme module
-------------------

.. automodule:: snake.readme
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: snake
   :members:
   :undoc-members:
   :show-inheritance:
