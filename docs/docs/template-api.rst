The Template API
================

While the document and element APIs are available
for folks who are already somewhat familiar with Markdown, 
a template system is slowly being developed for folks who
are looking for a bit more convenience. Ultimately, these 
folks can expect support for typical document sections such 
as tables of contents, footers, copyrights, and more. 

Template Interface
------------------

To allow for templates to be integrated with documents
seamlessly, the Template interface was developed to
inherit directly from the Element interface, just like
Block and Inline. 

.. autoclass:: snakemd.Template
   :members:
   :undoc-members:
   :show-inheritance:

Templates
---------

The template library is humble but growing. Feel free
to share your ideas for templates on the project page 
or `Discord <https://discord.gg/Jhmtj7Z>`_. Otherwise,
the existing templates can be found below.

TableOfContents
^^^^^^^^^^^^^^^

.. autoclass:: snakemd.TableOfContents
   :members:
   :undoc-members:
   :show-inheritance:
