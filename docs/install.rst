Installation
============

SnakeMD is fairly hassle-free and can be installed like
most third-party libraries using pip. Only caveat worth
noting is which SnakeMD version is compatibile with your
personal version of Python. See below for more details.

Python Support
--------------

SnakeMD at its core is a dependency-free markdown generation library.
As a result, you shouldn't have to concern yourself with issues that
can arise due to dependency conflicts in your environments. However,
SnakeMD is a Python library and is constrained by the various versions
of Python. To help you navigate this, the SnakeMD documentation includes
a table of Python support as seen below. Make sure to always install a
version of SnakeMD that is tested for your version of Python.

.. csv-table::
    :file: python-support.csv
    :header-rows: 1

Basic Installation
------------------

The quick and dirty way to install SnakeMD is to use pip:

.. code-block:: shell

    pip install snakemd

If you'd like access to any pre-releases, you can also
install SnakeMD with the :code:`--pre` flag:

.. code-block:: shell

    pip install --pre snakemd

Be aware that pre-releases are not suitable for production
code.

Building From Source
--------------------

For folks who want to help with development, we generally recommend
the following workflow as of v2.1.0 (see previous version of docs
for older guides):

1. Clone the Sourcecode From GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To start, we can download the sourcecode by
running a git clone command.

.. code-block:: powershell

    PS E:\Projects> git clone https://github.com/TheRenegadeCoder/SnakeMD.git
    Cloning into 'SnakeMD'...
    remote: Enumerating objects: 1477, done.
    remote: Counting objects: 100% (63/63), done.
    remote: Compressing objects: 100% (50/50), done.
    remote: Total 1477 (delta 27), reused 27 (delta 12), pack-reused 1414
    Receiving objects: 100% (1477/1477), 6.43 MiB | 5.68 MiB/s, done.
    Resolving deltas: 100% (814/814), done.git clone https://github.com/TheRenegadeCoder/SnakeMD.git

2. Change Directories
^^^^^^^^^^^^^^^^^^^^^

With the sourcecode downloaded, we can now navigate to
the project folder.

.. code-block:: powershell

    PS E:\Projects> cd SnakeMD

    PS E:\Projects\SnakeMD>

3. Initialize the Repo With Poetry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assuming you have poetry installed, you can
immediately get up to speed by running the
install command.

.. code-block:: powershell

    PS E:\Projects> poetry install

4. Verify Everything Works
^^^^^^^^^^^^^^^^^^^^^^^^^^

A quick way to check if everything worked out
is to try to run the tests.

.. code-block:: powershell

    PS E:\Projects\SnakeMD> poetry run pytest
    ============================= test session starts ==============================
    platform win32 -- Python 3.11.3, pytest-7.3.1, pluggy-1.0.0
    rootdir: E:\Projects\SnakeMD
    configfile: pyproject.toml
    testpaths: tests
    collected 168 items

    tests\test_code.py .....                                                  [  2%]
    tests\test_document.py ........................                           [ 17%]
    tests\test_heading.py .................                                   [ 27%]
    tests\test_horizontal_rule.py .                                           [ 27%]
    tests\test_inline.py ..........................................           [ 52%]
    tests\test_md_list.py .........................                           [ 67%]
    tests\test_module.py .                                                    [ 68%]
    tests\test_paragraph.py ...................                               [ 79%]
    tests\test_quote.py ........                                              [ 84%]
    tests\test_raw.py ....                                                    [ 86%]
    tests\test_table.py ...............                                       [ 95%]
    tests\test_table_of_contents.py .......                                   [100%]

    ============================= 168 passed in 0.15s ==============================

And at the same time, why not verify that
docs can be constructed:

.. code-block:: powershell

    PS E:\Projects\SnakeMD> poetry run sphinx-build -b dirhtml docs docs/_build
    Running Sphinx v6.2.1
    loading intersphinx inventory from https://docs.python.org/3/objects.inv...
    building [mo]: targets for 0 po files that are out of date
    writing output...
    building [dirhtml]: targets for 9 source files that are out of date
    updating environment: [new config] 9 added, 0 changed, 0 removed
    reading sources... [100%] version-history
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [100%] version-history
    generating indices... genindex py-modindex done
    writing additional pages... search done
    copying static files... done
    copying extra files... done
    dumping search index in English (code: en)... done
    dumping object inventory... done
    build succeeded.

    The HTML pages are in docs\_build.

If you see anything like above, you're ready to
start development.
