pytest-pythonpath
=================

**NOTE:**  This plugin is obsolete as of pytest 7.0.0.  Thanks to [this PR](https://github.com/pytest-dev/pytest/pull/9134) from [Brian Okken](https://github.com/okken), you can now modify the PYTHONPATH using the `pythonpath` configuration option.  See documentation here: https://docs.pytest.org/en/7.0.x/reference/reference.html#confval-pythonpath

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
you want inserted to the beginning of the PYTHONPATH before any tests run:

    [pytest]
    python_paths = your/path/apps your/path/libs

If you'd like to have `.pth` files be processed too, use `site_dirs` instead:

    [pytest]
    site_dirs = your/path/apps your/path/libs

This will cause the `addsitedir` function to be called on each path instead of a simple `sys.path.insert(0, path)`.
Note that using the `site_dirs` will not place your specified paths in front of existing paths.

Once this is added to your pytest.ini, you can use the py.test command as you normally would.
