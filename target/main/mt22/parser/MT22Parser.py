# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\20\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\2\2\5\2\4\6\2\3\3\2\5\b\2\f\2\b\3\2\2\2\4\13\3")
        buf.write("\2\2\2\6\r\3\2\2\2\b\t\5\6\4\2\t\n\7\2\2\3\n\3\3\2\2\2")
        buf.write("\13\f\7\3\2\2\f\5\3\2\2\2\r\16\t\2\2\2\16\7\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'expression'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'array'", "'auto'", 
                     "'bool'", "'break'", "'continue'", "'do'", "'else'", 
                     "'false'", "'float'", "'for'", "'function'", "'if'", 
                     "'inherit'", "'integer'", "'of'", "'out'", "'return'", 
                     "'string'", "'true'", "'while'", "'void'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'='", "','", "':'", "';'", 
                     "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", 
                     "'::'", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IDENT", "IntegerLiteral", 
                      "FloatingLiteral", "BooleanLiteral", "StringLiteral", 
                      "Array", "Auto", "Bool", "Break", "Continue", "Do", 
                      "Else", "False_", "Float", "For", "Function", "If", 
                      "Inherit", "Integer", "Of", "Out", "Return", "String", 
                      "True_", "While", "Void", "LeftParen", "RightParen", 
                      "LeftBracket", "RightBracket", "LeftBrace", "RightBrace", 
                      "Assign", "Comma", "Colon", "Semi", "Dot", "Plus", 
                      "Minus", "Star", "Div", "Mod", "Not", "AndAnd", "OrOr", 
                      "Equal", "NotEqual", "LessEqual", "GreaterEqual", 
                      "Less", "Greater", "Doublecolon", "Whitespace", "Newline", 
                      "BlockComment", "LineComment", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_translationUnit = 0
    RULE_expression = 1
    RULE_literal = 2

    ruleNames =  [ "translationUnit", "expression", "literal" ]

    EOF = Token.EOF
    T__0=1
    IDENT=2
    IntegerLiteral=3
    FloatingLiteral=4
    BooleanLiteral=5
    StringLiteral=6
    Array=7
    Auto=8
    Bool=9
    Break=10
    Continue=11
    Do=12
    Else=13
    False_=14
    Float=15
    For=16
    Function=17
    If=18
    Inherit=19
    Integer=20
    Of=21
    Out=22
    Return=23
    String=24
    True_=25
    While=26
    Void=27
    LeftParen=28
    RightParen=29
    LeftBracket=30
    RightBracket=31
    LeftBrace=32
    RightBrace=33
    Assign=34
    Comma=35
    Colon=36
    Semi=37
    Dot=38
    Plus=39
    Minus=40
    Star=41
    Div=42
    Mod=43
    Not=44
    AndAnd=45
    OrOr=46
    Equal=47
    NotEqual=48
    LessEqual=49
    GreaterEqual=50
    Less=51
    Greater=52
    Doublecolon=53
    Whitespace=54
    Newline=55
    BlockComment=56
    LineComment=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59
    ERROR_CHAR=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_translationUnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslationUnit" ):
                return visitor.visitTranslationUnit(self)
            else:
                return visitor.visitChildren(self)




    def translationUnit(self):

        localctx = MT22Parser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_translationUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.literal()
            self.state = 7
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(MT22Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(MT22Parser.IntegerLiteral, 0)

        def FloatingLiteral(self):
            return self.getToken(MT22Parser.FloatingLiteral, 0)

        def StringLiteral(self):
            return self.getToken(MT22Parser.StringLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(MT22Parser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.IntegerLiteral) | (1 << MT22Parser.FloatingLiteral) | (1 << MT22Parser.BooleanLiteral) | (1 << MT22Parser.StringLiteral))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





