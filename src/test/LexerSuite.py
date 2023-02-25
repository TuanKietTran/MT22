import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("x abc FEEL free4all ", "abc x,,<EOF>", 101))

    def test_ac(self):
        """"""
        input = """main: function void () {}"""
        expect = """"""
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_tgh(self):
        """"""
        input = """str:string="Hello World!"""
        expect = """"""
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_t1(self):
        """"""
        input = """str:string="Hello \\nWorld!";"""
        expect = """"""
        self.assertTrue(TestLexer.test(input, expect, 104))
