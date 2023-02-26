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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u018b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\3\2\5\2Y\n\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3a\n\3\3\4\3\4\5\4e\n\4\3\5\3\5")
        buf.write("\5\5i\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7")
        buf.write("u\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u0083\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u008a\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u0091\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u009e\n\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\5\r\u00a5\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00ac")
        buf.write("\n\16\3\17\3\17\5\17\u00b0\n\17\3\17\3\17\5\17\u00b4\n")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00be")
        buf.write("\n\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\7\22\u00c7\n")
        buf.write("\22\f\22\16\22\u00ca\13\22\5\22\u00cc\n\22\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u00d7\n\23\3\24")
        buf.write("\3\24\3\24\5\24\u00dc\n\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u00e4\n\25\3\26\3\26\5\26\u00e8\n\26\3\27\3\27")
        buf.write("\5\27\u00ec\n\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u00f8\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u010e\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\5\36\u0121\n\36\3\36\5\36\u0124\n\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u012d\n\37\3 \3")
        buf.write(" \3 \3 \3 \5 \u0134\n \3!\3!\3!\3!\3!\5!\u013b\n!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\5\"\u0142\n\"\3#\3#\3#\3#\3#\3#\7#\u014a")
        buf.write("\n#\f#\16#\u014d\13#\3$\3$\3$\3$\3$\3$\7$\u0155\n$\f$")
        buf.write("\16$\u0158\13$\3%\3%\3%\3%\3%\5%\u015f\n%\3&\3&\3&\5&")
        buf.write("\u0164\n&\3\'\3\'\3\'\5\'\u0169\n\'\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\7(\u0173\n(\f(\16(\u0176\13(\3)\3)\3)\3)\3)\3)")
        buf.write("\3)\5)\u017f\n)\3*\3*\3*\3*\5*\u0185\n*\3*\3*\3+\3+\3")
        buf.write("+\2\5DFN,\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPRT\2\t\6\2\t\t\17\17\24\24")
        buf.write("\30\30\3\2\n\13\3\2/\64\3\2-.\3\2\'(\3\2)+\3\2\3\6\2\u018d")
        buf.write("\2X\3\2\2\2\4`\3\2\2\2\6d\3\2\2\2\bh\3\2\2\2\nl\3\2\2")
        buf.write("\2\ft\3\2\2\2\16\u0082\3\2\2\2\20\u0089\3\2\2\2\22\u0090")
        buf.write("\3\2\2\2\24\u0092\3\2\2\2\26\u009a\3\2\2\2\30\u00a4\3")
        buf.write("\2\2\2\32\u00ab\3\2\2\2\34\u00af\3\2\2\2\36\u00bd\3\2")
        buf.write("\2\2 \u00bf\3\2\2\2\"\u00c1\3\2\2\2$\u00d6\3\2\2\2&\u00d8")
        buf.write("\3\2\2\2(\u00e3\3\2\2\2*\u00e7\3\2\2\2,\u00eb\3\2\2\2")
        buf.write(".\u00ef\3\2\2\2\60\u010d\3\2\2\2\62\u010f\3\2\2\2\64\u0115")
        buf.write("\3\2\2\2\66\u0119\3\2\2\28\u011b\3\2\2\2:\u0123\3\2\2")
        buf.write("\2<\u012c\3\2\2\2>\u0133\3\2\2\2@\u013a\3\2\2\2B\u0141")
        buf.write("\3\2\2\2D\u0143\3\2\2\2F\u014e\3\2\2\2H\u015e\3\2\2\2")
        buf.write("J\u0163\3\2\2\2L\u0168\3\2\2\2N\u016a\3\2\2\2P\u017e\3")
        buf.write("\2\2\2R\u0180\3\2\2\2T\u0188\3\2\2\2VY\5\4\3\2WY\3\2\2")
        buf.write("\2XV\3\2\2\2XW\3\2\2\2YZ\3\2\2\2Z[\7\2\2\3[\3\3\2\2\2")
        buf.write("\\]\5\6\4\2]^\5\4\3\2^a\3\2\2\2_a\5\6\4\2`\\\3\2\2\2`")
        buf.write("_\3\2\2\2a\5\3\2\2\2be\5\24\13\2ce\5\b\5\2db\3\2\2\2d")
        buf.write("c\3\2\2\2e\7\3\2\2\2fi\5\n\6\2gi\5\16\b\2hf\3\2\2\2hg")
        buf.write("\3\2\2\2ij\3\2\2\2jk\7%\2\2k\t\3\2\2\2lm\5\f\7\2mn\7$")
        buf.write("\2\2no\5\36\20\2o\13\3\2\2\2pq\7\66\2\2qr\7#\2\2ru\5\f")
        buf.write("\7\2su\7\66\2\2tp\3\2\2\2ts\3\2\2\2u\r\3\2\2\2vw\7\66")
        buf.write("\2\2wx\7#\2\2xy\5\16\b\2yz\7#\2\2z{\5\20\t\2{\u0083\3")
        buf.write("\2\2\2|}\7\66\2\2}~\7$\2\2~\177\5\36\20\2\177\u0080\7")
        buf.write("\"\2\2\u0080\u0081\5\20\t\2\u0081\u0083\3\2\2\2\u0082")
        buf.write("v\3\2\2\2\u0082|\3\2\2\2\u0083\17\3\2\2\2\u0084\u008a")
        buf.write("\5> \2\u0085\u0086\7 \2\2\u0086\u0087\5\22\n\2\u0087\u0088")
        buf.write("\7!\2\2\u0088\u008a\3\2\2\2\u0089\u0084\3\2\2\2\u0089")
        buf.write("\u0085\3\2\2\2\u008a\21\3\2\2\2\u008b\u008c\5\20\t\2\u008c")
        buf.write("\u008d\7#\2\2\u008d\u008e\5\22\n\2\u008e\u0091\3\2\2\2")
        buf.write("\u008f\u0091\5\20\t\2\u0090\u008b\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\23\3\2\2\2\u0092\u0093\7\66\2\2\u0093\u0094")
        buf.write("\7$\2\2\u0094\u0095\7\21\2\2\u0095\u0096\5\36\20\2\u0096")
        buf.write("\u0097\5\26\f\2\u0097\u0098\5\30\r\2\u0098\u0099\5&\24")
        buf.write("\2\u0099\25\3\2\2\2\u009a\u009d\7\34\2\2\u009b\u009e\5")
        buf.write("\32\16\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7\35\2")
        buf.write("\2\u00a0\27\3\2\2\2\u00a1\u00a2\7\23\2\2\u00a2\u00a5\7")
        buf.write("\66\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\31\3\2\2\2\u00a6\u00a7\5\34\17\2")
        buf.write("\u00a7\u00a8\7#\2\2\u00a8\u00a9\5\32\16\2\u00a9\u00ac")
        buf.write("\3\2\2\2\u00aa\u00ac\5\34\17\2\u00ab\u00a6\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\33\3\2\2\2\u00ad\u00b0\7\23\2\2\u00ae")
        buf.write("\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b3\3\2\2\2\u00b1\u00b4\7\26\2\2\u00b2\u00b4")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b6\7\66\2\2\u00b6\u00b7\7$\2\2")
        buf.write("\u00b7\u00b8\5\36\20\2\u00b8\35\3\2\2\2\u00b9\u00be\5")
        buf.write(" \21\2\u00ba\u00be\7\33\2\2\u00bb\u00be\5\"\22\2\u00bc")
        buf.write("\u00be\7\b\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\37\3\2")
        buf.write("\2\2\u00bf\u00c0\t\2\2\2\u00c0!\3\2\2\2\u00c1\u00c2\7")
        buf.write("\7\2\2\u00c2\u00cb\7\36\2\2\u00c3\u00c8\7\3\2\2\u00c4")
        buf.write("\u00c5\7#\2\2\u00c5\u00c7\7\3\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3")
        buf.write("\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00c3")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\7\37\2\2\u00ce\u00cf\7\25\2\2\u00cf\u00d0\5 \21")
        buf.write("\2\u00d0#\3\2\2\2\u00d1\u00d7\5&\24\2\u00d2\u00d7\5,\27")
        buf.write("\2\u00d3\u00d7\5.\30\2\u00d4\u00d7\5\60\31\2\u00d5\u00d7")
        buf.write("\5:\36\2\u00d6\u00d1\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d6")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7%\3\2\2\2\u00d8\u00db\7 \2\2\u00d9\u00dc\5(\25\2")
        buf.write("\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7!\2\2\u00de\'")
        buf.write("\3\2\2\2\u00df\u00e0\5*\26\2\u00e0\u00e1\5(\25\2\u00e1")
        buf.write("\u00e4\3\2\2\2\u00e2\u00e4\5*\26\2\u00e3\u00df\3\2\2\2")
        buf.write("\u00e3\u00e2\3\2\2\2\u00e4)\3\2\2\2\u00e5\u00e8\5$\23")
        buf.write("\2\u00e6\u00e8\5\b\5\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8+\3\2\2\2\u00e9\u00ec\5<\37\2\u00ea\u00ec")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ee\7%\2\2\u00ee-\3\2\2\2\u00ef")
        buf.write("\u00f0\7\22\2\2\u00f0\u00f1\7\34\2\2\u00f1\u00f2\5<\37")
        buf.write("\2\u00f2\u00f3\7\35\2\2\u00f3\u00f7\5$\23\2\u00f4\u00f5")
        buf.write("\7\r\2\2\u00f5\u00f8\5$\23\2\u00f6\u00f8\3\2\2\2\u00f7")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8/\3\2\2\2\u00f9")
        buf.write("\u00fa\7\32\2\2\u00fa\u00fb\7\34\2\2\u00fb\u00fc\5<\37")
        buf.write("\2\u00fc\u00fd\7\35\2\2\u00fd\u00fe\5$\23\2\u00fe\u010e")
        buf.write("\3\2\2\2\u00ff\u0100\7\f\2\2\u0100\u0101\5$\23\2\u0101")
        buf.write("\u0102\7\32\2\2\u0102\u0103\7\34\2\2\u0103\u0104\5<\37")
        buf.write("\2\u0104\u0105\7\35\2\2\u0105\u0106\7%\2\2\u0106\u010e")
        buf.write("\3\2\2\2\u0107\u0108\7\20\2\2\u0108\u0109\7\34\2\2\u0109")
        buf.write("\u010a\5\62\32\2\u010a\u010b\7\35\2\2\u010b\u010c\5$\23")
        buf.write("\2\u010c\u010e\3\2\2\2\u010d\u00f9\3\2\2\2\u010d\u00ff")
        buf.write("\3\2\2\2\u010d\u0107\3\2\2\2\u010e\61\3\2\2\2\u010f\u0110")
        buf.write("\5\64\33\2\u0110\u0111\7#\2\2\u0111\u0112\5\66\34\2\u0112")
        buf.write("\u0113\7#\2\2\u0113\u0114\58\35\2\u0114\63\3\2\2\2\u0115")
        buf.write("\u0116\7\66\2\2\u0116\u0117\7\"\2\2\u0117\u0118\5<\37")
        buf.write("\2\u0118\65\3\2\2\2\u0119\u011a\5B\"\2\u011a\67\3\2\2")
        buf.write("\2\u011b\u011c\5@!\2\u011c9\3\2\2\2\u011d\u0120\7\27\2")
        buf.write("\2\u011e\u0121\5<\37\2\u011f\u0121\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0124\t\3\2\2\u0123\u011d\3\2\2\2\u0123\u0122\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\u0126\7%\2\2\u0126;\3\2\2\2")
        buf.write("\u0127\u0128\5> \2\u0128\u0129\7#\2\2\u0129\u012a\5<\37")
        buf.write("\2\u012a\u012d\3\2\2\2\u012b\u012d\5> \2\u012c\u0127\3")
        buf.write("\2\2\2\u012c\u012b\3\2\2\2\u012d=\3\2\2\2\u012e\u0134")
        buf.write("\5@!\2\u012f\u0130\5J&\2\u0130\u0131\7\"\2\2\u0131\u0132")
        buf.write("\5> \2\u0132\u0134\3\2\2\2\u0133\u012e\3\2\2\2\u0133\u012f")
        buf.write("\3\2\2\2\u0134?\3\2\2\2\u0135\u0136\5B\"\2\u0136\u0137")
        buf.write("\7\65\2\2\u0137\u0138\5B\"\2\u0138\u013b\3\2\2\2\u0139")
        buf.write("\u013b\5B\"\2\u013a\u0135\3\2\2\2\u013a\u0139\3\2\2\2")
        buf.write("\u013bA\3\2\2\2\u013c\u013d\5D#\2\u013d\u013e\t\4\2\2")
        buf.write("\u013e\u013f\5D#\2\u013f\u0142\3\2\2\2\u0140\u0142\5D")
        buf.write("#\2\u0141\u013c\3\2\2\2\u0141\u0140\3\2\2\2\u0142C\3\2")
        buf.write("\2\2\u0143\u0144\b#\1\2\u0144\u0145\5F$\2\u0145\u014b")
        buf.write("\3\2\2\2\u0146\u0147\f\4\2\2\u0147\u0148\t\5\2\2\u0148")
        buf.write("\u014a\5F$\2\u0149\u0146\3\2\2\2\u014a\u014d\3\2\2\2\u014b")
        buf.write("\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014cE\3\2\2\2\u014d")
        buf.write("\u014b\3\2\2\2\u014e\u014f\b$\1\2\u014f\u0150\5H%\2\u0150")
        buf.write("\u0156\3\2\2\2\u0151\u0152\f\4\2\2\u0152\u0153\t\6\2\2")
        buf.write("\u0153\u0155\5H%\2\u0154\u0151\3\2\2\2\u0155\u0158\3\2")
        buf.write("\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157G\3")
        buf.write("\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\5J&\2\u015a\u015b")
        buf.write("\t\7\2\2\u015b\u015c\5H%\2\u015c\u015f\3\2\2\2\u015d\u015f")
        buf.write("\5J&\2\u015e\u0159\3\2\2\2\u015e\u015d\3\2\2\2\u015fI")
        buf.write("\3\2\2\2\u0160\u0161\7,\2\2\u0161\u0164\5J&\2\u0162\u0164")
        buf.write("\5L\'\2\u0163\u0160\3\2\2\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("K\3\2\2\2\u0165\u0166\7(\2\2\u0166\u0169\5L\'\2\u0167")
        buf.write("\u0169\5N(\2\u0168\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("M\3\2\2\2\u016a\u016b\b(\1\2\u016b\u016c\5P)\2\u016c\u0174")
        buf.write("\3\2\2\2\u016d\u016e\f\3\2\2\u016e\u016f\7\36\2\2\u016f")
        buf.write("\u0170\5<\37\2\u0170\u0171\7\37\2\2\u0171\u0173\3\2\2")
        buf.write("\2\u0172\u016d\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175O\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u017f\5T+\2\u0178\u017f\7\66\2\2\u0179")
        buf.write("\u017a\7\34\2\2\u017a\u017b\5<\37\2\u017b\u017c\7\35\2")
        buf.write("\2\u017c\u017f\3\2\2\2\u017d\u017f\5R*\2\u017e\u0177\3")
        buf.write("\2\2\2\u017e\u0178\3\2\2\2\u017e\u0179\3\2\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017fQ\3\2\2\2\u0180\u0181\7\66\2\2\u0181\u0184")
        buf.write("\7\34\2\2\u0182\u0185\5<\37\2\u0183\u0185\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0187\7\35\2\2\u0187S\3\2\2\2\u0188\u0189\t\b\2")
        buf.write("\2\u0189U\3\2\2\2\'X`dht\u0082\u0089\u0090\u009d\u00a4")
        buf.write("\u00ab\u00af\u00b3\u00bd\u00c8\u00cb\u00d6\u00db\u00e3")
        buf.write("\u00e7\u00eb\u00f7\u010d\u0120\u0123\u012c\u0133\u013a")
        buf.write("\u0141\u014b\u0156\u015e\u0163\u0168\u0174\u017e\u0184")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'array'", "'auto'", "'boolean'", "'break'", 
                     "'continue'", "'do'", "'else'", "'false'", "'float'", 
                     "'for'", "'function'", "'if'", "'inherit'", "'integer'", 
                     "'of'", "'out'", "'return'", "'string'", "'true'", 
                     "'while'", "'void'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'='", "','", "':'", "';'", "'.'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<='", "'>='", "'<'", "'>'", "'::'", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "IntegerLiteral", "FloatingLiteral", 
                      "BooleanLiteral", "StringLiteral", "Array", "Auto", 
                      "Bool", "Break", "Continue", "Do", "Else", "False_", 
                      "Float", "For", "Function", "If", "Inherit", "Integer", 
                      "Of", "Out", "Return", "String", "True_", "While", 
                      "Void", "LeftParen", "RightParen", "LeftBracket", 
                      "RightBracket", "LeftBrace", "RightBrace", "Assign", 
                      "Comma", "Colon", "Semi", "Dot", "Plus", "Minus", 
                      "Star", "Slash", "Mod", "Not", "AndAnd", "OrOr", "Equal", 
                      "NotEqual", "LessEqual", "GreaterEqual", "Less", "Greater", 
                      "Doublecolon", "Identifier", "Whitespace", "Newline", 
                      "BlockComment", "LineComment", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_translationUnit = 1
    RULE_externalDeclaration = 2
    RULE_variableDeclaration = 3
    RULE_shortDeclaration = 4
    RULE_identifierList = 5
    RULE_fullDeclaration = 6
    RULE_initializer = 7
    RULE_initializerList = 8
    RULE_functionDeclaration = 9
    RULE_paramDeclarator = 10
    RULE_inheritance = 11
    RULE_parameterList = 12
    RULE_parameter = 13
    RULE_typeSpecifier = 14
    RULE_atomicType = 15
    RULE_arrayType = 16
    RULE_statement = 17
    RULE_blockStatement = 18
    RULE_blockItemList = 19
    RULE_blockItem = 20
    RULE_expressionStatement = 21
    RULE_selectionStatement = 22
    RULE_iterationStatement = 23
    RULE_forCondition = 24
    RULE_forDeclaration = 25
    RULE_conditionExpression = 26
    RULE_updateExpression = 27
    RULE_jumpStatement = 28
    RULE_expression = 29
    RULE_assignmentExpression = 30
    RULE_stringExpression = 31
    RULE_relationalExpression = 32
    RULE_logicalExpression = 33
    RULE_additiveExpression = 34
    RULE_multiplicativeExpression = 35
    RULE_unaryExpression = 36
    RULE_signExpression = 37
    RULE_postfixExpression = 38
    RULE_primaryExpression = 39
    RULE_functionCall = 40
    RULE_literal = 41

    ruleNames =  [ "program", "translationUnit", "externalDeclaration", 
                   "variableDeclaration", "shortDeclaration", "identifierList", 
                   "fullDeclaration", "initializer", "initializerList", 
                   "functionDeclaration", "paramDeclarator", "inheritance", 
                   "parameterList", "parameter", "typeSpecifier", "atomicType", 
                   "arrayType", "statement", "blockStatement", "blockItemList", 
                   "blockItem", "expressionStatement", "selectionStatement", 
                   "iterationStatement", "forCondition", "forDeclaration", 
                   "conditionExpression", "updateExpression", "jumpStatement", 
                   "expression", "assignmentExpression", "stringExpression", 
                   "relationalExpression", "logicalExpression", "additiveExpression", 
                   "multiplicativeExpression", "unaryExpression", "signExpression", 
                   "postfixExpression", "primaryExpression", "functionCall", 
                   "literal" ]

    EOF = Token.EOF
    IntegerLiteral=1
    FloatingLiteral=2
    BooleanLiteral=3
    StringLiteral=4
    Array=5
    Auto=6
    Bool=7
    Break=8
    Continue=9
    Do=10
    Else=11
    False_=12
    Float=13
    For=14
    Function=15
    If=16
    Inherit=17
    Integer=18
    Of=19
    Out=20
    Return=21
    String=22
    True_=23
    While=24
    Void=25
    LeftParen=26
    RightParen=27
    LeftBracket=28
    RightBracket=29
    LeftBrace=30
    RightBrace=31
    Assign=32
    Comma=33
    Colon=34
    Semi=35
    Dot=36
    Plus=37
    Minus=38
    Star=39
    Slash=40
    Mod=41
    Not=42
    AndAnd=43
    OrOr=44
    Equal=45
    NotEqual=46
    LessEqual=47
    GreaterEqual=48
    Less=49
    Greater=50
    Doublecolon=51
    Identifier=52
    Whitespace=53
    Newline=54
    BlockComment=55
    LineComment=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    ERROR_CHAR=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def translationUnit(self):
            return self.getTypedRuleContext(MT22Parser.TranslationUnitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Identifier]:
                self.state = 84
                self.translationUnit()
                pass
            elif token in [MT22Parser.EOF]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 88
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def externalDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.ExternalDeclarationContext,0)


        def translationUnit(self):
            return self.getTypedRuleContext(MT22Parser.TranslationUnitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_translationUnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslationUnit" ):
                return visitor.visitTranslationUnit(self)
            else:
                return visitor.visitChildren(self)




    def translationUnit(self):

        localctx = MT22Parser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_translationUnit)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.externalDeclaration()
                self.state = 91
                self.translationUnit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.externalDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternalDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.FunctionDeclarationContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_externalDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternalDeclaration" ):
                return visitor.visitExternalDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def externalDeclaration(self):

        localctx = MT22Parser.ExternalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_externalDeclaration)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.variableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def shortDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.ShortDeclarationContext,0)


        def fullDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.FullDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variableDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = MT22Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 100
                self.shortDeclaration()
                pass

            elif la_ == 2:
                self.state = 101
                self.fullDeclaration()
                pass


            self.state = 104
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MT22Parser.IdentifierListContext,0)


        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_shortDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortDeclaration" ):
                return visitor.visitShortDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def shortDeclaration(self):

        localctx = MT22Parser.ShortDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shortDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.identifierList()
            self.state = 107
            self.match(MT22Parser.Colon)
            self.state = 108
            self.typeSpecifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Comma(self):
            return self.getToken(MT22Parser.Comma, 0)

        def identifierList(self):
            return self.getTypedRuleContext(MT22Parser.IdentifierListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = MT22Parser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifierList)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(MT22Parser.Identifier)
                self.state = 111
                self.match(MT22Parser.Comma)
                self.state = 112
                self.identifierList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(MT22Parser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def fullDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.FullDeclarationContext,0)


        def initializer(self):
            return self.getTypedRuleContext(MT22Parser.InitializerContext,0)


        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def Assign(self):
            return self.getToken(MT22Parser.Assign, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_fullDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullDeclaration" ):
                return visitor.visitFullDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def fullDeclaration(self):

        localctx = MT22Parser.FullDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fullDeclaration)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(MT22Parser.Identifier)
                self.state = 117
                self.match(MT22Parser.Comma)
                self.state = 118
                self.fullDeclaration()
                self.state = 119
                self.match(MT22Parser.Comma)
                self.state = 120
                self.initializer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(MT22Parser.Identifier)
                self.state = 123
                self.match(MT22Parser.Colon)
                self.state = 124
                self.typeSpecifier()
                self.state = 125
                self.match(MT22Parser.Assign)
                self.state = 126
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentExpressionContext,0)


        def LeftBrace(self):
            return self.getToken(MT22Parser.LeftBrace, 0)

        def initializerList(self):
            return self.getTypedRuleContext(MT22Parser.InitializerListContext,0)


        def RightBrace(self):
            return self.getToken(MT22Parser.RightBrace, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_initializer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer" ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = MT22Parser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_initializer)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Minus, MT22Parser.Not, MT22Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.assignmentExpression()
                pass
            elif token in [MT22Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(MT22Parser.LeftBrace)
                self.state = 132
                self.initializerList()
                self.state = 133
                self.match(MT22Parser.RightBrace)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializer(self):
            return self.getTypedRuleContext(MT22Parser.InitializerContext,0)


        def Comma(self):
            return self.getToken(MT22Parser.Comma, 0)

        def initializerList(self):
            return self.getTypedRuleContext(MT22Parser.InitializerListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_initializerList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerList" ):
                return visitor.visitInitializerList(self)
            else:
                return visitor.visitChildren(self)




    def initializerList(self):

        localctx = MT22Parser.InitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initializerList)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.initializer()
                self.state = 138
                self.match(MT22Parser.Comma)
                self.state = 139
                self.initializerList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def Function(self):
            return self.getToken(MT22Parser.Function, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def paramDeclarator(self):
            return self.getTypedRuleContext(MT22Parser.ParamDeclaratorContext,0)


        def inheritance(self):
            return self.getTypedRuleContext(MT22Parser.InheritanceContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = MT22Parser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(MT22Parser.Identifier)
            self.state = 145
            self.match(MT22Parser.Colon)
            self.state = 146
            self.match(MT22Parser.Function)
            self.state = 147
            self.typeSpecifier()
            self.state = 148
            self.paramDeclarator()
            self.state = 149
            self.inheritance()
            self.state = 150
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MT22Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramDeclarator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDeclarator" ):
                return visitor.visitParamDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def paramDeclarator(self):

        localctx = MT22Parser.ParamDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramDeclarator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MT22Parser.LeftParen)
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Inherit, MT22Parser.Out, MT22Parser.Identifier]:
                self.state = 153
                self.parameterList()
                pass
            elif token in [MT22Parser.RightParen]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self.match(MT22Parser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InheritanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_inheritance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInheritance" ):
                return visitor.visitInheritance(self)
            else:
                return visitor.visitChildren(self)




    def inheritance(self):

        localctx = MT22Parser.InheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_inheritance)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Inherit]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(MT22Parser.Inherit)
                self.state = 160
                self.match(MT22Parser.Identifier)
                pass
            elif token in [MT22Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def Comma(self):
            return self.getToken(MT22Parser.Comma, 0)

        def parameterList(self):
            return self.getTypedRuleContext(MT22Parser.ParameterListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = MT22Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterList)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.parameter()
                self.state = 165
                self.match(MT22Parser.Comma)
                self.state = 166
                self.parameterList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Colon(self):
            return self.getToken(MT22Parser.Colon, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(MT22Parser.TypeSpecifierContext,0)


        def Inherit(self):
            return self.getToken(MT22Parser.Inherit, 0)

        def Out(self):
            return self.getToken(MT22Parser.Out, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Inherit]:
                self.state = 171
                self.match(MT22Parser.Inherit)
                pass
            elif token in [MT22Parser.Out, MT22Parser.Identifier]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Out]:
                self.state = 175
                self.match(MT22Parser.Out)
                pass
            elif token in [MT22Parser.Identifier]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self.match(MT22Parser.Identifier)
            self.state = 180
            self.match(MT22Parser.Colon)
            self.state = 181
            self.typeSpecifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def Void(self):
            return self.getToken(MT22Parser.Void, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def Auto(self):
            return self.getToken(MT22Parser.Auto, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_typeSpecifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = MT22Parser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typeSpecifier)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Bool, MT22Parser.Float, MT22Parser.Integer, MT22Parser.String]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.atomicType()
                pass
            elif token in [MT22Parser.Void]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(MT22Parser.Void)
                pass
            elif token in [MT22Parser.Array]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.arrayType()
                pass
            elif token in [MT22Parser.Auto]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(MT22Parser.Auto)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(MT22Parser.Integer, 0)

        def Bool(self):
            return self.getToken(MT22Parser.Bool, 0)

        def Float(self):
            return self.getToken(MT22Parser.Float, 0)

        def String(self):
            return self.getToken(MT22Parser.String, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomicType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicType" ):
                return visitor.visitAtomicType(self)
            else:
                return visitor.visitChildren(self)




    def atomicType(self):

        localctx = MT22Parser.AtomicTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atomicType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Bool) | (1 << MT22Parser.Float) | (1 << MT22Parser.Integer) | (1 << MT22Parser.String))) != 0)):
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array(self):
            return self.getToken(MT22Parser.Array, 0)

        def LeftBracket(self):
            return self.getToken(MT22Parser.LeftBracket, 0)

        def RightBracket(self):
            return self.getToken(MT22Parser.RightBracket, 0)

        def Of(self):
            return self.getToken(MT22Parser.Of, 0)

        def atomicType(self):
            return self.getTypedRuleContext(MT22Parser.AtomicTypeContext,0)


        def IntegerLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IntegerLiteral)
            else:
                return self.getToken(MT22Parser.IntegerLiteral, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MT22Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MT22Parser.Array)
            self.state = 192
            self.match(MT22Parser.LeftBracket)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.IntegerLiteral:
                self.state = 193
                self.match(MT22Parser.IntegerLiteral)
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MT22Parser.Comma:
                    self.state = 194
                    self.match(MT22Parser.Comma)
                    self.state = 195
                    self.match(MT22Parser.IntegerLiteral)
                    self.state = 200
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 203
            self.match(MT22Parser.RightBracket)
            self.state = 204
            self.match(MT22Parser.Of)
            self.state = 205
            self.atomicType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionStatementContext,0)


        def selectionStatement(self):
            return self.getTypedRuleContext(MT22Parser.SelectionStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(MT22Parser.IterationStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(MT22Parser.JumpStatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.LeftBrace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.blockStatement()
                pass
            elif token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Semi, MT22Parser.Minus, MT22Parser.Not, MT22Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.expressionStatement()
                pass
            elif token in [MT22Parser.If]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.selectionStatement()
                pass
            elif token in [MT22Parser.Do, MT22Parser.For, MT22Parser.While]:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.iterationStatement()
                pass
            elif token in [MT22Parser.Break, MT22Parser.Continue, MT22Parser.Return]:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.jumpStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftBrace(self):
            return self.getToken(MT22Parser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(MT22Parser.RightBrace, 0)

        def blockItemList(self):
            return self.getTypedRuleContext(MT22Parser.BlockItemListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = MT22Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MT22Parser.LeftBrace)
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.Break, MT22Parser.Continue, MT22Parser.Do, MT22Parser.For, MT22Parser.If, MT22Parser.Return, MT22Parser.While, MT22Parser.LeftParen, MT22Parser.LeftBrace, MT22Parser.Semi, MT22Parser.Minus, MT22Parser.Not, MT22Parser.Identifier]:
                self.state = 215
                self.blockItemList()
                pass
            elif token in [MT22Parser.RightBrace]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 219
            self.match(MT22Parser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockItemListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockItem(self):
            return self.getTypedRuleContext(MT22Parser.BlockItemContext,0)


        def blockItemList(self):
            return self.getTypedRuleContext(MT22Parser.BlockItemListContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockItemList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockItemList" ):
                return visitor.visitBlockItemList(self)
            else:
                return visitor.visitChildren(self)




    def blockItemList(self):

        localctx = MT22Parser.BlockItemListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_blockItemList)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.blockItem()
                self.state = 222
                self.blockItemList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.blockItem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockItem" ):
                return visitor.visitBlockItem(self)
            else:
                return visitor.visitChildren(self)




    def blockItem(self):

        localctx = MT22Parser.BlockItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_blockItem)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.variableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expressionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MT22Parser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Minus, MT22Parser.Not, MT22Parser.Identifier]:
                self.state = 231
                self.expression()
                pass
            elif token in [MT22Parser.Semi]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 235
            self.match(MT22Parser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(MT22Parser.If, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def Else(self):
            return self.getToken(MT22Parser.Else, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_selectionStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectionStatement" ):
                return visitor.visitSelectionStatement(self)
            else:
                return visitor.visitChildren(self)




    def selectionStatement(self):

        localctx = MT22Parser.SelectionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_selectionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MT22Parser.If)
            self.state = 238
            self.match(MT22Parser.LeftParen)
            self.state = 239
            self.expression()
            self.state = 240
            self.match(MT22Parser.RightParen)
            self.state = 241
            self.statement()
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 242
                self.match(MT22Parser.Else)
                self.state = 243
                self.statement()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(MT22Parser.While, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def Do(self):
            return self.getToken(MT22Parser.Do, 0)

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def For(self):
            return self.getToken(MT22Parser.For, 0)

        def forCondition(self):
            return self.getTypedRuleContext(MT22Parser.ForConditionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_iterationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterationStatement" ):
                return visitor.visitIterationStatement(self)
            else:
                return visitor.visitChildren(self)




    def iterationStatement(self):

        localctx = MT22Parser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_iterationStatement)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.While]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(MT22Parser.While)
                self.state = 248
                self.match(MT22Parser.LeftParen)
                self.state = 249
                self.expression()
                self.state = 250
                self.match(MT22Parser.RightParen)
                self.state = 251
                self.statement()
                pass
            elif token in [MT22Parser.Do]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(MT22Parser.Do)
                self.state = 254
                self.statement()
                self.state = 255
                self.match(MT22Parser.While)
                self.state = 256
                self.match(MT22Parser.LeftParen)
                self.state = 257
                self.expression()
                self.state = 258
                self.match(MT22Parser.RightParen)
                self.state = 259
                self.match(MT22Parser.Semi)
                pass
            elif token in [MT22Parser.For]:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.match(MT22Parser.For)
                self.state = 262
                self.match(MT22Parser.LeftParen)
                self.state = 263
                self.forCondition()
                self.state = 264
                self.match(MT22Parser.RightParen)
                self.state = 265
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forDeclaration(self):
            return self.getTypedRuleContext(MT22Parser.ForDeclarationContext,0)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.Comma)
            else:
                return self.getToken(MT22Parser.Comma, i)

        def conditionExpression(self):
            return self.getTypedRuleContext(MT22Parser.ConditionExpressionContext,0)


        def updateExpression(self):
            return self.getTypedRuleContext(MT22Parser.UpdateExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MT22Parser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.forDeclaration()
            self.state = 270
            self.match(MT22Parser.Comma)
            self.state = 271
            self.conditionExpression()
            self.state = 272
            self.match(MT22Parser.Comma)
            self.state = 273
            self.updateExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def Assign(self):
            return self.getToken(MT22Parser.Assign, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForDeclaration" ):
                return visitor.visitForDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def forDeclaration(self):

        localctx = MT22Parser.ForDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MT22Parser.Identifier)
            self.state = 276
            self.match(MT22Parser.Assign)
            self.state = 277
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self):
            return self.getTypedRuleContext(MT22Parser.RelationalExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_conditionExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpression" ):
                return visitor.visitConditionExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionExpression(self):

        localctx = MT22Parser.ConditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_conditionExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.relationalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringExpression(self):
            return self.getTypedRuleContext(MT22Parser.StringExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_updateExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateExpression" ):
                return visitor.visitUpdateExpression(self)
            else:
                return visitor.visitChildren(self)




    def updateExpression(self):

        localctx = MT22Parser.UpdateExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_updateExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.stringExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(MT22Parser.Semi, 0)

        def Return(self):
            return self.getToken(MT22Parser.Return, 0)

        def Continue(self):
            return self.getToken(MT22Parser.Continue, 0)

        def Break(self):
            return self.getToken(MT22Parser.Break, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_jumpStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpStatement" ):
                return visitor.visitJumpStatement(self)
            else:
                return visitor.visitChildren(self)




    def jumpStatement(self):

        localctx = MT22Parser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Return]:
                self.state = 283
                self.match(MT22Parser.Return)
                self.state = 286
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Minus, MT22Parser.Not, MT22Parser.Identifier]:
                    self.state = 284
                    self.expression()
                    pass
                elif token in [MT22Parser.Semi]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [MT22Parser.Break, MT22Parser.Continue]:
                self.state = 288
                _la = self._input.LA(1)
                if not(_la==MT22Parser.Break or _la==MT22Parser.Continue):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 291
            self.match(MT22Parser.Semi)
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

        def assignmentExpression(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentExpressionContext,0)


        def Comma(self):
            return self.getToken(MT22Parser.Comma, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.assignmentExpression()
                self.state = 294
                self.match(MT22Parser.Comma)
                self.state = 295
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringExpression(self):
            return self.getTypedRuleContext(MT22Parser.StringExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.UnaryExpressionContext,0)


        def Assign(self):
            return self.getToken(MT22Parser.Assign, 0)

        def assignmentExpression(self):
            return self.getTypedRuleContext(MT22Parser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignmentExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = MT22Parser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignmentExpression)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.stringExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.unaryExpression()
                self.state = 302
                self.match(MT22Parser.Assign)
                self.state = 303
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.RelationalExpressionContext,i)


        def Doublecolon(self):
            return self.getToken(MT22Parser.Doublecolon, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpression" ):
                return visitor.visitStringExpression(self)
            else:
                return visitor.visitChildren(self)




    def stringExpression(self):

        localctx = MT22Parser.StringExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stringExpression)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.relationalExpression()
                self.state = 308
                self.match(MT22Parser.Doublecolon)
                self.state = 309
                self.relationalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.relationalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.LogicalExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.LogicalExpressionContext,i)


        def Less(self):
            return self.getToken(MT22Parser.Less, 0)

        def Greater(self):
            return self.getToken(MT22Parser.Greater, 0)

        def LessEqual(self):
            return self.getToken(MT22Parser.LessEqual, 0)

        def GreaterEqual(self):
            return self.getToken(MT22Parser.GreaterEqual, 0)

        def Equal(self):
            return self.getToken(MT22Parser.Equal, 0)

        def NotEqual(self):
            return self.getToken(MT22Parser.NotEqual, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relationalExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = MT22Parser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.logicalExpression(0)
                self.state = 315
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Equal) | (1 << MT22Parser.NotEqual) | (1 << MT22Parser.LessEqual) | (1 << MT22Parser.GreaterEqual) | (1 << MT22Parser.Less) | (1 << MT22Parser.Greater))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 316
                self.logicalExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.logicalExpression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(MT22Parser.AdditiveExpressionContext,0)


        def logicalExpression(self):
            return self.getTypedRuleContext(MT22Parser.LogicalExpressionContext,0)


        def AndAnd(self):
            return self.getToken(MT22Parser.AndAnd, 0)

        def OrOr(self):
            return self.getToken(MT22Parser.OrOr, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logicalExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.LogicalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_logicalExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.LogicalExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExpression)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 325
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AndAnd or _la==MT22Parser.OrOr):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 326
                    self.additiveExpression(0) 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(MT22Parser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(MT22Parser.AdditiveExpressionContext,0)


        def Plus(self):
            return self.getToken(MT22Parser.Plus, 0)

        def Minus(self):
            return self.getToken(MT22Parser.Minus, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_additiveExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_additiveExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.multiplicativeExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.AdditiveExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                    self.state = 335
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 336
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.Plus or _la==MT22Parser.Minus):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 337
                    self.multiplicativeExpression() 
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.UnaryExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(MT22Parser.MultiplicativeExpressionContext,0)


        def Star(self):
            return self.getToken(MT22Parser.Star, 0)

        def Slash(self):
            return self.getToken(MT22Parser.Slash, 0)

        def Mod(self):
            return self.getToken(MT22Parser.Mod, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplicativeExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = MT22Parser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.unaryExpression()
                self.state = 344
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.Star) | (1 << MT22Parser.Slash) | (1 << MT22Parser.Mod))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 345
                self.multiplicativeExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.unaryExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Not(self):
            return self.getToken(MT22Parser.Not, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.UnaryExpressionContext,0)


        def signExpression(self):
            return self.getTypedRuleContext(MT22Parser.SignExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_unaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = MT22Parser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unaryExpression)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(MT22Parser.Not)
                self.state = 351
                self.unaryExpression()
                pass
            elif token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Minus, MT22Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.signExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Minus(self):
            return self.getToken(MT22Parser.Minus, 0)

        def signExpression(self):
            return self.getTypedRuleContext(MT22Parser.SignExpressionContext,0)


        def postfixExpression(self):
            return self.getTypedRuleContext(MT22Parser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_signExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignExpression" ):
                return visitor.visitSignExpression(self)
            else:
                return visitor.visitChildren(self)




    def signExpression(self):

        localctx = MT22Parser.SignExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_signExpression)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.Minus]:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(MT22Parser.Minus)
                self.state = 356
                self.signExpression()
                pass
            elif token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.postfixExpression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(MT22Parser.PrimaryExpressionContext,0)


        def postfixExpression(self):
            return self.getTypedRuleContext(MT22Parser.PostfixExpressionContext,0)


        def LeftBracket(self):
            return self.getToken(MT22Parser.LeftBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RightBracket(self):
            return self.getToken(MT22Parser.RightBracket, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_postfixExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpression" ):
                return visitor.visitPostfixExpression(self)
            else:
                return visitor.visitChildren(self)



    def postfixExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.PostfixExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_postfixExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.primaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.PostfixExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                    self.state = 363
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 364
                    self.match(MT22Parser.LeftBracket)
                    self.state = 365
                    self.expression()
                    self.state = 366
                    self.match(MT22Parser.RightBracket) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def functionCall(self):
            return self.getTypedRuleContext(MT22Parser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_primaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = MT22Parser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_primaryExpression)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(MT22Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.match(MT22Parser.LeftParen)
                self.state = 376
                self.expression()
                self.state = 377
                self.match(MT22Parser.RightParen)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MT22Parser.Identifier, 0)

        def LeftParen(self):
            return self.getToken(MT22Parser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(MT22Parser.RightParen, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MT22Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MT22Parser.Identifier)
            self.state = 383
            self.match(MT22Parser.LeftParen)
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IntegerLiteral, MT22Parser.FloatingLiteral, MT22Parser.BooleanLiteral, MT22Parser.StringLiteral, MT22Parser.LeftParen, MT22Parser.Minus, MT22Parser.Not, MT22Parser.Identifier]:
                self.state = 384
                self.expression()
                pass
            elif token in [MT22Parser.RightParen]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 388
            self.match(MT22Parser.RightParen)
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
        self.enterRule(localctx, 82, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.logicalExpression_sempred
        self._predicates[34] = self.additiveExpression_sempred
        self._predicates[38] = self.postfixExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExpression_sempred(self, localctx:LogicalExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def postfixExpression_sempred(self, localctx:PostfixExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




