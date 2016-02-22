# -*- coding: utf-8 -*-
#
# Kinto documentation build configuration file, created by
# sphinx-quickstart on Mon Feb  2 15:08:06 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import shutil
import cliquet_docs

__HERE__ = os.path.dirname(os.path.abspath(__file__))

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify
# it

# Copy the docs from Cliquet inside these ones.
# XXX how do we copy on 2.x ?
destination = os.path.join(__HERE__, 'api', '1.x', 'cliquet')
cliquet_docs.copy_docs('api', destination)
os.remove(os.path.join(destination, 'index.rst'))
os.remove(os.path.join(destination, 'authentication.rst'))

# the versioning doc goes in api/versionning
shutil.move(os.path.join(destination, 'versioning.rst'),
            os.path.join(__HERE__, 'api', 'versioning.rst'))

# Copy the cliquet glossary
destination = os.path.join(__HERE__, 'cliquet_glossary.rst')
source = os.path.join(os.path.dirname(cliquet_docs.__file__), 'reference',
                      'glossary.rst')

with open(destination, 'wb') as d:
    with open(source, 'rb') as s:
        d.write(s.read())

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.httpdomain',
    'sphinx.ext.extlinks',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_additional_pages = {
    'index': 'indexcontent.html',
}


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Kinto'
copyright = u'2015, Mozilla Services — Da French Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.11'
# The full version, including alpha/beta/rc tags.
release = '1.11.2'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Kintodoc'


# -- Options of extlinks --------------------------------------------------

extlinks = {
    'github': ('https://github.com/%s/', ''),
    'rtd': ('http://%s.readthedocs.org', ''),
    'blog': ('http://www.servicedenuages.fr/%s', '')
}


def setup(app):
    # path relative to _static
    app.add_stylesheet('theme_overrides.css')
    app.add_javascript('piwik.js')


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'Kinto.tex', u'Kinto Documentation',
     u'Mozilla Services — Da French Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'kinto', u'Kinto Documentation',
     [u'Mozilla Services — Da French Team'], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Kinto', u'Kinto Documentation',
     u'Mozilla Services — Da French Team', 'Kinto',
     'A remote storage service with syncing and sharing abilities.',
     'Miscellaneous'),
]