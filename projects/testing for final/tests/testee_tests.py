from nose.tools import *
from testee.testee import *
import mock

def test_testing_function():
    with mock.patch('__builtins__.raw_input', return_value="123"):
        testing_function()