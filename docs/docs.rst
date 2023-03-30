Documentation
=============

The documentation page lists out all of the relevant classes
and functions for generating markdown documents in Python.

The SnakeMD Module
-------------------

The SnakeMD module contains all of the functionality for
generating markdown files with Python. To get started, 
check out :ref:`usage_target` for information. Otherwise, 
see the rest of this document for details on all the 
functionality provided in snakemd. 

.. automodule:: snakemd
   :members:

The SnakeMD Document
-----------------------

For the average user, the document object is the only
object in the library necessary to create markdown files.
Document objects are automatically created from the
:code:`new_doc()` function of the SnakeMD module.

.. autoclass:: snakemd.generator.Document
   :members:
   :undoc-members:
   :show-inheritance:

The SnakeMD Elements
-----------------------

For users who want a little more control over how
their markdown is formatted, SnakeMD provides, 
a variety of markdown elements which you can create 
and add to an existing document using the 
:code:`add_element()` method. Elements all inherit 
from the :code:`Element` "interface" which is defined 
as follows:

.. autoclass:: snakemd.generator.Element
   :members:
   :undoc-members:
   :show-inheritance:

Because of the increase in control granted to you
by elements, there are opportunities where invalid
markdown can be generated. In an attempt to provide
a method of verifying the structure of the markdown,
a :code:`verify()`` method has been provided for all 
elements. The result of a call to :code:`verify`
is a verification object which is defined as folows:

.. autoclass:: snakemd.generator.Verification
   :members:
   :undoc-members:
   :show-inheritance:

The remainder of this section outlines the various
elements that can be added to a markdown document.

CheckBox
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.CheckBox
   :members:
   :undoc-members:
   :show-inheritance:

Header
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.Header
   :members:
   :undoc-members:
   :show-inheritance:

Heading
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.Heading
   :members:
   :undoc-members:
   :show-inheritance:

HorizontalRule
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.HorizontalRule
   :members:
   :undoc-members:
   :show-inheritance:

InlineText
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.InlineText
   :members:
   :undoc-members:
   :show-inheritance:

MDCheckList
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.MDCheckList
   :members:
   :undoc-members:
   :show-inheritance:

MDList
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.MDList
   :members:
   :undoc-members:
   :show-inheritance:

Paragraph
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.Paragraph
   :members:
   :undoc-members:
   :show-inheritance:

Table
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.Table
   :members:
   :undoc-members:
   :show-inheritance:

TableOfContents
^^^^^^^^^^^^^^^^^^^

.. autoclass:: snakemd.generator.TableOfContents
   :members:
   :undoc-members:
   :show-inheritance:
