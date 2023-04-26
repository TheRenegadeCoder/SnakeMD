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
the following workflow on Windows:

1. Clone the Sourcecode From GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To start, we can download the sourcecode by
running a git clone command. 

.. code-block:: batch

    C:\Users\example>git clone https://github.com/TheRenegadeCoder/SnakeMD.git
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

.. code-block:: batch

    C:\Users\example>cd SnakeMD

    C:\Users\example\SnakeMD>     

3. Create a Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Something we would recommend for any Python project
is to establish a virtual environment. The Python
approved virtual environment tool is venv, and it
comes standard with Python. 

.. code-block:: batch

    C:\Users\example>python -m venv .venv

4. Activate the Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the virtual environment is created, it has
to be activated. Luckily, there is a script for
that. 

.. code-block:: batch

    C:\Users\example>.\.venv\Scripts\activate

    (.venv) C:\Users\example>

If all goes well, we should see the name of the
virtual environment appended to the front of
the system path. 

5. Update Pip
^^^^^^^^^^^^^

With the virtual environment setup, it's a good idea
to upgrade the dependancy manager, pip, to the latest
version.

.. code-block:: batch

    (.venv) C:\Users\example\SnakeMD>py -m pip install --upgrade pip
    Requirement already satisfied: pip in ...
    Collecting pip
    Using cached pip-23.1.1-py3-none-any.whl (2.1 MB)
    Installing collected packages: pip
    Attempting uninstall: pip
        Found existing installation: pip 22.3.1
        Uninstalling pip-22.3.1:
        Successfully uninstalled pip-22.3.1
    Successfully installed pip-23.1.1

6. Install Build Tools
^^^^^^^^^^^^^^^^^^^^^^

While SnakeMD has no dependencies, we still make
use of a variety of third-party tools like pytest,
coverage, and markdown. These can all be found
in the requirements.txt file. 

.. code-block:: batch

    (.venv) C:\Users\example\SnakeMD>pip install -r requirements.txt
    Collecting pytest==7.2.0 (from -r requirements.txt (line 1))
    Downloading pytest-7.2.0-py3-none-any.whl (316 kB)
        ---------------------------------------- 316.8/316.8 kB 3.9 MB/s eta 0:00:00
    Collecting coverage==7.2.2 (from -r requirements.txt (line 2))
    Downloading coverage-7.2.2-cp311-cp311-win_amd64.whl (202 kB)
        ---------------------------------------- 202.9/202.9 kB 6.0 MB/s eta 0:00:00
    Collecting markdown==3.4.3 (from -r requirements.txt (line 3))
    Downloading Markdown-3.4.3-py3-none-any.whl (93 kB)
        ---------------------------------------- 93.9/93.9 kB 5.6 MB/s eta 0:00:00
    Collecting attrs>=19.2.0 (from pytest==7.2.0->-r requirements.txt (line 1))
    Downloading attrs-23.1.0-py3-none-any.whl (61 kB)
        ---------------------------------------- 61.2/61.2 kB ? eta 0:00:00
    Collecting iniconfig (from pytest==7.2.0->-r requirements.txt (line 1))
    Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
    Collecting packaging (from pytest==7.2.0->-r requirements.txt (line 1))
    Downloading packaging-23.1-py3-none-any.whl (48 kB)
        ---------------------------------------- 48.9/48.9 kB ? eta 0:00:00
    Collecting pluggy<2.0,>=0.12 (from pytest==7.2.0->-r requirements.txt (line 1))
    Downloading pluggy-1.0.0-py2.py3-none-any.whl (13 kB)
    Collecting colorama (from pytest==7.2.0->-r requirements.txt (line 1))
    Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
    Installing collected packages: pluggy, packaging, markdown, iniconfig, coverage, colorama, attrs, pytest
    Successfully installed attrs-23.1.0 colorama-0.4.6 coverage-7.2.2 iniconfig-2.0.0 markdown-3.4.3 packaging-23.1 pluggy-1.0.0 pytest-7.2.0

And to build the documentation, we can install 
the dependencies for that as well.

