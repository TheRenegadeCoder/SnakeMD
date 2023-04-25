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
