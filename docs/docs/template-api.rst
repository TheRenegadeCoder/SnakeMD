The Template API
================

While the document and element APIs are available
for folks who are already somewhat familiar with Markdown, 
a template system is slowly being developed for folks who
are looking for a bit more convenience. Ultimately, these 
folks can expect support for typical document sections such 
as tables of contents, footers, and more. 

Templates
---------

To allow for templates to be integrated with documents
seamlessly, the Template interface was developed to
inherit directly from the Element interface, just like
Block and Inline. Therefore, templates can also be 
verified. 

.. autoclass:: snakemd.Template
   :members:
   :undoc-members:
   :show-inheritance:

Below are a few existing templates. 

TableOfContents
---------------

.. autoclass:: snakemd.TableOfContents
   :members:
   :undoc-members:
   :show-inheritance:
