pytest-pythonpath
=================

This is a py.test plugin for adding to the PYTHONPATH from the pytests.ini file before tests run.

Installation
------------

Install with pip::

    pip install pytest-pythonpath

Uninstall with pip::

    pip uninstall pytest-pythonpath

Usage
-----

Add a line in your pytest.ini file with a key of `python_paths` and provide a space seperated list of paths
you want added to the PYTHONPATH before any tests run:

    [pytest]
    python_paths = your/path/apps your/path/libs

Once this is added to your pytest.ini, you can use the py.test command as you normally would.
