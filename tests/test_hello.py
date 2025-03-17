from src.hello import hello_f
import pytest

def test_hello_f (capsys):
    hello_f()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
    assert captured.err == ""
if __name__ == '__main__':
    pytest.main([__file__,"-v", "-s"]) # run tests (without stdout/stderr capture) when thisscript is run