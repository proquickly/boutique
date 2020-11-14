# Hints; more coming

## Cleaning up mess!

ever pip install in wrong the wrong venv, or system python?
Here's how to undo that:

    python -m pip freeze > requirements.del
    python -m pip uninstall -y -r requirements.del

Then do

    python -m pip uninstall -y -r requirements.del

# documentation

take a look at http://www.sphinx-doc.org/