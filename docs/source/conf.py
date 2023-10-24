# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Computerprogrammeren voor het Pregymnasium'
copyright = '2023, S. Faas'
author = 'S. Faas'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_copybutton',
              'sphinx_design']

templates_path = ['_templates']
exclude_patterns = ['.venv']

language = 'nl'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_logo = "images/logo_beekvliet.png"

# -- Options for pydata_sphinx_theme
html_theme_options = {
"navbar_start": ["navbar-logo"],
"navbar_center": [],
"navbar_end": ["navbar-icon-links"],
"navbar_persistent": [],
"logo": {
    "image_light": "images/logo_beekvliet.png",
    "image_dark": "images/logo_beekvliet.png",
    "text": "Computerprogrammeren voor het Pregymnasium"
    }
}

# -- Options for sphinx-copybutton
copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"