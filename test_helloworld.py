from io import StringIO
from helloworld import *
import sys

def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"
