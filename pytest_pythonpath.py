import sys


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption('--pythonpath', action='store_true', help="update PYTHONPATH using .ini settings.")
    parser.addini("python_paths", type="pathlist", help="space seperated directory paths to add to PYTHONPATH")


def pytest_configure(config):
    if config.option.pythonpath:
        for path in config.getini("python_paths"):
            sys.path.append(str(path))
