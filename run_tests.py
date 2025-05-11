import unittest
from tests.homework.c_decisions import test_decisions

suite = unittest.TestLoader().loadTestsFromModule(test_decisions)
unittest.TextTestRunner().run(suite)
