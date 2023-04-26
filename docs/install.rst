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

Update Pip
^^^^^^^^^^

A common first step in building from source is to
ensure your dependency manager is up to date. In this
case, pip is typically already on systems that have
Python, so it's worth it to dust off the cobwebs with
a quick update. 

.. code-block:: batch

    C:\Users\example>python -m pip install --upgrade pip
    Requirement already satisfied: pip in ...
    Collecting pip
    Using cached pip-23.1.1-py3-none-any.whl (2.1 MB)
    Installing collected packages: pip
    Attempting uninstall: pip
        Found existing installation: pip 23.1
        Uninstalling pip-23.1:
        Successfully uninstalled pip-23.1
    Successfully installed pip-23.1.1

Clone the Sourcecode From GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From there, we can download the sourcecode by
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

Change Directories
^^^^^^^^^^^^^^^^^^

With the sourcecode downloaded, we can now navigate to
the project folder. 

.. code-block:: batch

    C:\Users\example>cd SnakeMD

    C:\Users\example\SnakeMD>     

1. Create a virtual environment

.. code-block:: batch

    C:\Users\example>python -m venv .venv

5. Activate the virtual environment

.. code-block:: batch

    C:\Users\example>.\.venv\Scripts\activate

    (.venv) C:\Users\example>

6. Install dependencies
