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
        buf.write("\u01d1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\62\5\62\u0142\n\62\3\62")
        buf.write("\3\62\5\62\u0146\n\62\3\62\3\62\3\62\5\62\u014b\n\62\3")
        buf.write("\62\3\62\3\62\5\62\u0150\n\62\3\63\3\63\5\63\u0154\n\63")
        buf.write("\3\64\3\64\7\64\u0158\n\64\f\64\16\64\u015b\13\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\7\65\u0162\n\65\f\65\16\65\u0165")
        buf.write("\13\65\3\66\3\66\3\67\3\67\38\38\39\39\39\59\u0170\n9")
        buf.write("\39\79\u0173\n9\f9\169\u0176\139\39\39\59\u017a\n9\3:")
        buf.write("\3:\7:\u017e\n:\f:\16:\u0181\13:\3;\3;\5;\u0185\n;\3;")
        buf.write("\6;\u0188\n;\r;\16;\u0189\3<\3<\5<\u018e\n<\3=\3=\3=\3")
        buf.write(">\6>\u0194\n>\r>\16>\u0195\3>\3>\3?\3?\3?\3?\3@\3@\3@")
        buf.write("\3@\7@\u01a2\n@\f@\16@\u01a5\13@\3@\3@\3@\3@\3@\3A\3A")
        buf.write("\3A\3A\7A\u01b0\nA\fA\16A\u01b3\13A\3A\3A\3B\3B\7B\u01b9")
        buf.write("\nB\fB\16B\u01bc\13B\3B\5B\u01bf\nB\3B\3B\3C\3C\7C\u01c5")
        buf.write("\nC\fC\16C\u01c8\13C\3C\3C\3C\3C\3C\3D\3D\3D\3\u01a3\2")
        buf.write("E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\2q\2")
        buf.write("s\2u\2w\2y\2{\67}8\1779\u0081:\u0083;\u0085<\u0087=\3")
        buf.write("\2\r\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2--/")
        buf.write("/\4\2GGgg\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2\n")
        buf.write("\f\16\17\"\"\4\2\f\f\17\17\t\2$$^^ddhhppttvv\2\u01dd\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\3\u0089\3\2\2\2\5\u008f\3\2\2\2\7\u0094\3\2\2")
        buf.write("\2\t\u0099\3\2\2\2\13\u009f\3\2\2\2\r\u00a8\3\2\2\2\17")
        buf.write("\u00ab\3\2\2\2\21\u00b0\3\2\2\2\23\u00b6\3\2\2\2\25\u00bc")
        buf.write("\3\2\2\2\27\u00c0\3\2\2\2\31\u00c9\3\2\2\2\33\u00cc\3")
        buf.write("\2\2\2\35\u00d4\3\2\2\2\37\u00dc\3\2\2\2!\u00df\3\2\2")
        buf.write("\2#\u00e3\3\2\2\2%\u00ea\3\2\2\2\'\u00f1\3\2\2\2)\u00f6")
        buf.write("\3\2\2\2+\u00fc\3\2\2\2-\u0101\3\2\2\2/\u0103\3\2\2\2")
        buf.write("\61\u0105\3\2\2\2\63\u0107\3\2\2\2\65\u0109\3\2\2\2\67")
        buf.write("\u010b\3\2\2\29\u010d\3\2\2\2;\u010f\3\2\2\2=\u0111\3")
        buf.write("\2\2\2?\u0113\3\2\2\2A\u0115\3\2\2\2C\u0117\3\2\2\2E\u0119")
        buf.write("\3\2\2\2G\u011b\3\2\2\2I\u011d\3\2\2\2K\u011f\3\2\2\2")
        buf.write("M\u0121\3\2\2\2O\u0123\3\2\2\2Q\u0126\3\2\2\2S\u0129\3")
        buf.write("\2\2\2U\u012c\3\2\2\2W\u012f\3\2\2\2Y\u0132\3\2\2\2[\u0135")
        buf.write("\3\2\2\2]\u0137\3\2\2\2_\u0139\3\2\2\2a\u013c\3\2\2\2")
        buf.write("c\u014f\3\2\2\2e\u0153\3\2\2\2g\u0155\3\2\2\2i\u015f\3")
        buf.write("\2\2\2k\u0166\3\2\2\2m\u0168\3\2\2\2o\u016a\3\2\2\2q\u0179")
        buf.write("\3\2\2\2s\u017b\3\2\2\2u\u0182\3\2\2\2w\u018d\3\2\2\2")
        buf.write("y\u018f\3\2\2\2{\u0193\3\2\2\2}\u0199\3\2\2\2\177\u019d")
        buf.write("\3\2\2\2\u0081\u01ab\3\2\2\2\u0083\u01b6\3\2\2\2\u0085")
        buf.write("\u01c2\3\2\2\2\u0087\u01ce\3\2\2\2\u0089\u008a\7c\2\2")
        buf.write("\u008a\u008b\7t\2\2\u008b\u008c\7t\2\2\u008c\u008d\7c")
        buf.write("\2\2\u008d\u008e\7{\2\2\u008e\4\3\2\2\2\u008f\u0090\7")
        buf.write("c\2\2\u0090\u0091\7w\2\2\u0091\u0092\7v\2\2\u0092\u0093")
        buf.write("\7q\2\2\u0093\6\3\2\2\2\u0094\u0095\7d\2\2\u0095\u0096")
        buf.write("\7q\2\2\u0096\u0097\7q\2\2\u0097\u0098\7n\2\2\u0098\b")
        buf.write("\3\2\2\2\u0099\u009a\7d\2\2\u009a\u009b\7t\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7c\2\2\u009d\u009e\7m\2\2\u009e\n")
        buf.write("\3\2\2\2\u009f\u00a0\7e\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7g\2\2\u00a7\f")
        buf.write("\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9\u00aa\7q\2\2\u00aa\16")
        buf.write("\3\2\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae")
        buf.write("\7u\2\2\u00ae\u00af\7g\2\2\u00af\20\3\2\2\2\u00b0\u00b1")
        buf.write("\7h\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\22\3\2\2\2\u00b6\u00b7")
        buf.write("\7h\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7c\2\2\u00ba\u00bb\7v\2\2\u00bb\24\3\2\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7t\2\2\u00bf\26")
        buf.write("\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3")
        buf.write("\7p\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7p\2\2\u00c8\30")
        buf.write("\3\2\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7h\2\2\u00cb\32")
        buf.write("\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf")
        buf.write("\7j\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7v\2\2\u00d3\34\3\2\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\u00d9\7i\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\36\3\2\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de")
        buf.write("\7h\2\2\u00de \3\2\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7w\2\2\u00e1\u00e2\7v\2\2\u00e2\"\3\2\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7p\2\2\u00e9$\3")
        buf.write("\2\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7i\2\2\u00f0&\3\2\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5\7g\2\2\u00f5(\3")
        buf.write("\2\2\2\u00f6\u00f7\7y\2\2\u00f7\u00f8\7j\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7g\2\2\u00fb*\3")
        buf.write("\2\2\2\u00fc\u00fd\7x\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7f\2\2\u0100,\3\2\2\2\u0101\u0102")
        buf.write("\7*\2\2\u0102.\3\2\2\2\u0103\u0104\7+\2\2\u0104\60\3\2")
        buf.write("\2\2\u0105\u0106\7]\2\2\u0106\62\3\2\2\2\u0107\u0108\7")
        buf.write("_\2\2\u0108\64\3\2\2\2\u0109\u010a\7}\2\2\u010a\66\3\2")
        buf.write("\2\2\u010b\u010c\7\177\2\2\u010c8\3\2\2\2\u010d\u010e")
        buf.write("\7?\2\2\u010e:\3\2\2\2\u010f\u0110\7.\2\2\u0110<\3\2\2")
        buf.write("\2\u0111\u0112\7<\2\2\u0112>\3\2\2\2\u0113\u0114\7=\2")
        buf.write("\2\u0114@\3\2\2\2\u0115\u0116\7\60\2\2\u0116B\3\2\2\2")
        buf.write("\u0117\u0118\7-\2\2\u0118D\3\2\2\2\u0119\u011a\7/\2\2")
        buf.write("\u011aF\3\2\2\2\u011b\u011c\7,\2\2\u011cH\3\2\2\2\u011d")
        buf.write("\u011e\7\61\2\2\u011eJ\3\2\2\2\u011f\u0120\7\'\2\2\u0120")
        buf.write("L\3\2\2\2\u0121\u0122\7#\2\2\u0122N\3\2\2\2\u0123\u0124")
        buf.write("\7(\2\2\u0124\u0125\7(\2\2\u0125P\3\2\2\2\u0126\u0127")
        buf.write("\7~\2\2\u0127\u0128\7~\2\2\u0128R\3\2\2\2\u0129\u012a")
        buf.write("\7?\2\2\u012a\u012b\7?\2\2\u012bT\3\2\2\2\u012c\u012d")
        buf.write("\7#\2\2\u012d\u012e\7?\2\2\u012eV\3\2\2\2\u012f\u0130")
        buf.write("\7>\2\2\u0130\u0131\7?\2\2\u0131X\3\2\2\2\u0132\u0133")
        buf.write("\7@\2\2\u0133\u0134\7?\2\2\u0134Z\3\2\2\2\u0135\u0136")
        buf.write("\7>\2\2\u0136\\\3\2\2\2\u0137\u0138\7@\2\2\u0138^\3\2")
        buf.write("\2\2\u0139\u013a\7<\2\2\u013a\u013b\7<\2\2\u013b`\3\2")
        buf.write("\2\2\u013c\u013d\5q9\2\u013db\3\2\2\2\u013e\u013f\5q9")
        buf.write("\2\u013f\u0141\5s:\2\u0140\u0142\5u;\2\u0141\u0140\3\2")
        buf.write("\2\2\u0141\u0142\3\2\2\2\u0142\u0150\3\2\2\2\u0143\u0145")
        buf.write("\5q9\2\u0144\u0146\5s:\2\u0145\u0144\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\5u;\2\u0148\u0150")
        buf.write("\3\2\2\2\u0149\u014b\5q9\2\u014a\u0149\3\2\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\5s:\2\u014d\u014e")
        buf.write("\5u;\2\u014e\u0150\3\2\2\2\u014f\u013e\3\2\2\2\u014f\u0143")
        buf.write("\3\2\2\2\u014f\u014a\3\2\2\2\u0150d\3\2\2\2\u0151\u0154")
        buf.write("\5\21\t\2\u0152\u0154\5\'\24\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154f\3\2\2\2\u0155\u0159\7$\2\2\u0156")
        buf.write("\u0158\5w<\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159")
        buf.write("\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015c\u015d\7$\2\2\u015d\u015e\b")
        buf.write("\64\2\2\u015eh\3\2\2\2\u015f\u0163\t\2\2\2\u0160\u0162")
        buf.write("\t\3\2\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164j\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0166\u0167\t\4\2\2\u0167l\3\2\2\2\u0168")
        buf.write("\u0169\t\5\2\2\u0169n\3\2\2\2\u016a\u016b\t\6\2\2\u016b")
        buf.write("p\3\2\2\2\u016c\u017a\7\62\2\2\u016d\u0174\5m\67\2\u016e")
        buf.write("\u0170\7a\2\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u0173\5k\66\2\u0172\u016f\3")
        buf.write("\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0178\b9\3\2\u0178\u017a\3\2\2\2\u0179\u016c\3\2\2\2")
        buf.write("\u0179\u016d\3\2\2\2\u017ar\3\2\2\2\u017b\u017f\7\60\2")
        buf.write("\2\u017c\u017e\5k\66\2\u017d\u017c\3\2\2\2\u017e\u0181")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("t\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0184\t\7\2\2\u0183")
        buf.write("\u0185\5o8\2\u0184\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("\u0187\3\2\2\2\u0186\u0188\5k\66\2\u0187\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3")
        buf.write("\2\2\2\u018av\3\2\2\2\u018b\u018e\n\b\2\2\u018c\u018e")
        buf.write("\5y=\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018ex")
        buf.write("\3\2\2\2\u018f\u0190\7^\2\2\u0190\u0191\t\t\2\2\u0191")
        buf.write("z\3\2\2\2\u0192\u0194\t\n\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0195\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0198\b>\4\2\u0198|\3\2\2\2")
        buf.write("\u0199\u019a\7\f\2\2\u019a\u019b\3\2\2\2\u019b\u019c\b")
        buf.write("?\4\2\u019c~\3\2\2\2\u019d\u019e\7\61\2\2\u019e\u019f")
        buf.write("\7,\2\2\u019f\u01a3\3\2\2\2\u01a0\u01a2\13\2\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3")
        buf.write("\2\2\2\u01a6\u01a7\7,\2\2\u01a7\u01a8\7\61\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9\u01aa\b@\4\2\u01aa\u0080\3\2\2\2\u01ab")
        buf.write("\u01ac\7\61\2\2\u01ac\u01ad\7\61\2\2\u01ad\u01b1\3\2\2")
        buf.write("\2\u01ae\u01b0\n\13\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3")
        buf.write("\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\bA\4\2")
        buf.write("\u01b5\u0082\3\2\2\2\u01b6\u01ba\7$\2\2\u01b7\u01b9\5")
        buf.write("w<\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bd\u01bf\7\2\2\3\u01be\u01bd\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\b")
        buf.write("B\5\2\u01c1\u0084\3\2\2\2\u01c2\u01c6\7$\2\2\u01c3\u01c5")
        buf.write("\5w<\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c9\u01ca\7^\2\2\u01ca\u01cb\n\f\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01cd\bC\6\2\u01cd\u0086\3")
        buf.write("\2\2\2\u01ce\u01cf\13\2\2\2\u01cf\u01d0\bD\7\2\u01d0\u0088")
        buf.write("\3\2\2\2\27\2\u0141\u0145\u014a\u014f\u0153\u0159\u0163")
        buf.write("\u016f\u0174\u0179\u017f\u0184\u0189\u018d\u0195\u01a3")
        buf.write("\u01b1\u01ba\u01be\u01c6\b\3\64\2\39\3\b\2\2\3B\4\3C\5")
        buf.write("\3D\6")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Array = 1
    Auto = 2
    Bool = 3
    Break = 4
    Continue = 5
    Do = 6
    Else = 7
    False_ = 8
    Float = 9
    For = 10
    Function = 11
    If = 12
    Inherit = 13
    Integer = 14
    Of = 15
    Out = 16
    Return = 17
    String = 18
    True_ = 19
    While = 20
    Void = 21
    LeftParen = 22
    RightParen = 23
    LeftBracket = 24
    RightBracket = 25
    LeftBrace = 26
    RightBrace = 27
    Assign = 28
    Comma = 29
    Colon = 30
    Semi = 31
    Dot = 32
    Plus = 33
    Minus = 34
    Star = 35
    Slash = 36
    Mod = 37
    Not = 38
    AndAnd = 39
    OrOr = 40
    Equal = 41
    NotEqual = 42
    LessEqual = 43
    GreaterEqual = 44
    Less = 45
    Greater = 46
    Doublecolon = 47
    IntegerLiteral = 48
    FloatingLiteral = 49
    BooleanLiteral = 50
    StringLiteral = 51
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
            "'array'", "'auto'", "'bool'", "'break'", "'continue'", "'do'", 
            "'else'", "'false'", "'float'", "'for'", "'function'", "'if'", 
            "'inherit'", "'integer'", "'of'", "'out'", "'return'", "'string'", 
            "'true'", "'while'", "'void'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'='", "','", "':'", "';'", "'.'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<='", 
            "'>='", "'<'", "'>'", "'::'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "Array", "Auto", "Bool", "Break", "Continue", "Do", "Else", 
            "False_", "Float", "For", "Function", "If", "Inherit", "Integer", 
            "Of", "Out", "Return", "String", "True_", "While", "Void", "LeftParen", 
            "RightParen", "LeftBracket", "RightBracket", "LeftBrace", "RightBrace", 
            "Assign", "Comma", "Colon", "Semi", "Dot", "Plus", "Minus", 
            "Star", "Slash", "Mod", "Not", "AndAnd", "OrOr", "Equal", "NotEqual", 
            "LessEqual", "GreaterEqual", "Less", "Greater", "Doublecolon", 
            "IntegerLiteral", "FloatingLiteral", "BooleanLiteral", "StringLiteral", 
            "Identifier", "Whitespace", "Newline", "BlockComment", "LineComment", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "Array", "Auto", "Bool", "Break", "Continue", "Do", "Else", 
                  "False_", "Float", "For", "Function", "If", "Inherit", 
                  "Integer", "Of", "Out", "Return", "String", "True_", "While", 
                  "Void", "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
                  "LeftBrace", "RightBrace", "Assign", "Comma", "Colon", 
                  "Semi", "Dot", "Plus", "Minus", "Star", "Slash", "Mod", 
                  "Not", "AndAnd", "OrOr", "Equal", "NotEqual", "LessEqual", 
                  "GreaterEqual", "Less", "Greater", "Doublecolon", "IntegerLiteral", 
                  "FloatingLiteral", "BooleanLiteral", "StringLiteral", 
                  "Identifier", "DIGIT", "NONZERODIGIT", "SIGN", "Digitsequence", 
                  "DecimalPart", "ExponentPart", "StringCharacter", "EscapeSequence", 
                  "Whitespace", "Newline", "BlockComment", "LineComment", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[50] = self.StringLiteral_action 
            actions[55] = self.Digitsequence_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def StringLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def Digitsequence_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise UncloseString(y[0:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise IllegalEscape(y[0:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


