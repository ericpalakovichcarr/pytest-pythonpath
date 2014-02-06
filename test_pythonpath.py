from test_package import return_hi, hey
from hello import return_hello


def test_imports_worked():
    assert "hi" == return_hi()
    assert "hey" == hey.return_hey()
    assert "hello" == return_hello()
