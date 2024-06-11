.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/boutique.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/boutique
    .. image:: https://readthedocs.org/projects/boutique/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://boutique.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/boutique/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/boutique
    .. image:: https://img.shields.io/pypi/v/boutique.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/boutique/
    .. image:: https://img.shields.io/conda/vn/conda-forge/boutique.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/boutique
    .. image:: https://pepy.tech/badge/boutique/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/boutique
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/boutique

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

========
boutique
========


    Add a short description here!


This project layout was created with pyscaffold. Pyscaffold is not needed to run
this project (but you can use it to create projects with this layout if you like).
This project uses pyenv for manging python versions and virtual environments. The
virtual environments automatically activate due to the .python_version file.
Tis project uses tox for building. I install that with pipx (which is also how I
install pyscaffold) so I can always have it at hand).

You can do something like this (one off). Lots of really great tooling on linux and
Mac:

    pipx install pyscaffold
    pipx install tox
    brew install pyenv
    brew install sphinx-doc
    pyenv install 3.12.3 # or whatever os the bersion you want

After cloning this repo be sure to run the following commands to get started:
    pyenv virtualenv 3.12.3 boutique
    pyenv local boutique
    pip install -e .

NOTE: add dependencies to setup,cfg at ```install_requires =``` and then run
```pip install -e .``` to install them.

If using pyright be sure to add this to pyproject.toml:
[tool.pyright]
venvPath = "/Users/andy/.pyenv/versions/"  # your directory
venv = "boutique"                          # the venv name


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses and will be setup to use `pre-commit`_,
if you run the `post-clone` script.

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
