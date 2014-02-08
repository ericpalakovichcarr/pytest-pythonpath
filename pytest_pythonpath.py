import sys


def pytest_addoption(parser):
    parser.addini("python_paths", type="pathlist", help="space seperated directory paths to add to PYTHONPATH",
                  default=[])


def pytest_configure(config):
    for path in config.getini("python_paths"):
        sys.path.append(str(path))
