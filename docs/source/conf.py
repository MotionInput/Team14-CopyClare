# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

from sphinx.application import Sphinx
from sphinx.util.docfields import Field

sys.path.insert(0, os.path.abspath('../../copyclare'))

# -- Project information -----------------------------------------------------

project = 'CopyClare'
copyright = '2022, MotionInput'
author = 'Adi Bozzhanov, Yan Lai, Tianhao Chen, Sricharan Sanakkayala'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinxawesome_theme',
    'recommonmark',
    'sphinx_panels',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_collapsible_definitions = True
html_awesome_headerlinks = False

html_theme_options = {
    "show_scrolltop": True,
    "show_breadcrumbs": False,
    "extra_header_links": {
        "Blog": "blog",
        "HCI": "hci",
        "Design": "design",
        "Requirements": "requirements",
        "Research": "research",
        "Implementation": "implementation",
        "Testing": "testing",
        "Documentation": "documentation",
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]


def setup(app: Sphinx) -> None:
    app.add_object_type(
        "blogfield",
        "blogfield",
        objname="blog field",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default", ),
                bodyrolename="class",
            )
        ],
    )
