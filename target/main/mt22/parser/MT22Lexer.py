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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\6\3\u0099\n\3\r\3\16\3\u009a\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\5\5\u00a3\n\5\3\5\3\5\3\5\3\5\5\5\u00a9\n")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u00af\n\5\3\5\3\5\3\5\3\5\5\5\u00b5")
        buf.write("\n\5\3\6\3\6\5\6\u00b9\n\6\3\7\3\7\7\7\u00bd\n\7\f\7\16")
        buf.write("\7\u00c0\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\5:\u0180\n:")
        buf.write("\3:\7:\u0183\n:\f:\16:\u0186\13:\5:\u0188\n:\3;\3;\7;")
        buf.write("\u018c\n;\f;\16;\u018f\13;\3<\3<\5<\u0193\n<\3<\6<\u0196")
        buf.write("\n<\r<\16<\u0197\3=\3=\5=\u019c\n=\3>\3>\3>\3?\6?\u01a2")
        buf.write("\n?\r?\16?\u01a3\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\7A\u01b0")
        buf.write("\nA\fA\16A\u01b3\13A\3A\3A\3A\3A\3A\3B\3B\3B\3B\7B\u01be")
        buf.write("\nB\fB\16B\u01c1\13B\3B\3B\3C\3C\7C\u01c7\nC\fC\16C\u01ca")
        buf.write("\13C\3C\5C\u01cd\nC\3C\3C\3D\3D\7D\u01d3\nD\fD\16D\u01d6")
        buf.write("\13D\3D\3D\3D\3D\3D\3E\3E\3E\3\u01b1\2F\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2s\2u\2w\2y\2{\2}")
        buf.write("8\1779\u0081:\u0083;\u0085<\u0087=\u0089>\3\2\r\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2--//\4\2GGgg\6")
        buf.write("\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2\n\f\16\17\"\"")
        buf.write("\4\2\f\f\17\17\t\2$$^^ddhhppttvv\2\u01eb\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\3\u008b\3\2\2\2\5\u0096\3\2\2\2\7\u009c\3\2\2")
        buf.write("\2\t\u00b4\3\2\2\2\13\u00b8\3\2\2\2\r\u00ba\3\2\2\2\17")
        buf.write("\u00c3\3\2\2\2\21\u00c9\3\2\2\2\23\u00ce\3\2\2\2\25\u00d3")
        buf.write("\3\2\2\2\27\u00d9\3\2\2\2\31\u00e2\3\2\2\2\33\u00e5\3")
        buf.write("\2\2\2\35\u00ea\3\2\2\2\37\u00f0\3\2\2\2!\u00f6\3\2\2")
        buf.write("\2#\u00fa\3\2\2\2%\u0103\3\2\2\2\'\u0106\3\2\2\2)\u010e")
        buf.write("\3\2\2\2+\u0116\3\2\2\2-\u0119\3\2\2\2/\u011d\3\2\2\2")
        buf.write("\61\u0124\3\2\2\2\63\u012b\3\2\2\2\65\u0130\3\2\2\2\67")
        buf.write("\u0136\3\2\2\29\u013b\3\2\2\2;\u013d\3\2\2\2=\u013f\3")
        buf.write("\2\2\2?\u0141\3\2\2\2A\u0143\3\2\2\2C\u0145\3\2\2\2E\u0147")
        buf.write("\3\2\2\2G\u0149\3\2\2\2I\u014b\3\2\2\2K\u014d\3\2\2\2")
        buf.write("M\u014f\3\2\2\2O\u0151\3\2\2\2Q\u0153\3\2\2\2S\u0155\3")
        buf.write("\2\2\2U\u0157\3\2\2\2W\u0159\3\2\2\2Y\u015b\3\2\2\2[\u015d")
        buf.write("\3\2\2\2]\u0160\3\2\2\2_\u0163\3\2\2\2a\u0166\3\2\2\2")
        buf.write("c\u0169\3\2\2\2e\u016c\3\2\2\2g\u016f\3\2\2\2i\u0171\3")
        buf.write("\2\2\2k\u0173\3\2\2\2m\u0176\3\2\2\2o\u0178\3\2\2\2q\u017a")
        buf.write("\3\2\2\2s\u0187\3\2\2\2u\u0189\3\2\2\2w\u0190\3\2\2\2")
        buf.write("y\u019b\3\2\2\2{\u019d\3\2\2\2}\u01a1\3\2\2\2\177\u01a7")
        buf.write("\3\2\2\2\u0081\u01ab\3\2\2\2\u0083\u01b9\3\2\2\2\u0085")
        buf.write("\u01c4\3\2\2\2\u0087\u01d0\3\2\2\2\u0089\u01dc\3\2\2\2")
        buf.write("\u008b\u008c\7g\2\2\u008c\u008d\7z\2\2\u008d\u008e\7r")
        buf.write("\2\2\u008e\u008f\7t\2\2\u008f\u0090\7g\2\2\u0090\u0091")
        buf.write("\7u\2\2\u0091\u0092\7u\2\2\u0092\u0093\7k\2\2\u0093\u0094")
        buf.write("\7q\2\2\u0094\u0095\7p\2\2\u0095\4\3\2\2\2\u0096\u0098")
        buf.write("\t\2\2\2\u0097\u0099\t\3\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\6\3\2\2\2\u009c\u009d\5s:\2\u009d\u009e\b\4\2\2")
        buf.write("\u009e\b\3\2\2\2\u009f\u00a0\5s:\2\u00a0\u00a2\5u;\2\u00a1")
        buf.write("\u00a3\5w<\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\b\5\3\2\u00a5\u00b5\3\2\2\2")
        buf.write("\u00a6\u00a8\5s:\2\u00a7\u00a9\5u;\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab")
        buf.write("\5w<\2\u00ab\u00ac\b\5\4\2\u00ac\u00b5\3\2\2\2\u00ad\u00af")
        buf.write("\5s:\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b1\5u;\2\u00b1\u00b2\5w<\2\u00b2\u00b3")
        buf.write("\b\5\5\2\u00b3\u00b5\3\2\2\2\u00b4\u009f\3\2\2\2\u00b4")
        buf.write("\u00a6\3\2\2\2\u00b4\u00ae\3\2\2\2\u00b5\n\3\2\2\2\u00b6")
        buf.write("\u00b9\5\35\17\2\u00b7\u00b9\5\63\32\2\u00b8\u00b6\3\2")
        buf.write("\2\2\u00b8\u00b7\3\2\2\2\u00b9\f\3\2\2\2\u00ba\u00be\7")
        buf.write("$\2\2\u00bb\u00bd\5y=\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\7$\2\2")
        buf.write("\u00c2\16\3\2\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7t\2")
        buf.write("\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7")
        buf.write("{\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7w\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7q\2\2\u00cd\22")
        buf.write("\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7n\2\2\u00d2\24\3\2\2\2\u00d3\u00d4")
        buf.write("\7d\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7m\2\2\u00d8\26\3\2\2\2\u00d9\u00da")
        buf.write("\7e\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd")
        buf.write("\7v\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df\u00e0")
        buf.write("\7w\2\2\u00e0\u00e1\7g\2\2\u00e1\30\3\2\2\2\u00e2\u00e3")
        buf.write("\7f\2\2\u00e3\u00e4\7q\2\2\u00e4\32\3\2\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\34\3\2\2\2\u00ea\u00eb\7h\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef\36\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5 \3\2\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8")
        buf.write("\7q\2\2\u00f8\u00f9\7t\2\2\u00f9\"\3\2\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7p\2\2\u0102$\3\2\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7h\2\2\u0105&\3\2\2\2\u0106\u0107")
        buf.write("\7k\2\2\u0107\u0108\7p\2\2\u0108\u0109\7j\2\2\u0109\u010a")
        buf.write("\7g\2\2\u010a\u010b\7t\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d(\3\2\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7p\2\2\u0110\u0111\7v\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7i\2\2\u0113\u0114\7g\2\2\u0114\u0115\7t\2\2\u0115*\3")
        buf.write("\2\2\2\u0116\u0117\7q\2\2\u0117\u0118\7h\2\2\u0118,\3")
        buf.write("\2\2\2\u0119\u011a\7q\2\2\u011a\u011b\7w\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c.\3\2\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7v\2\2\u0120\u0121\7w\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7p\2\2\u0123\60\3\2\2\2\u0124\u0125")
        buf.write("\7u\2\2\u0125\u0126\7v\2\2\u0126\u0127\7t\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a\7i\2\2\u012a\62")
        buf.write("\3\2\2\2\u012b\u012c\7v\2\2\u012c\u012d\7t\2\2\u012d\u012e")
        buf.write("\7w\2\2\u012e\u012f\7g\2\2\u012f\64\3\2\2\2\u0130\u0131")
        buf.write("\7y\2\2\u0131\u0132\7j\2\2\u0132\u0133\7k\2\2\u0133\u0134")
        buf.write("\7n\2\2\u0134\u0135\7g\2\2\u0135\66\3\2\2\2\u0136\u0137")
        buf.write("\7x\2\2\u0137\u0138\7q\2\2\u0138\u0139\7k\2\2\u0139\u013a")
        buf.write("\7f\2\2\u013a8\3\2\2\2\u013b\u013c\7*\2\2\u013c:\3\2\2")
        buf.write("\2\u013d\u013e\7+\2\2\u013e<\3\2\2\2\u013f\u0140\7]\2")
        buf.write("\2\u0140>\3\2\2\2\u0141\u0142\7_\2\2\u0142@\3\2\2\2\u0143")
        buf.write("\u0144\7}\2\2\u0144B\3\2\2\2\u0145\u0146\7\177\2\2\u0146")
        buf.write("D\3\2\2\2\u0147\u0148\7?\2\2\u0148F\3\2\2\2\u0149\u014a")
        buf.write("\7.\2\2\u014aH\3\2\2\2\u014b\u014c\7<\2\2\u014cJ\3\2\2")
        buf.write("\2\u014d\u014e\7=\2\2\u014eL\3\2\2\2\u014f\u0150\7\60")
        buf.write("\2\2\u0150N\3\2\2\2\u0151\u0152\7-\2\2\u0152P\3\2\2\2")
        buf.write("\u0153\u0154\7/\2\2\u0154R\3\2\2\2\u0155\u0156\7,\2\2")
        buf.write("\u0156T\3\2\2\2\u0157\u0158\7\61\2\2\u0158V\3\2\2\2\u0159")
        buf.write("\u015a\7\'\2\2\u015aX\3\2\2\2\u015b\u015c\7#\2\2\u015c")
        buf.write("Z\3\2\2\2\u015d\u015e\7(\2\2\u015e\u015f\7(\2\2\u015f")
        buf.write("\\\3\2\2\2\u0160\u0161\7~\2\2\u0161\u0162\7~\2\2\u0162")
        buf.write("^\3\2\2\2\u0163\u0164\7?\2\2\u0164\u0165\7?\2\2\u0165")
        buf.write("`\3\2\2\2\u0166\u0167\7#\2\2\u0167\u0168\7?\2\2\u0168")
        buf.write("b\3\2\2\2\u0169\u016a\7>\2\2\u016a\u016b\7?\2\2\u016b")
        buf.write("d\3\2\2\2\u016c\u016d\7@\2\2\u016d\u016e\7?\2\2\u016e")
        buf.write("f\3\2\2\2\u016f\u0170\7>\2\2\u0170h\3\2\2\2\u0171\u0172")
        buf.write("\7@\2\2\u0172j\3\2\2\2\u0173\u0174\7<\2\2\u0174\u0175")
        buf.write("\7<\2\2\u0175l\3\2\2\2\u0176\u0177\t\4\2\2\u0177n\3\2")
        buf.write("\2\2\u0178\u0179\t\5\2\2\u0179p\3\2\2\2\u017a\u017b\t")
        buf.write("\6\2\2\u017br\3\2\2\2\u017c\u0188\7\62\2\2\u017d\u0184")
        buf.write("\5o8\2\u017e\u0180\7a\2\2\u017f\u017e\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\5m\67\2\u0182")
        buf.write("\u017f\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3")
        buf.write("\2\2\2\u0187\u017c\3\2\2\2\u0187\u017d\3\2\2\2\u0188t")
        buf.write("\3\2\2\2\u0189\u018d\7\60\2\2\u018a\u018c\5m\67\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018ev\3\2\2\2\u018f\u018d\3\2\2")
        buf.write("\2\u0190\u0192\t\7\2\2\u0191\u0193\5q9\2\u0192\u0191\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0196")
        buf.write("\5m\67\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198x\3\2\2\2\u0199")
        buf.write("\u019c\n\b\2\2\u019a\u019c\5{>\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019cz\3\2\2\2\u019d\u019e\7^\2\2\u019e")
        buf.write("\u019f\t\t\2\2\u019f|\3\2\2\2\u01a0\u01a2\t\n\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\b")
        buf.write("?\6\2\u01a6~\3\2\2\2\u01a7\u01a8\7\f\2\2\u01a8\u01a9\3")
        buf.write("\2\2\2\u01a9\u01aa\b@\6\2\u01aa\u0080\3\2\2\2\u01ab\u01ac")
        buf.write("\7\61\2\2\u01ac\u01ad\7,\2\2\u01ad\u01b1\3\2\2\2\u01ae")
        buf.write("\u01b0\13\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2")
        buf.write("\2\u01b1\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b4")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\7,\2\2\u01b5")
        buf.write("\u01b6\7\61\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\bA\6\2")
        buf.write("\u01b8\u0082\3\2\2\2\u01b9\u01ba\7\61\2\2\u01ba\u01bb")
        buf.write("\7\61\2\2\u01bb\u01bf\3\2\2\2\u01bc\u01be\n\13\2\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c2\u01c3\bB\6\2\u01c3\u0084\3\2\2\2\u01c4\u01c8")
        buf.write("\7$\2\2\u01c5\u01c7\5y=\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cd\7\2\2\3")
        buf.write("\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01cf\bC\7\2\u01cf\u0086\3\2\2\2\u01d0\u01d4")
        buf.write("\7$\2\2\u01d1\u01d3\5y=\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\7^\2\2")
        buf.write("\u01d8\u01d9\n\f\2\2\u01d9\u01da\3\2\2\2\u01da\u01db\b")
        buf.write("D\b\2\u01db\u0088\3\2\2\2\u01dc\u01dd\13\2\2\2\u01dd\u01de")
        buf.write("\bE\t\2\u01de\u008a\3\2\2\2\27\2\u009a\u00a2\u00a8\u00ae")
        buf.write("\u00b4\u00b8\u00be\u017f\u0184\u0187\u018d\u0192\u0197")
        buf.write("\u019b\u01a3\u01b1\u01bf\u01c8\u01cc\u01d4\n\3\4\2\3\5")
        buf.write("\3\3\5\4\3\5\5\b\2\2\3C\6\3D\7\3E\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IDENT = 2
    IntegerLiteral = 3
    FloatingLiteral = 4
    BooleanLiteral = 5
    StringLiteral = 6
    Array = 7
    Auto = 8
    Bool = 9
    Break = 10
    Continue = 11
    Do = 12
    Else = 13
    False_ = 14
    Float = 15
    For = 16
    Function = 17
    If = 18
    Inherit = 19
    Integer = 20
    Of = 21
    Out = 22
    Return = 23
    String = 24
    True_ = 25
    While = 26
    Void = 27
    LeftParen = 28
    RightParen = 29
    LeftBracket = 30
    RightBracket = 31
    LeftBrace = 32
    RightBrace = 33
    Assign = 34
    Comma = 35
    Colon = 36
    Semi = 37
    Dot = 38
    Plus = 39
    Minus = 40
    Star = 41
    Div = 42
    Mod = 43
    Not = 44
    AndAnd = 45
    OrOr = 46
    Equal = 47
    NotEqual = 48
    LessEqual = 49
    GreaterEqual = 50
    Less = 51
    Greater = 52
    Doublecolon = 53
    Whitespace = 54
    Newline = 55
    BlockComment = 56
    LineComment = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'expression'", "'array'", "'auto'", "'bool'", "'break'", "'continue'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'inherit'", "'integer'", "'of'", "'out'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'='", "','", "':'", "';'", "'.'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<='", "'>='", "'<'", "'>'", "'::'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IDENT", "IntegerLiteral", "FloatingLiteral", "BooleanLiteral", 
            "StringLiteral", "Array", "Auto", "Bool", "Break", "Continue", 
            "Do", "Else", "False_", "Float", "For", "Function", "If", "Inherit", 
            "Integer", "Of", "Out", "Return", "String", "True_", "While", 
            "Void", "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
            "LeftBrace", "RightBrace", "Assign", "Comma", "Colon", "Semi", 
            "Dot", "Plus", "Minus", "Star", "Div", "Mod", "Not", "AndAnd", 
            "OrOr", "Equal", "NotEqual", "LessEqual", "GreaterEqual", "Less", 
            "Greater", "Doublecolon", "Whitespace", "Newline", "BlockComment", 
            "LineComment", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IDENT", "IntegerLiteral", "FloatingLiteral", 
                  "BooleanLiteral", "StringLiteral", "Array", "Auto", "Bool", 
                  "Break", "Continue", "Do", "Else", "False_", "Float", 
                  "For", "Function", "If", "Inherit", "Integer", "Of", "Out", 
                  "Return", "String", "True_", "While", "Void", "LeftParen", 
                  "RightParen", "LeftBracket", "RightBracket", "LeftBrace", 
                  "RightBrace", "Assign", "Comma", "Colon", "Semi", "Dot", 
                  "Plus", "Minus", "Star", "Div", "Mod", "Not", "AndAnd", 
                  "OrOr", "Equal", "NotEqual", "LessEqual", "GreaterEqual", 
                  "Less", "Greater", "Doublecolon", "DIGIT", "NONZERODIGIT", 
                  "SIGN", "Digitsequence", "DecimalPart", "ExponentPart", 
                  "StringCharacter", "EscapeSequence", "Whitespace", "Newline", 
                  "BlockComment", "LineComment", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[2] = self.IntegerLiteral_action 
            actions[3] = self.FloatingLiteral_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
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
     

        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 3:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise UncloseString(y[0:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[0:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


