import os
import sys

from test_package import return_hi, hey
from hello import return_hello
from yo import return_yo
from hola import return_hola
from pow import return_pow


def test_imports_worked():
    assert "hi" == return_hi()
    assert "hey" == hey.return_hey()
    assert "hello" == return_hello()
    assert "yo" == return_yo()
    assert "hola" == return_hola()
    assert "pow" == return_pow()


def test_pythonpath_has_correct_order():
    assert sys.path[0] == os.path.join(os.getcwd())
    assert sys.path[1] == os.path.join(os.getcwd(), "test_path/apps")
    assert sys.path[2] == os.path.join(os.getcwd(), "test_path/libs")
    assert sys.path[-3] == os.path.join(os.getcwd(), "test_path/sitedir1")
    assert sys.path[-2] == os.path.join(os.getcwd(), "test_path/sitedir2")
    assert sys.path[-1] == os.path.join(os.getcwd(), "test_path/sitedir3")
