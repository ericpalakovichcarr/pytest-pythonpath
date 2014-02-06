# pytest-pythonpath

This is a py.test plugin for adding to the PYTHONPATH from the pytests.ini file before tests run.

## Installation

Install with pip::

    pip install pytest-pythonpath

Uninstall with pip::

    pip uninstall pytest-pythonpath

## Usage

### Setting up the pytest.ini

Add a line in your pytest.ini file with a key of `python_paths` and provide a space seperated list of paths
you want added to the PYTHONPATH before any tests run:

    [pytest]
    python_paths = your/path/apps your/path/libs

### Running py.test with an updated PYTHONPATH

    py.test --pythonpath
