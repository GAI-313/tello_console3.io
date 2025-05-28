# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

project = 'tello_console3'
copyright = '2025, Gai Nakatogawa'
author = 'Gai Nakatogawa'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # docstring からドキュメントを生成
    'sphinx.ext.napoleon',      # Google/NumPy スタイルの docstring を解釈
    'sphinx.ext.viewcode',      # ソースコードへのリンクを追加
    'sphinx_autodoc_typehints', # 型ヒントを表示
    'sphinx_rtd_theme',         # Read the Docs テーマ
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_member_order = 'bysource'
