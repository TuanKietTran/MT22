# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u0090\n\3\3\3\3\3")
        buf.write("\5\3\u0094\n\3\3\3\3\3\3\3\5\3\u0099\n\3\3\3\3\3\3\3\5")
        buf.write("\3\u009e\n\3\3\3\3\3\3\4\3\4\5\4\u00a4\n\4\3\5\3\5\7\5")
        buf.write("\u00a8\n\5\f\5\16\5\u00ab\13\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\7\65\u0168\n\65")
        buf.write("\f\65\16\65\u016b\13\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\39\59\u0176\n9\39\79\u0179\n9\f9\169\u017c\139\59\u017e")
        buf.write("\n9\3:\3:\7:\u0182\n:\f:\16:\u0185\13:\3;\3;\5;\u0189")
        buf.write("\n;\3;\6;\u018c\n;\r;\16;\u018d\3<\3<\5<\u0192\n<\3=\3")
        buf.write("=\3=\3>\6>\u0198\n>\r>\16>\u0199\3>\3>\3?\3?\3?\3?\3@")
        buf.write("\3@\3@\3@\7@\u01a6\n@\f@\16@\u01a9\13@\3@\3@\3@\3@\3@")
        buf.write("\3A\3A\3A\3A\7A\u01b4\nA\fA\16A\u01b7\13A\3A\3A\3B\3B")
        buf.write("\7B\u01bd\nB\fB\16B\u01c0\13B\3B\5B\u01c3\nB\3B\3B\3C")
        buf.write("\3C\7C\u01c9\nC\fC\16C\u01cc\13C\3C\3C\3C\3C\3C\3D\3D")
        buf.write("\3D\3\u01a7\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\2m\2o\2q\2s\2u\2w\2y\2{\67}8\1779\u0081:\u0083;\u0085")
        buf.write("<\u0087=\3\2\r\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63")
        buf.write(";\4\2--//\4\2GGgg\6\2\f\f\17\17$$^^\n\2$$))^^ddhhpptt")
        buf.write("vv\5\2\n\f\16\17\"\"\4\2\f\f\17\17\t\2$$^^ddhhppttvv\2")
        buf.write("\u01e1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u009d\3\2\2\2\7\u00a3")
        buf.write("\3\2\2\2\t\u00a5\3\2\2\2\13\u00af\3\2\2\2\r\u00b5\3\2")
        buf.write("\2\2\17\u00ba\3\2\2\2\21\u00c2\3\2\2\2\23\u00c8\3\2\2")
        buf.write("\2\25\u00d1\3\2\2\2\27\u00d4\3\2\2\2\31\u00d9\3\2\2\2")
        buf.write("\33\u00df\3\2\2\2\35\u00e5\3\2\2\2\37\u00e9\3\2\2\2!\u00f2")
        buf.write("\3\2\2\2#\u00f5\3\2\2\2%\u00fd\3\2\2\2\'\u0105\3\2\2\2")
        buf.write(")\u0108\3\2\2\2+\u010c\3\2\2\2-\u0113\3\2\2\2/\u011a\3")
        buf.write("\2\2\2\61\u011f\3\2\2\2\63\u0125\3\2\2\2\65\u012a\3\2")
        buf.write("\2\2\67\u012c\3\2\2\29\u012e\3\2\2\2;\u0130\3\2\2\2=\u0132")
        buf.write("\3\2\2\2?\u0134\3\2\2\2A\u0136\3\2\2\2C\u0138\3\2\2\2")
        buf.write("E\u013a\3\2\2\2G\u013c\3\2\2\2I\u013e\3\2\2\2K\u0140\3")
        buf.write("\2\2\2M\u0142\3\2\2\2O\u0144\3\2\2\2Q\u0146\3\2\2\2S\u0148")
        buf.write("\3\2\2\2U\u014a\3\2\2\2W\u014c\3\2\2\2Y\u014f\3\2\2\2")
        buf.write("[\u0152\3\2\2\2]\u0155\3\2\2\2_\u0158\3\2\2\2a\u015b\3")
        buf.write("\2\2\2c\u015e\3\2\2\2e\u0160\3\2\2\2g\u0162\3\2\2\2i\u0165")
        buf.write("\3\2\2\2k\u016c\3\2\2\2m\u016e\3\2\2\2o\u0170\3\2\2\2")
        buf.write("q\u017d\3\2\2\2s\u017f\3\2\2\2u\u0186\3\2\2\2w\u0191\3")
        buf.write("\2\2\2y\u0193\3\2\2\2{\u0197\3\2\2\2}\u019d\3\2\2\2\177")
        buf.write("\u01a1\3\2\2\2\u0081\u01af\3\2\2\2\u0083\u01ba\3\2\2\2")
        buf.write("\u0085\u01c6\3\2\2\2\u0087\u01d2\3\2\2\2\u0089\u008a\5")
        buf.write("q9\2\u008a\u008b\b\2\2\2\u008b\4\3\2\2\2\u008c\u008d\5")
        buf.write("q9\2\u008d\u008f\5s:\2\u008e\u0090\5u;\2\u008f\u008e\3")
        buf.write("\2\2\2\u008f\u0090\3\2\2\2\u0090\u009e\3\2\2\2\u0091\u0093")
        buf.write("\5q9\2\u0092\u0094\5s:\2\u0093\u0092\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\5u;\2\u0096\u009e")
        buf.write("\3\2\2\2\u0097\u0099\5q9\2\u0098\u0097\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5s:\2\u009b\u009c")
        buf.write("\5u;\2\u009c\u009e\3\2\2\2\u009d\u008c\3\2\2\2\u009d\u0091")
        buf.write("\3\2\2\2\u009d\u0098\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a0\b\3\3\2\u00a0\6\3\2\2\2\u00a1\u00a4\5\31\r\2\u00a2")
        buf.write("\u00a4\5/\30\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\b\3\2\2\2\u00a5\u00a9\7$\2\2\u00a6\u00a8\5w<\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00ad\7$\2\2\u00ad\u00ae\b\5\4\2\u00ae")
        buf.write("\n\3\2\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1\7t\2\2\u00b1")
        buf.write("\u00b2\7t\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7{\2\2\u00b4")
        buf.write("\f\3\2\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7w\2\2\u00b7")
        buf.write("\u00b8\7v\2\2\u00b8\u00b9\7q\2\2\u00b9\16\3\2\2\2\u00ba")
        buf.write("\u00bb\7d\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7q\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7p\2\2\u00c1\20\3\2\2\2\u00c2\u00c3\7d\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7c\2\2\u00c6")
        buf.write("\u00c7\7m\2\2\u00c7\22\3\2\2\2\u00c8\u00c9\7e\2\2\u00c9")
        buf.write("\u00ca\7q\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7w\2\2\u00cf")
        buf.write("\u00d0\7g\2\2\u00d0\24\3\2\2\2\u00d1\u00d2\7f\2\2\u00d2")
        buf.write("\u00d3\7q\2\2\u00d3\26\3\2\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\u00d6\7n\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7g\2\2\u00d8")
        buf.write("\30\3\2\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7c\2\2\u00db")
        buf.write("\u00dc\7n\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de")
        buf.write("\32\3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7n\2\2\u00e1")
        buf.write("\u00e2\7q\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\34\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7q\2\2\u00e7")
        buf.write("\u00e8\7t\2\2\u00e8\36\3\2\2\2\u00e9\u00ea\7h\2\2\u00ea")
        buf.write("\u00eb\7w\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7e\2\2\u00ed")
        buf.write("\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7q\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1 \3\2\2\2\u00f2\u00f3\7k\2\2\u00f3")
        buf.write("\u00f4\7h\2\2\u00f4\"\3\2\2\2\u00f5\u00f6\7k\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7j\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\u00fa\7t\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7v\2\2\u00fc")
        buf.write("$\3\2\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write("\u0100\7v\2\2\u0100\u0101\7g\2\2\u0101\u0102\7i\2\2\u0102")
        buf.write("\u0103\7g\2\2\u0103\u0104\7t\2\2\u0104&\3\2\2\2\u0105")
        buf.write("\u0106\7q\2\2\u0106\u0107\7h\2\2\u0107(\3\2\2\2\u0108")
        buf.write("\u0109\7q\2\2\u0109\u010a\7w\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("*\3\2\2\2\u010c\u010d\7t\2\2\u010d\u010e\7g\2\2\u010e")
        buf.write("\u010f\7v\2\2\u010f\u0110\7w\2\2\u0110\u0111\7t\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112,\3\2\2\2\u0113\u0114\7u\2\2\u0114")
        buf.write("\u0115\7v\2\2\u0115\u0116\7t\2\2\u0116\u0117\7k\2\2\u0117")
        buf.write("\u0118\7p\2\2\u0118\u0119\7i\2\2\u0119.\3\2\2\2\u011a")
        buf.write("\u011b\7v\2\2\u011b\u011c\7t\2\2\u011c\u011d\7w\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\60\3\2\2\2\u011f\u0120\7y\2\2\u0120")
        buf.write("\u0121\7j\2\2\u0121\u0122\7k\2\2\u0122\u0123\7n\2\2\u0123")
        buf.write("\u0124\7g\2\2\u0124\62\3\2\2\2\u0125\u0126\7x\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7k\2\2\u0128\u0129\7f\2\2\u0129")
        buf.write("\64\3\2\2\2\u012a\u012b\7*\2\2\u012b\66\3\2\2\2\u012c")
        buf.write("\u012d\7+\2\2\u012d8\3\2\2\2\u012e\u012f\7]\2\2\u012f")
        buf.write(":\3\2\2\2\u0130\u0131\7_\2\2\u0131<\3\2\2\2\u0132\u0133")
        buf.write("\7}\2\2\u0133>\3\2\2\2\u0134\u0135\7\177\2\2\u0135@\3")
        buf.write("\2\2\2\u0136\u0137\7?\2\2\u0137B\3\2\2\2\u0138\u0139\7")
        buf.write(".\2\2\u0139D\3\2\2\2\u013a\u013b\7<\2\2\u013bF\3\2\2\2")
        buf.write("\u013c\u013d\7=\2\2\u013dH\3\2\2\2\u013e\u013f\7\60\2")
        buf.write("\2\u013fJ\3\2\2\2\u0140\u0141\7-\2\2\u0141L\3\2\2\2\u0142")
        buf.write("\u0143\7/\2\2\u0143N\3\2\2\2\u0144\u0145\7,\2\2\u0145")
        buf.write("P\3\2\2\2\u0146\u0147\7\61\2\2\u0147R\3\2\2\2\u0148\u0149")
        buf.write("\7\'\2\2\u0149T\3\2\2\2\u014a\u014b\7#\2\2\u014bV\3\2")
        buf.write("\2\2\u014c\u014d\7(\2\2\u014d\u014e\7(\2\2\u014eX\3\2")
        buf.write("\2\2\u014f\u0150\7~\2\2\u0150\u0151\7~\2\2\u0151Z\3\2")
        buf.write("\2\2\u0152\u0153\7?\2\2\u0153\u0154\7?\2\2\u0154\\\3\2")
        buf.write("\2\2\u0155\u0156\7#\2\2\u0156\u0157\7?\2\2\u0157^\3\2")
        buf.write("\2\2\u0158\u0159\7>\2\2\u0159\u015a\7?\2\2\u015a`\3\2")
        buf.write("\2\2\u015b\u015c\7@\2\2\u015c\u015d\7?\2\2\u015db\3\2")
        buf.write("\2\2\u015e\u015f\7>\2\2\u015fd\3\2\2\2\u0160\u0161\7@")
        buf.write("\2\2\u0161f\3\2\2\2\u0162\u0163\7<\2\2\u0163\u0164\7<")
        buf.write("\2\2\u0164h\3\2\2\2\u0165\u0169\t\2\2\2\u0166\u0168\t")
        buf.write("\3\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016aj\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016c\u016d\t\4\2\2\u016dl\3\2\2\2\u016e\u016f")
        buf.write("\t\5\2\2\u016fn\3\2\2\2\u0170\u0171\t\6\2\2\u0171p\3\2")
        buf.write("\2\2\u0172\u017e\7\62\2\2\u0173\u017a\5m\67\2\u0174\u0176")
        buf.write("\7a\2\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0179\5k\66\2\u0178\u0175\3\2\2\2")
        buf.write("\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u0172")
        buf.write("\3\2\2\2\u017d\u0173\3\2\2\2\u017er\3\2\2\2\u017f\u0183")
        buf.write("\7\60\2\2\u0180\u0182\5k\66\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184t\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0188\t\7\2")
        buf.write("\2\u0187\u0189\5o8\2\u0188\u0187\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u018b\3\2\2\2\u018a\u018c\5k\66\2\u018b\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018ev\3\2\2\2\u018f\u0192\n\b\2\2\u0190")
        buf.write("\u0192\5y=\2\u0191\u018f\3\2\2\2\u0191\u0190\3\2\2\2\u0192")
        buf.write("x\3\2\2\2\u0193\u0194\7^\2\2\u0194\u0195\t\t\2\2\u0195")
        buf.write("z\3\2\2\2\u0196\u0198\t\n\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019c\b>\5\2\u019c|\3\2\2\2")
        buf.write("\u019d\u019e\7\f\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\b")
        buf.write("?\5\2\u01a0~\3\2\2\2\u01a1\u01a2\7\61\2\2\u01a2\u01a3")
        buf.write("\7,\2\2\u01a3\u01a7\3\2\2\2\u01a4\u01a6\13\2\2\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3")
        buf.write("\2\2\2\u01aa\u01ab\7,\2\2\u01ab\u01ac\7\61\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\u01ae\b@\5\2\u01ae\u0080\3\2\2\2\u01af")
        buf.write("\u01b0\7\61\2\2\u01b0\u01b1\7\61\2\2\u01b1\u01b5\3\2\2")
        buf.write("\2\u01b2\u01b4\n\13\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\bA\5\2")
        buf.write("\u01b9\u0082\3\2\2\2\u01ba\u01be\7$\2\2\u01bb\u01bd\5")
        buf.write("w<\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c1\u01c3\7\2\2\3\u01c2\u01c1\3\2\2\2")
        buf.write("\u01c2\u01c3\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b")
        buf.write("B\6\2\u01c5\u0084\3\2\2\2\u01c6\u01ca\7$\2\2\u01c7\u01c9")
        buf.write("\5w<\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc")
        buf.write("\u01ca\3\2\2\2\u01cd\u01ce\7^\2\2\u01ce\u01cf\n\f\2\2")
        buf.write("\u01cf\u01d0\3\2\2\2\u01d0\u01d1\bC\7\2\u01d1\u0086\3")
        buf.write("\2\2\2\u01d2\u01d3\13\2\2\2\u01d3\u01d4\bD\b\2\u01d4\u0088")
        buf.write("\3\2\2\2\27\2\u008f\u0093\u0098\u009d\u00a3\u00a9\u0169")
        buf.write("\u0175\u017a\u017d\u0183\u0188\u018d\u0191\u0199\u01a7")
        buf.write("\u01b5\u01be\u01c2\u01ca\t\3\2\2\3\3\3\3\5\4\b\2\2\3B")
        buf.write("\5\3C\6\3D\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IntegerLiteral = 1
    FloatingLiteral = 2
    BooleanLiteral = 3
    StringLiteral = 4
    Array = 5
    Auto = 6
    Bool = 7
    Break = 8
    Continue = 9
    Do = 10
    Else = 11
    False_ = 12
    Float = 13
    For = 14
    Function = 15
    If = 16
    Inherit = 17
    Integer = 18
    Of = 19
    Out = 20
    Return = 21
    String = 22
    True_ = 23
    While = 24
    Void = 25
    LeftParen = 26
    RightParen = 27
    LeftBracket = 28
    RightBracket = 29
    LeftBrace = 30
    RightBrace = 31
    Assign = 32
    Comma = 33
    Colon = 34
    Semi = 35
    Dot = 36
    Plus = 37
    Minus = 38
    Star = 39
    Slash = 40
    Mod = 41
    Not = 42
    AndAnd = 43
    OrOr = 44
    Equal = 45
    NotEqual = 46
    LessEqual = 47
    GreaterEqual = 48
    Less = 49
    Greater = 50
    Doublecolon = 51
    Identifier = 52
    Whitespace = 53
    Newline = 54
    BlockComment = 55
    LineComment = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'auto'", "'boolean'", "'break'", "'continue'", "'do'", 
            "'else'", "'false'", "'float'", "'for'", "'function'", "'if'", 
            "'inherit'", "'integer'", "'of'", "'out'", "'return'", "'string'", 
            "'true'", "'while'", "'void'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'='", "','", "':'", "';'", "'.'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<='", 
            "'>='", "'<'", "'>'", "'::'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IntegerLiteral", "FloatingLiteral", "BooleanLiteral", "StringLiteral", 
            "Array", "Auto", "Bool", "Break", "Continue", "Do", "Else", 
            "False_", "Float", "For", "Function", "If", "Inherit", "Integer", 
            "Of", "Out", "Return", "String", "True_", "While", "Void", "LeftParen", 
            "RightParen", "LeftBracket", "RightBracket", "LeftBrace", "RightBrace", 
            "Assign", "Comma", "Colon", "Semi", "Dot", "Plus", "Minus", 
            "Star", "Slash", "Mod", "Not", "AndAnd", "OrOr", "Equal", "NotEqual", 
            "LessEqual", "GreaterEqual", "Less", "Greater", "Doublecolon", 
            "Identifier", "Whitespace", "Newline", "BlockComment", "LineComment", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IntegerLiteral", "FloatingLiteral", "BooleanLiteral", 
                  "StringLiteral", "Array", "Auto", "Bool", "Break", "Continue", 
                  "Do", "Else", "False_", "Float", "For", "Function", "If", 
                  "Inherit", "Integer", "Of", "Out", "Return", "String", 
                  "True_", "While", "Void", "LeftParen", "RightParen", "LeftBracket", 
                  "RightBracket", "LeftBrace", "RightBrace", "Assign", "Comma", 
                  "Colon", "Semi", "Dot", "Plus", "Minus", "Star", "Slash", 
                  "Mod", "Not", "AndAnd", "OrOr", "Equal", "NotEqual", "LessEqual", 
                  "GreaterEqual", "Less", "Greater", "Doublecolon", "Identifier", 
                  "DIGIT", "NONZERODIGIT", "SIGN", "Digitsequence", "DecimalPart", 
                  "ExponentPart", "StringCharacter", "EscapeSequence", "Whitespace", 
                  "Newline", "BlockComment", "LineComment", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.IntegerLiteral_action 
            actions[1] = self.FloatingLiteral_action 
            actions[3] = self.StringLiteral_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def IntegerLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def FloatingLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def StringLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise UncloseString(y[0:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[0:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


