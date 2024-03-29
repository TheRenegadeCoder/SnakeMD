The Element API
=========================

For users who want a little more control over how
their markdown is formatted, SnakeMD provides a low-level
API constructed of elements.

Element Interface
-----------------

Broadly speaking, anything that can be rendered as markdown
is known as an element. Below is the element interface.

.. autoclass:: snakemd.Element
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

For consistency, element mutators all return self to allow
for method chaining. This is sometimes referred to as the
fluent interface pattern, and it's particularly useful
for applying a series of changes to a single element. This
design choice most obviously shines in both :class:`snakemd.Paragraph`,
which allows different aspects of the text to be replaced
over a series of chained methods, and :class:`snakemd.Inline`,
which allows inline elements to be styled over a series of
chained methods.

For practical purposes, elements cannot be constructed directly.
Instead, they are broken down into two main categories:
block and inline.

Block Elements
--------------

SnakeMD block elements borrow from the idea of block-level elements
from HTML. And because Markdown documents are constructed from a
series of blocks, users of SnakeMD can seemlessly append their own
custom blocks using the :func:`snakemd.Document.add_block` method. To make use
of this method, blocks must be imported and constructed manually,
like the following :class:`snakemd.Heading` example:

.. doctest:: block

   >>> from snakemd import Heading, new_doc
   >>> doc = new_doc()
   >>> heading = doc.add_block(Heading("Hello, World!", 2))

The remainder of this section introduces the Block interface
as well as all of the Blocks currently available for use.

Block Interface
^^^^^^^^^^^^^^^

All markdown blocks inherit from the Block interface.

.. autoclass:: snakemd.Block
   :members:
   :undoc-members:
   :show-inheritance:

Code
^^^^

.. autoclass:: snakemd.Code
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

Heading
^^^^^^^

.. autoclass:: snakemd.Heading
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

HorizontalRule
^^^^^^^^^^^^^^

.. autoclass:: snakemd.HorizontalRule
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

MDList
^^^^^^

.. autoclass:: snakemd.MDList
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

Paragraph
^^^^^^^^^

.. autoclass:: snakemd.Paragraph
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

Quote
^^^^^

.. autoclass:: snakemd.Quote
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

Raw
^^^

.. autoclass:: snakemd.Raw
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

Table
^^^^^

.. autoclass:: snakemd.Table
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__

Inline Elements
---------------

One of the benefits of creating Block elements over using the
Document methods is the control users now have
over the underlying structure and style. Instead of being
bound to the string inputs, users can provide Inline elements
directly. For example, there is often a need to link Headings.
This is not exactly possible through the Document methods as even
the returned Heading object has no support for linking. However,
with Inline elements, we can create a custom Heading to our
standards:

.. doctest:: inline

   >>> from snakemd import Heading, Inline, new_doc
   >>> doc = new_doc()
   >>> heading = doc.add_block(Heading(Inline("Hello, World!", "https://snakemd.io"), 2))

The remainder of this section introduces the Inline class.

Inline
^^^^^^

.. autoclass:: snakemd.Inline
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __str__, __repr__
