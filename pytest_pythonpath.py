import sys
import os
import site


def pytest_addoption(parser):
    # py.test has an issue where the cwd is not in the PYTHONPATH. Fix it here.
    if os.getcwd() not in sys.path:
        sys.path.insert(0, os.getcwd())
    parser.addini("python_paths", type="pathlist", help="space seperated directory paths to add to PYTHONPATH via sys.path.insert(0, path)",
                  default=[])
    parser.addini("site_dirs", type="pathlist", help="space seperated directory paths to add to PYTHONPATH via site.addsitedir(path)",
                  default=[])


def pytest_configure(config):
    print config.getini("site_dirs")
    for path in reversed(config.getini("python_paths")):
        sys.path.insert(0, str(path))
    for path in config.getini("site_dirs"):
        site.addsitedir(str(path))
