# -*- coding: utf-8 -*-
#
# NaluWindUtils documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 30 11:34:48 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# Are we running this on ReadTheDocs
on_rtd = os.environ.get("READTHEDOCS") == 'True'
use_breathe = tags.has("use_breathe") or on_rtd

if on_rtd:
    try:
        subprocess.call("cd ../../doxygen; doxygen Doxyfile.rtd")
    except:
        with open("index.rst", 'a') as fh:
            fh.write("\n\n %s\n\n"%os.getcwd())
        use_breathe = False

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.githubpages']

if use_breathe:
    extensions.append('breathe')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'NaluWindUtils'
copyright = u'2017, Shreyas Ananthan, Marc Henry de Frahan'
author = u'Shreyas Ananthan, Marc Henry de Frahan'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'v0.1.0'
# The full version, including alpha/beta/rc tags.
release = u'v0.1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if on_rtd:
    html_theme = 'default'
else:
    html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NaluWindUtilsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NaluWindUtils.tex', u'NaluWindUtils Documentation',
     u'Shreyas Ananthan, Marc Henry de Frahan', 'manual'),
]

latex_toplevel_sectioning = "part"


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'naluwindutils', u'NaluWindUtils Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NaluWindUtils', u'NaluWindUtils Documentation',
     author, 'NaluWindUtils', 'One line description of project.',
     'Miscellaneous'),
]

### Breathe configuration
breathe_projects = {
    'naluwindutils' : '../../doxygen/xml/'
}

breathe_default_project = "naluwindutils"

primary_domain = "cpp"

def setup(app):
    app.add_object_type("confval", "confval",
                        objname="input file parameter",
                        indextemplate="pair: %s; input file parameter")
    app.add_object_type("cmakeval", "cmakeval",
                        objname="CMake configuration value",
                        indextemplate="pair: %s; CMake configuration")

    app.add_config_value("use_breathe", use_breathe, 'env')
