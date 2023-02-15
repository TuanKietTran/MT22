import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_error_number_at_head(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("0ca", "Error Token 0", 102))


