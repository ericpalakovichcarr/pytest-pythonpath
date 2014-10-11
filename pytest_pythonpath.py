import os
import site
import sys


def pytest_addoption(parser):
    # py.test has an issue where the cwd is not in the PYTHONPATH. Fix it here.
    if os.getcwd() not in sys.path:
        site.addsitedir(os.getcwd())
    parser.addini("python_paths", type="pathlist", help="space seperated directory paths to add to PYTHONPATH",
                  default=[])


def pytest_load_initial_conftests(args, early_config, parser):
    for path in early_config.getini("python_paths"):
        site.addsitedir(str(path))
