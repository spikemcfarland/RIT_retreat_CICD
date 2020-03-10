import pytest
from hello.hello_world import hello_world, hello_to

def test_hello_world():
    hello_world()

def test_hello_to():
    hello_to('yournamehere')