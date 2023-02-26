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
        buf.write("C\4D\tD\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3\u009a\n\3\3\3\3\3\3\4\3\4\5\4\u00a0")
        buf.write("\n\4\3\5\3\5\7\5\u00a4\n\5\f\5\16\5\u00a7\13\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\7\65\u0164\n\65\f\65\16\65\u0167\13\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\39\59\u0172\n9\39\79\u0175\n9\f9\16")
        buf.write("9\u0178\139\59\u017a\n9\3:\3:\7:\u017e\n:\f:\16:\u0181")
        buf.write("\13:\3;\3;\5;\u0185\n;\3;\6;\u0188\n;\r;\16;\u0189\3<")
        buf.write("\3<\5<\u018e\n<\3=\3=\3=\3>\6>\u0194\n>\r>\16>\u0195\3")
        buf.write(">\3>\3?\3?\3?\3?\3@\3@\3@\3@\7@\u01a2\n@\f@\16@\u01a5")
        buf.write("\13@\3@\3@\3@\3@\3@\3A\3A\3A\3A\7A\u01b0\nA\fA\16A\u01b3")
        buf.write("\13A\3A\3A\3B\3B\7B\u01b9\nB\fB\16B\u01bc\13B\3B\5B\u01bf")
        buf.write("\nB\3B\3B\3C\3C\7C\u01c5\nC\fC\16C\u01c8\13C\3C\3C\3C")
        buf.write("\3C\3C\3D\3D\3D\3\u01a3\2E\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2y\2{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\3\2\r\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\62;\3\2\63;\4\2--//\4\2GGgg\6\2\f\f\17\17$$^^\n")
        buf.write("\2$$))^^ddhhppttvv\5\2\n\f\16\17\"\"\4\2\f\f\17\17\t\2")
        buf.write("$$^^ddhhppttvv\2\u01db\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u0099")
        buf.write("\3\2\2\2\7\u009f\3\2\2\2\t\u00a1\3\2\2\2\13\u00ab\3\2")
        buf.write("\2\2\r\u00b1\3\2\2\2\17\u00b6\3\2\2\2\21\u00be\3\2\2\2")
        buf.write("\23\u00c4\3\2\2\2\25\u00cd\3\2\2\2\27\u00d0\3\2\2\2\31")
        buf.write("\u00d5\3\2\2\2\33\u00db\3\2\2\2\35\u00e1\3\2\2\2\37\u00e5")
        buf.write("\3\2\2\2!\u00ee\3\2\2\2#\u00f1\3\2\2\2%\u00f9\3\2\2\2")
        buf.write("\'\u0101\3\2\2\2)\u0104\3\2\2\2+\u0108\3\2\2\2-\u010f")
        buf.write("\3\2\2\2/\u0116\3\2\2\2\61\u011b\3\2\2\2\63\u0121\3\2")
        buf.write("\2\2\65\u0126\3\2\2\2\67\u0128\3\2\2\29\u012a\3\2\2\2")
        buf.write(";\u012c\3\2\2\2=\u012e\3\2\2\2?\u0130\3\2\2\2A\u0132\3")
        buf.write("\2\2\2C\u0134\3\2\2\2E\u0136\3\2\2\2G\u0138\3\2\2\2I\u013a")
        buf.write("\3\2\2\2K\u013c\3\2\2\2M\u013e\3\2\2\2O\u0140\3\2\2\2")
        buf.write("Q\u0142\3\2\2\2S\u0144\3\2\2\2U\u0146\3\2\2\2W\u0148\3")
        buf.write("\2\2\2Y\u014b\3\2\2\2[\u014e\3\2\2\2]\u0151\3\2\2\2_\u0154")
        buf.write("\3\2\2\2a\u0157\3\2\2\2c\u015a\3\2\2\2e\u015c\3\2\2\2")
        buf.write("g\u015e\3\2\2\2i\u0161\3\2\2\2k\u0168\3\2\2\2m\u016a\3")
        buf.write("\2\2\2o\u016c\3\2\2\2q\u0179\3\2\2\2s\u017b\3\2\2\2u\u0182")
        buf.write("\3\2\2\2w\u018d\3\2\2\2y\u018f\3\2\2\2{\u0193\3\2\2\2")
        buf.write("}\u0199\3\2\2\2\177\u019d\3\2\2\2\u0081\u01ab\3\2\2\2")
        buf.write("\u0083\u01b6\3\2\2\2\u0085\u01c2\3\2\2\2\u0087\u01ce\3")
        buf.write("\2\2\2\u0089\u008a\5q9\2\u008a\u008b\b\2\2\2\u008b\4\3")
        buf.write("\2\2\2\u008c\u008d\5q9\2\u008d\u008e\5s:\2\u008e\u009a")
        buf.write("\3\2\2\2\u008f\u0090\5q9\2\u0090\u0091\5u;\2\u0091\u009a")
        buf.write("\3\2\2\2\u0092\u0093\5s:\2\u0093\u0094\5u;\2\u0094\u009a")
        buf.write("\3\2\2\2\u0095\u0096\5q9\2\u0096\u0097\5s:\2\u0097\u0098")
        buf.write("\5u;\2\u0098\u009a\3\2\2\2\u0099\u008c\3\2\2\2\u0099\u008f")
        buf.write("\3\2\2\2\u0099\u0092\3\2\2\2\u0099\u0095\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\b\3\3\2\u009c\6\3\2\2\2\u009d")
        buf.write("\u00a0\5\31\r\2\u009e\u00a0\5/\30\2\u009f\u009d\3\2\2")
        buf.write("\2\u009f\u009e\3\2\2\2\u00a0\b\3\2\2\2\u00a1\u00a5\7$")
        buf.write("\2\2\u00a2\u00a4\5w<\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7$\2\2")
        buf.write("\u00a9\u00aa\b\5\4\2\u00aa\n\3\2\2\2\u00ab\u00ac\7c\2")
        buf.write("\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7")
        buf.write("c\2\2\u00af\u00b0\7{\2\2\u00b0\f\3\2\2\2\u00b1\u00b2\7")
        buf.write("c\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\16\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd\7p\2\2\u00bd\20")
        buf.write("\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7m\2\2\u00c3\22")
        buf.write("\3\2\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca")
        buf.write("\7p\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7g\2\2\u00cc\24")
        buf.write("\3\2\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf\7q\2\2\u00cf\26")
        buf.write("\3\2\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\30\3\2\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7u\2\2\u00d9\u00da\7g\2\2\u00da\32\3\2\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7v\2\2\u00e0\34\3\2\2\2\u00e1\u00e2")
        buf.write("\7h\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4\36")
        buf.write("\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed \3")
        buf.write("\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7h\2\2\u00f0\"\3")
        buf.write("\2\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7j\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7v\2\2\u00f8$\3\2\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7i\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100&\3\2\2\2\u0101\u0102\7q\2\2\u0102\u0103")
        buf.write("\7h\2\2\u0103(\3\2\2\2\u0104\u0105\7q\2\2\u0105\u0106")
        buf.write("\7w\2\2\u0106\u0107\7v\2\2\u0107*\3\2\2\2\u0108\u0109")
        buf.write("\7t\2\2\u0109\u010a\7g\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7w\2\2\u010c\u010d\7t\2\2\u010d\u010e\7p\2\2\u010e,\3")
        buf.write("\2\2\2\u010f\u0110\7u\2\2\u0110\u0111\7v\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7k\2\2\u0113\u0114\7p\2\2\u0114\u0115")
        buf.write("\7i\2\2\u0115.\3\2\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7w\2\2\u0119\u011a\7g\2\2\u011a\60")
        buf.write("\3\2\2\2\u011b\u011c\7y\2\2\u011c\u011d\7j\2\2\u011d\u011e")
        buf.write("\7k\2\2\u011e\u011f\7n\2\2\u011f\u0120\7g\2\2\u0120\62")
        buf.write("\3\2\2\2\u0121\u0122\7x\2\2\u0122\u0123\7q\2\2\u0123\u0124")
        buf.write("\7k\2\2\u0124\u0125\7f\2\2\u0125\64\3\2\2\2\u0126\u0127")
        buf.write("\7*\2\2\u0127\66\3\2\2\2\u0128\u0129\7+\2\2\u01298\3\2")
        buf.write("\2\2\u012a\u012b\7]\2\2\u012b:\3\2\2\2\u012c\u012d\7_")
        buf.write("\2\2\u012d<\3\2\2\2\u012e\u012f\7}\2\2\u012f>\3\2\2\2")
        buf.write("\u0130\u0131\7\177\2\2\u0131@\3\2\2\2\u0132\u0133\7?\2")
        buf.write("\2\u0133B\3\2\2\2\u0134\u0135\7.\2\2\u0135D\3\2\2\2\u0136")
        buf.write("\u0137\7<\2\2\u0137F\3\2\2\2\u0138\u0139\7=\2\2\u0139")
        buf.write("H\3\2\2\2\u013a\u013b\7\60\2\2\u013bJ\3\2\2\2\u013c\u013d")
        buf.write("\7-\2\2\u013dL\3\2\2\2\u013e\u013f\7/\2\2\u013fN\3\2\2")
        buf.write("\2\u0140\u0141\7,\2\2\u0141P\3\2\2\2\u0142\u0143\7\61")
        buf.write("\2\2\u0143R\3\2\2\2\u0144\u0145\7\'\2\2\u0145T\3\2\2\2")
        buf.write("\u0146\u0147\7#\2\2\u0147V\3\2\2\2\u0148\u0149\7(\2\2")
        buf.write("\u0149\u014a\7(\2\2\u014aX\3\2\2\2\u014b\u014c\7~\2\2")
        buf.write("\u014c\u014d\7~\2\2\u014dZ\3\2\2\2\u014e\u014f\7?\2\2")
        buf.write("\u014f\u0150\7?\2\2\u0150\\\3\2\2\2\u0151\u0152\7#\2\2")
        buf.write("\u0152\u0153\7?\2\2\u0153^\3\2\2\2\u0154\u0155\7>\2\2")
        buf.write("\u0155\u0156\7?\2\2\u0156`\3\2\2\2\u0157\u0158\7@\2\2")
        buf.write("\u0158\u0159\7?\2\2\u0159b\3\2\2\2\u015a\u015b\7>\2\2")
        buf.write("\u015bd\3\2\2\2\u015c\u015d\7@\2\2\u015df\3\2\2\2\u015e")
        buf.write("\u015f\7<\2\2\u015f\u0160\7<\2\2\u0160h\3\2\2\2\u0161")
        buf.write("\u0165\t\2\2\2\u0162\u0164\t\3\2\2\u0163\u0162\3\2\2\2")
        buf.write("\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166j\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169")
        buf.write("\t\4\2\2\u0169l\3\2\2\2\u016a\u016b\t\5\2\2\u016bn\3\2")
        buf.write("\2\2\u016c\u016d\t\6\2\2\u016dp\3\2\2\2\u016e\u017a\7")
        buf.write("\62\2\2\u016f\u0176\5m\67\2\u0170\u0172\7a\2\2\u0171\u0170")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0175\5k\66\2\u0174\u0171\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u017a\3")
        buf.write("\2\2\2\u0178\u0176\3\2\2\2\u0179\u016e\3\2\2\2\u0179\u016f")
        buf.write("\3\2\2\2\u017ar\3\2\2\2\u017b\u017f\7\60\2\2\u017c\u017e")
        buf.write("\5k\66\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180t\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0182\u0184\t\7\2\2\u0183\u0185\5o8\2\u0184")
        buf.write("\u0183\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2")
        buf.write("\u0186\u0188\5k\66\2\u0187\u0186\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018av")
        buf.write("\3\2\2\2\u018b\u018e\n\b\2\2\u018c\u018e\5y=\2\u018d\u018b")
        buf.write("\3\2\2\2\u018d\u018c\3\2\2\2\u018ex\3\2\2\2\u018f\u0190")
        buf.write("\7^\2\2\u0190\u0191\t\t\2\2\u0191z\3\2\2\2\u0192\u0194")
        buf.write("\t\n\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0198\b>\5\2\u0198|\3\2\2\2\u0199\u019a\7\f\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019c\b?\5\2\u019c~\3\2\2\2")
        buf.write("\u019d\u019e\7\61\2\2\u019e\u019f\7,\2\2\u019f\u01a3\3")
        buf.write("\2\2\2\u01a0\u01a2\13\2\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\7")
        buf.write(",\2\2\u01a7\u01a8\7\61\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa")
        buf.write("\b@\5\2\u01aa\u0080\3\2\2\2\u01ab\u01ac\7\61\2\2\u01ac")
        buf.write("\u01ad\7\61\2\2\u01ad\u01b1\3\2\2\2\u01ae\u01b0\n\13\2")
        buf.write("\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b5\bA\5\2\u01b5\u0082\3\2\2\2")
        buf.write("\u01b6\u01ba\7$\2\2\u01b7\u01b9\5w<\2\u01b8\u01b7\3\2")
        buf.write("\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("\u01bf\7\2\2\3\u01be\u01bd\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c1\bB\6\2\u01c1\u0084\3")
        buf.write("\2\2\2\u01c2\u01c6\7$\2\2\u01c3\u01c5\5w<\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c9\u01ca\7^\2\2\u01ca\u01cb\n\f\2\2\u01cb\u01cc\3")
        buf.write("\2\2\2\u01cc\u01cd\bC\7\2\u01cd\u0086\3\2\2\2\u01ce\u01cf")
        buf.write("\13\2\2\2\u01cf\u01d0\bD\b\2\u01d0\u0088\3\2\2\2\24\2")
        buf.write("\u0099\u009f\u00a5\u0165\u0171\u0176\u0179\u017f\u0184")
        buf.write("\u0189\u018d\u0195\u01a3\u01b1\u01ba\u01be\u01c6\t\3\2")
        buf.write("\2\3\3\3\3\5\4\b\2\2\3B\5\3C\6\3D\7")
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
            		raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


