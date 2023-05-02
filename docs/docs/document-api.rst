The Document API
==========================

SnakeMD is designed with different types of users in mind.
The main type of user is the person who wants to design
and generate markdown quickly without worrying too much
about the format or styling of their documents. To help
this type of user, we've developed a high-level API
which consists of a single function, :func:`snakemd.new_doc()`.
This function returns a :class:`snakemd.Document` object that
is ready to be modified using any of the convenience methods available
in the :class:`snakemd.Document` class. Both the
:func:`snakemd.new_doc()` function and the :class:`snakemd.Document`
class are detailed below.

Module
------

The SnakeMD module contains all of the functionality for
generating markdown files with Python. To get started,
check out :ref:`usage_target` for quickstart sample code.

.. automodule:: snakemd
   :members:

Document
--------

.. note::
   All of the methods described in the :class:`snakemd.Document` class
   are assumed to work without any :class:`snakemd.Element` imports.
   In circumstances where methods may make use of Elements, such as
   in :meth:`snakemd.Document.add_table`, the snakemd module will be
   referenced directly in the sample source code.

For the average user, the document object is the only
object in the library necessary to create markdown files.
Document objects are automatically created from the
:func:`new_doc()` function of the SnakeMD module.

.. autoclass:: snakemd.Document
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__
