Version History
===============

.. note::
    All versions of documentation are left in the condition
    in which they were generated. At times, the navigation may
    look different than expected. 

In an effort to keep history of all the documentation
for SnakeMD, we've included all old versions below
as follows:

* `v0.9.0 <https://snakemd.therenegadecoder.com/v0.9.0/>`_
    * Added convenience function for creating new Document objects

* v0.8.1
    * Fixed an issue where nested lists did not render correctly 

* v0.8.0
    * Added range feature to Table of Contents

* v0.7.0
    * Added replace_link() method to Paragraph
    * Added various state methods to InlineText
    * Expanded testing
    * Lowered log level to INFO for verify URL errors
    * Added code coverage to build

* v0.6.0
    * Restructured api, so snakemd is the import module
    * Updated usage page to show more features
    * Fixed issue where base docs link would reroute to index.html directly

* v0.5.0
    * Added favicon to docs (:issue:`26`)
    * Added mass URL verification function to Paragraph class (:issue:`27`)
    * Expanded testing to ensure code works as expected
    * Changed behavior of insert_link() to mimic str.replace() (:issue:`19`)
    * Added a replace method to Paragraph (:issue:`27`)
    * Added plausible tracking to latest version of docs (:issue:`25`)

* v0.4.1
    * Added support for Python logging library (:issue:`22`)
    * Expanded support for strings in the Header, Paragraph, and MDList classes
    * Fixed an issue where Paragraphs would sometimes render unexpected spaces (:issue:`23`)
    * Added GitHub links to version history page
    * Added support for column alignment on tables (:issue:`4`)
    * Fixed issue where tables sometimes wouldn't pretty print properly (:issue:`5`)

* v0.3.0 [:pr:`21`]
    * Gave documentation a major overhaul
    * Added support for paragraphs in MDList
    * Added is_text() method to Paragraph
    * Fixed issue where punctuation sometimes rendered with an extra space in front

* v0.2.0 [:pr:`17`]
    * Added support for horizontal rules
    * Added automated testing through PyTest and GitHub Actions
    * Added document verification services
    * Added documentation link to README as well as info about installing the package
    * Fixed table of contents single render problem
    * Added a feature which allows users to insert links in existing paragraphs

* v0.1.0
    * Added support for links, lists, images, tables, code blocks, and quotes
    * Added a table of contents feature