.. code-block:: batch

    (.venv) C:\Users\example\SnakeMD>pip install -r docs/requirements.txt
    Collecting sphinx~=5.3 (from -r docs/requirements.txt (line 1))
    Downloading sphinx-5.3.0-py3-none-any.whl (3.2 MB)
        ---------------------------------------- 3.2/3.2 MB 6.5 MB/s eta 0:00:00
    Collecting sphinx_rtd_theme~=1.1 (from -r docs/requirements.txt (line 2))
    Downloading sphinx_rtd_theme-1.2.0-py2.py3-none-any.whl (2.8 MB)
        ---------------------------------------- 2.8/2.8 MB 7.2 MB/s eta 0:00:00
    Collecting sphinx-issues~=3.0 (from -r docs/requirements.txt (line 3))
    Downloading sphinx_issues-3.0.1-py3-none-any.whl (8.2 kB)
    Requirement already satisfied: sphinxcontrib-applehelp in ...
    Requirement already satisfied: sphinxcontrib-devhelp in ...
    Requirement already satisfied: sphinxcontrib-jsmath in ...
    Requirement already satisfied: sphinxcontrib-htmlhelp>=2.0.0 in ...
    Requirement already satisfied: sphinxcontrib-serializinghtml>=1.1.5 in ...
    Requirement already satisfied: sphinxcontrib-qthelp in ...
    Requirement already satisfied: Jinja2>=3.0 in ...
    Requirement already satisfied: Pygments>=2.12 in ...
    Requirement already satisfied: docutils<0.20,>=0.14 in ...
    Requirement already satisfied: snowballstemmer>=2.0 in ...
    Requirement already satisfied: babel>=2.9 in ...
    Requirement already satisfied: alabaster<0.8,>=0.7 in ...
    Requirement already satisfied: imagesize>=1.3 in ...
    Requirement already satisfied: requests>=2.5.0 in ...
    Requirement already satisfied: packaging>=21.0 in ...
    Requirement already satisfied: colorama>=0.4.5 in ...
    Requirement already satisfied: sphinxcontrib-jquery!=3.0.0,>=2.0.0 in ...
    Requirement already satisfied: MarkupSafe>=2.0 in ...
    Requirement already satisfied: charset-normalizer<4,>=2 in ...
    Requirement already satisfied: idna<4,>=2.5 in ...
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in ...
    Requirement already satisfied: certifi>=2017.4.17 in ...
    Installing collected packages: sphinx, sphinx-issues, sphinx_rtd_theme
    Successfully installed sphinx-5.3.0 sphinx-issues-3.0.1 sphinx_rtd_theme-1.2.0

7. Verify Everything Works
^^^^^^^^^^^^^^^^^^^^^^^^^^

A quick way to check if everything worked out
is to try to run the tests.

.. code-block:: batch

    (.venv) C:\Users\example\SnakeMD>python -m pytest
    ================================================= test session starts =================================================
    platform win32 -- Python 3.11.3, pytest-7.2.0, pluggy-1.0.0
    rootdir: C:\Users\example\SnakeMD
    collected 167 items

    tests\test_code.py .....                                                                                         [  2%]
    tests\test_document.py ........................                                                                  [ 17%]
    tests\test_heading.py .................                                                                          [ 27%]
    tests\test_horizontal_rule.py .                                                                                  [ 28%]
    tests\test_inline.py ..........................................                                                  [ 53%]
    tests\test_md_list.py .........................                                                                  [ 68%]
    tests\test_module.py .                                                                                           [ 68%]
    tests\test_paragraph.py ...................                                                                      [ 80%]
    tests\test_quote.py ........                                                                                     [ 85%]
    tests\test_raw.py ....                                                                                           [ 87%]
    tests\test_table.py ..............                                                                               [ 95%]
    tests\test_table_of_contents.py .......                                                                          [100%]

    ================================================= 167 passed in 0.22s =================================================

And at the same time, why not verify that
docs can be constructed:

.. code-block:: batch

    (.venv) C:\Users\example\SnakeMD>./docs/make.bat dirhtml
    Running Sphinx v6.2.1
    making output directory... done
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

    The HTML pages are in docs\_build\dirhtml.

If you see anything like above, you're ready to 
start development.
