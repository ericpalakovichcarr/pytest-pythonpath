import sys
import os


def pytest_addoption(parser):
    # py.test has an issue where the cwd is not in the PYTHONPATH. Fix it here.
    if os.getcwd() not in sys.path:
        sys.path.insert(0, os.getcwd())
    parser.addini("python_paths", type="pathlist", help="space seperated directory paths to add to PYTHONPATH",
                  default=[])


def pytest_configure(config):
    for path in config.getini("python_paths"):
        sys.path.append(str(path))
