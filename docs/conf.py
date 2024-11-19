# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

sys.path.insert(0, os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = "SnakeMD"
copyright = "2021-2023, The Renegade Coder"
author = "The Renegade Coder"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_issues",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinxcontrib.jquery",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Adds "edit source" links
# Source: https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html
html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "TheRenegadeCoder", # Username
    "github_repo": "SnakeMD", # Repo name
    "github_version": "main", # Version
    "conf_py_path": "/docs/", # Path in the checkout to the docs root
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

github_url = "https://github.com/TheRenegadeCoder/SnakeMD"
html_logo = "_static/icon.png"
html_favicon = "_static/favicon.ico"
issues_github_path = "TheRenegadeCoder/SnakeMD"

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

html_theme_options = {"display_version": True}

# -- ReadTheDocs Configuration

# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
