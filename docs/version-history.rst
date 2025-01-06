Version History
===============

.. note::
    All versions of documentation are left in the condition
    in which they were generated. At times, the navigation may
    look different than expected.

In an effort to keep history of all the documentation
for SnakeMD, we've included all old versions below
as follows:

v2.x
----

* v2.3.0 [:pr:`168`]

  * Added a line break option to Inline text to grant a little more control over formatting

* v2.2.1 [:pr:`164`]

  * Fixed a bug where headings with special characters would not link properly in the table of contents
  * Dropped support for Python 3.8 due to deprecation
  * Added support for Python 3.12 and 3.13

* v2.2.0 [:pr:`152`, :pr:`153`, :pr:`159`]
  
  * Added documentation throughout the repo
  * Expanded testing
  * Added CSVTable Template and accompanying documentation

* v2.2.0b1 [:pr:`140`, :pr:`142`, :pr:`143`, :pr:`144`, :pr:`145`, :pr:`146`, :pr:`149`]

  * Expanded the Element requirements to include :code:`__repr__()` for developer friendly strings
  * Reworked logging system to take advantage of lazy loading and new :code:`__repr__()` methods
  * Expanded testing to verify the :code:`__repr__()` strings can be used as Python code
  * Added a handful of getter methods to dissuade folks from using protected members of classes
  * Fixed jQuery issues in documentation
  * Incorporated linting (specifically pylint) in development workflow
  * Updated changelog string for consistency on PyPI
  * Introduced concept of lazy loading for templates to allow for processing of document contents at render time
  * Broke existing behavior of a handful of utilities: 
  
    * Changed the :code:`dir` parameter to :code:`directory` for :code:`dump()` method of :code:`Document` to eliminate shadowing of built-in :code:`dir` 
    * Removed :code:`doc` parameter of :code:`TableOfContents` constructor in preference of new lazy loading system of templates

* v2.1.0 [:pr:`136`]

  * Migrated build system from setup.py to poetry

* v2.0.0 [:pr:`131`]

  * Setup code for 2023-04-14 release
  * See beta releases below for the bulk of the changes

* v2.0.0b2 [:pr:`129`, :pr:`130`]

  * Converted all code snippets in docs to doctests
  * Reworked string input for :code:`Quote` to pass directly through raw
  * Updated language around parameters in documentation to provide a list of possible inputs and their effects
  * Replaced :code:`url` parameter with :code:`link` parameter in :code:`insert_link()` method of :code:`Paragraph`

* v2.0.0b1 [:pr:`104`, :pr:`107`, :pr:`108`, :pr:`110`, :pr:`113`, :pr:`115`, :pr:`118`, :pr:`120`, :pr:`122`, :pr:`123`, :pr:`125`, :pr:`126`]

  * Removed several deprecated items:

    * Classes

      * :code:`MDCheckList`
      * :code:`CheckBox`
      * :code:`Verification`

    * Methods

      * :code:`Document.add_element()`
      * :code:`Document.add_header()`
      * :code:`Document.check_for_errors()`
      * :code:`Inline.verify_url()`
      * :code:`Paragraph.verify_urls()`
      * :code:`Paragaph.is_text()`

    * Parameters

      * :code:`name` from :code:`new_doc` and :code:`Document`
      * :code:`code` and :code:`lang` from :code:`Paragraph`
      * :code:`quote` from :code:`Paragaph`
      * :code:`render()` and :code:`verify()` from the entire repository

  * Replaced several deprecated items:

    * Classes

      * :code:`Inline` replaces :code:`InlineText`
      * :code:`Heading` replaces :code:`Header`

    * Methods

      * :code:`Inline.is_link()` replaces :code:`Inline.is_url()`
      * :code:`Document.dump()` replaces :code:`Document.output_page()`

    * Parameters

      * :code:`link` replaces :code:`url` in :code:`Inline`

  * Added several new features:

    * Included a :code:`Quote` block which allows for quote nesting
    * Incorporated :code:`ValueError` exceptions in various class constructors
    * Started a resources page in documentation
    * Created a requirements file at the root of the repo to aid in development

  * Improved various aspects of the repo:

    * Expanded testing to 163 tests for 100% coverage
    * Clarified design of :code:`Inline` to highlight precedence
    * Cleaned up documentation of pre-release version directives
    * Expanded types of inputs on various classes for quality of life
    * Changed behavior of horizontal rule to avoid clashes with list items
    * Fixed bugs in logs and expanded logging capabilities
    * Standardized docstring formatting
    * Updated README automation to use latest features

.. note::

    The gap between v0.x and v2.x is not a mistake. Initial
    development of SnakeMD used v1.x versions, which contaminated
    the PyPI repository. To avoid failed releases due to
    version clashes, all v1.x versions have been deleted,
    and the project has jumped straight to v2.x. Consider
    v2.x to be the official release of the module. Anything
    prior to v2.x is considered a pre-release.

v0.x
----

* v0.15.0 [:pr:`97`, :pr:`98`, :pr:`99`, :pr:`101`]

  * Moved README generation code to repo root as a script
  * Expanded Heading constructor to support list of strings and Inline objects
  * Migrated code block support from Paragraph class into new Code class

* v0.14.0 [:pr:`84`, :pr:`86`, :pr:`89`, :pr:`90`, :pr:`91`, :pr:`95`]

  * Added Raw block for user formatted text
  * Replaced InlineText with Inline
  * Added Block and Inline classes
  * Deprecated MDCheckList and CheckBox
  * Replaced render with bulit-in str method

* v0.13.0 [:pr:`71`, :pr:`74`, :pr:`76`, :pr:`78`, :pr:`80`, :pr:`82`]

  * Created a replacement method for output_page called dump
  * Renamed Header class to Heading
  * Included deprecation warnings for both output_page and header as well as others affected

* v0.12.0 [:pr:`65`, :pr:`66`]

  * Added support for table generation on-the-fly (:issue:`64`)
  * Reworked documentation to include proper headings and organization
  * Added support for strikethrough on InlineText elements (:issue:`58`)

* v0.11.0 [:pr:`61`, :pr:`62`]

  * Added support for table indentation

* v0.10.1 [:pr:`59`]

  * Enforced UTF-8 encoding in the output_page method (:issue:`54`)

* v0.10.0 [:pr:`55`, :pr:`56`, :pr:`57`]

  * Added the CheckBox class for creating checkboxes
  * Added the MDCheckList class for creating lists of checkboxes
  * Added a Document method for implementing easy checklists
  * Updated README to include a new section on checklists

* v0.9.3 [:pr:`50`, :pr:`49`]

  * Added multiple versions of Python testing
  * Restricted package to Python version 3.8+
  * Added Markdown linting for main README

* v0.9.0 [:pr:`47`, :pr:`46`, :pr:`45`]

  * Added convenience function for creating new Document objects (:issue:`40`)
  * Ported documentation to Read the Docs (:issue:`43`)

* v0.8.1

  * Fixed an issue where nested lists did not render correctly

* v0.8.0

  * Added range feature to Table of Contents (:issue:`41`)

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
