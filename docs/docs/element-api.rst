The Element API
=========================

For users who want a little more control over how
their markdown is formatted, SnakeMD provides a low-level
API constructed of elements.

Element Interface
-----------------

.. autoclass:: snakemd.Element
   :members:
   :undoc-members:
   :show-inheritance:

Elements are then broken down into two main types:
block and inline. 

Block Elements
--------------

SnakeMD block elements borrow from the idea of block-level elements
from HTML. And because Markdown documents are constructed from a
series of blocks, users of SnakeMD can seemlessly append their own
custom blocks using the :func:`add_block` method. To make use
of this method, blocks must be imported and constructed manually,
like the following Heading example:

.. code-block:: Python 

    from snakemd import Heading
    doc.add_block(Heading("Hello, World!", 2))

The remainder of this section introduces the Block interface
as well as all of the Blocks currently available for use. 

Block Interface
^^^^^^^^^^^^^^^

All markdown blocks inherit from the Block interface. 

.. autoclass:: snakemd.Block
   :members:
   :undoc-members:
   :show-inheritance:

Verification
^^^^^^^^^^^^

.. warning::
    The verification object and its implementation
    throughout SnakeMD is in beta, and it should
    not be used to verify production markdown. 

Because of the increase in control granted to users
by blocks, there are opportunities where invalid
markdown can be generated. In an attempt to provide
a method of verifying the structure of the markdown,
a :func:`verify` method has been provided for all 
elements. The result of a call to :func:`verify`
is a verification object which is defined as folows:

.. autoclass:: snakemd.Verification
   :members:
   :undoc-members:
   :show-inheritance:

The remainder of this page outlines the various
elements that can be added to a markdown document.

Code
^^^^

.. autoclass:: snakemd.Code
   :members:
   :undoc-members:
   :show-inheritance:

Heading
^^^^^^^

.. autoclass:: snakemd.Heading
   :members:
   :undoc-members:
   :show-inheritance:

HorizontalRule
^^^^^^^^^^^^^^

.. autoclass:: snakemd.HorizontalRule
   :members:
   :undoc-members:
   :show-inheritance:

MDList
^^^^^^

.. autoclass:: snakemd.MDList
   :members:
   :undoc-members:
   :show-inheritance:

Paragraph
^^^^^^^^^

.. autoclass:: snakemd.Paragraph
   :members:
   :undoc-members:
   :show-inheritance:

Raw
^^^

.. autoclass:: snakemd.Raw
   :members:
   :undoc-members:
   :show-inheritance:

Table
^^^^^

.. autoclass:: snakemd.Table
   :members:
   :undoc-members:
   :show-inheritance:

Inline Elements
---------------

One of the benefits of creating the Block elements directly
over using the Document methods is the control users now have
over the underlying structure and style. Now, instead of being
bound to the string inputs, users can provide Inline elements
directly. For example, maybe we want to be able to link a Heading.
This is not exactly possible through the Document methods as even
the returned Heading object has no support for linking. However,
with Inline elements, we can create a custom Heading to our
standards:

.. code-block:: Python 

    from snakemd import Heading
    doc.add_block(Heading(Inline("Hello, World!", "https://snakemd.io"), 2))

The remainder of this section introduces the Inline class.

Inline
^^^^^^

.. autoclass:: snakemd.Inline
   :members:
   :undoc-members:
   :show-inheritance:
