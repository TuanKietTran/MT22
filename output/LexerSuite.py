import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_func_declare(self):
        """"""
        testcase = """main: function void () {}"""
        expect = """main,:,function,void,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 100))

    def test_unclose_string(self):
        """"""
        testcase = """str:string="Hello World!"""
        expect = """str,:,string,=,Unclosed String: Hello World!"""
        self.assertTrue(TestLexer.test(testcase, expect, 101))

    def test_nl_text(self):
        """"""
        testcase = """str:string="Hello \\n\\tWorld!";"""
        expect = """str,:,string,=,Hello \\n\\tWorld!,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 102))

    def test_Illegal_escape(self):
        """"""
        testcase = """str:string="Hello \\aWorld!";"""
        expect = """str,:,string,=,Illegal Escape In String: Hello \\a"""
        self.assertTrue(TestLexer.test(testcase, expect, 103))

    def test_nl_escape_error(self):
        """"""
        testcase = """str:string="Hello \nWorld!";"""
        expect = """str,:,string,=,Unclosed String: Hello """
        self.assertTrue(TestLexer.test(testcase, expect, 104))

    def test_identifier_list(self):
        """"""
        testcase = """abjkabv gega ghei giaw3y gue ve"""
        expect = """abjkabv,gega,ghei,giaw3y,gue,ve,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 105))

    def test_float_literal(self):
        """"""
        testcase = """1.12e+2 3.14e-312 12e8 1. 0.33E-3 123_5e10 6_3 1_0.12E-12 1_1_0.12e-10"""
        expect = """1.12e+2,3.14e-312,12e8,1.,0.33E-3,1235e10,63,10.12E-12,110.12e-10,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 106))

    def test_single_block_comment(self):
        """"""
        testcase = """/*this is block comt*/"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 107))

    def test_2_block_comments(self):
        """"""
        testcase = """            /* This is a block cmt */
                /* This is a block cmt */"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 108))

    def test_unterminated_comment(self):
        """"""
        testcase = """/* This is /*a block*/ cmt */"""
        expect = """cmt,*,/,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 109))

    def test_io_integer(self):
        """"""
        testcase = """main: function void () {a=readInteger(); printInteger(a);}"""
        expect = """main,:,function,void,(,),{,a,=,readInteger,(,),;,printInteger,(,a,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 110))

    def test_io_float(self):
        """"""
        testcase = """main: function void () {n=readFloat(); printFloat(n);}"""
        expect = """main,:,function,void,(,),{,n,=,readFloat,(,),;,printFloat,(,n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 111))

    def test_io_string(self):
        """"""
        testcase = """main: function void () {str=readString(); printString(str);}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,printString,(,str,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 112))

    def test_short_decl_array_2d(self):
        """"""
        testcase = """arr: array[5,5] of integer;"""
        expect = """arr,:,array,[,5,,,5,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 113))

    def test_short_decl_array_1d(self):
        """"""
        testcase = """arr: array[10] of integer;"""
        expect = """arr,:,array,[,10,],of,integer,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 114))

    def test_full_decl_array_1d(self):
        """"""
        testcase = """arr: array[5] of integer={1,2,3,4,5};"""
        expect = """arr,:,array,[,5,],of,integer,=,{,1,,,2,,,3,,,4,,,5,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 115))

    def test_full_decl_array_2d(self):
        """"""
        testcase = """arr: array[5,5] of integer={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};"""
        expect = """arr,:,array,[,5,,,5,],of,integer,=,{,{,1,,,2,,,3,,,4,,,5,},,,{,6,,,7,,,8,,,9,,,10,},,,{,11,,,12,,,13,,,14,,,15,},,,{,16,,,17,,,18,,,19,,,20,},,,{,21,,,22,,,23,,,24,,,25,},},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 116))

    def test_print_int_cal(self):
        """"""
        testcase = """main: function void () {printInteger(10+11);}"""
        expect = """main,:,function,void,(,),{,printInteger,(,10,+,11,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 117))

    def test_print_float_cal(self):
        """"""
        testcase = """main: function void () {printFloat(2e-7+3e-1);}"""
        expect = """main,:,function,void,(,),{,printFloat,(,2e-7,+,3e-1,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 118))

    def test_print_bool_cal(self):
        """"""
        testcase = """main: function void () {printBoolean(var_a && var_b || var_c);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,var_a,&&,var_b,||,var_c,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 119))

    def test_assign_int_expr(self):
        """"""
        testcase = """a:integer=5+6-(123*10+(24-30));"""
        expect = """a,:,integer,=,5,+,6,-,(,123,*,10,+,(,24,-,30,),),;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 120))

    def test_assign_int_list(self):
        """"""
        testcase = """a,b,c:intger=2,3;"""
        expect = """a,,,b,,,c,:,intger,=,2,,,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 121))

    def test_print_elem(self):
        """"""
        testcase = """main: function void () {printInteger(arr[0,1]);}"""
        expect = """main,:,function,void,(,),{,printInteger,(,arr,[,0,,,1,],),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 122))

    def test_assign_elem(self):
        """"""
        testcase = """main: function void () {arr[3]=3.14;}"""
        expect = """main,:,function,void,(,),{,arr,[,3,],=,3.14,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 123))

    def test_validate_zero(self):
        """"""
        testcase = """main: function void () {a:integer=readInteger(); if(a!=0) printString("Non-zero"); else printString("Zero!!!");}"""
        expect = """main,:,function,void,(,),{,a,:,integer,=,readInteger,(,),;,if,(,a,!=,0,),printString,(,Non-zero,),;,else,printString,(,Zero!!!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 124))

    def test_empty_func(self):
        """"""
        testcase = """print: function void(){printString("Empty function!");}"""
        expect = """print,:,function,void,(,),{,printString,(,Empty function!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 125))

    def test_compare(self):
        """"""
        testcase = """main: function void () {printBoolean(2>3);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,2,>,3,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 126))

    def test_multiple_concat(self):
        """"""
        testcase = """main: function void () {str="abc"::"def"::("ghi"::"jkl");}"""
        expect = """main,:,function,void,(,),{,str,=,abc,::,def,::,(,ghi,::,jkl,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 127))

    def test_return_int_0(self):
        """"""
        testcase = """foo:function int(){return 0;}"""
        expect = """foo,:,function,int,(,),{,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 128))

    def test_return_float_0_001(self):
        """"""
        testcase = """foo:function float(){return 0.001;}"""
        expect = """foo,:,function,float,(,),{,return,0.001,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 129))

    def test_return_string_zero(self):
        """"""
        testcase = """foo:function string(){return "zero";}"""
        expect = """foo,:,function,string,(,),{,return,zero,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 130))

    def test_print_double_not(self):
        """"""
        testcase = """main: function void () {printBoolean(!!false);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,!,!,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 131))

    def test_print_triple_sign(self):
        """"""
        testcase = """main: function void () {printInteger(---3);}"""
        expect = """main,:,function,void,(,),{,printInteger,(,-,-,-,3,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 132))

    def test_fibo_function(self):
        """"""
        testcase = """fibonacci:function integer(n:integer){if(n==0)return 1;else return fibonacci(n-1)+fibonacci(n-2);}"""
        expect = """fibonacci,:,function,integer,(,n,:,integer,),{,if,(,n,==,0,),return,1,;,else,return,fibonacci,(,n,-,1,),+,fibonacci,(,n,-,2,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 133))

    def test_check_positive(self):
        """"""
        testcase = """main: function void () {if(n>0) printBoolean(true); else printBoolean(false);}"""
        expect = """main,:,function,void,(,),{,if,(,n,>,0,),printBoolean,(,true,),;,else,printBoolean,(,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 134))

    def test_break_down_string(self):
        """"""
        testcase = """main: function void () {breakDownString("Hello My Name Is Jeff");}"""
        expect = """main,:,function,void,(,),{,breakDownString,(,Hello My Name Is Jeff,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 135))

    def test_empty_array(self):
        """"""
        testcase = """arr:array[] of string={};"""
        expect = """arr,:,array,[,],of,string,=,{,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 136))

    def test_unknown_size_array(self):
        """"""
        testcase = """arr:array[] of string={"string1","string2","string3"};"""
        expect = """arr,:,array,[,],of,string,=,{,string1,,,string2,,,string3,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 137))

    def test_check_proplayer(self):
        """"""
        testcase = """main: function void () {if(level==max) printString("I\'m a global elite!!!"); else printString("I\'m noob :(");}"""
        expect = """main,:,function,void,(,),{,if,(,level,==,max,),printString,(,I'm a global elite!!!,),;,else,printString,(,I'm noob :(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 138))

    def test_check_rich(self):
        """"""
        testcase = """main: function void () {if(money>1e6) printString("I\'m rich!"); else printString("Poor peasant!!!");}"""
        expect = """main,:,function,void,(,),{,if,(,money,>,1e6,),printString,(,I'm rich!,),;,else,printString,(,Poor peasant!!!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 139))

    def test_bored(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str="bored") printString("You are bored af!"); else printString("Keep doing testcases then!");}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,if,(,str,=,bored,),printString,(,You are bored af!,),;,else,printString,(,Keep doing testcases then!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 140))

    def test_sleepy(self):
        """"""
        testcase = """main: function void () {str=readString(); if(str="sleepy") printString("To bed we go!"); else printString("Working we continue!");}"""
        expect = """main,:,function,void,(,),{,str,=,readString,(,),;,if,(,str,=,sleepy,),printString,(,To bed we go!,),;,else,printString,(,Working we continue!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 141))

    def test_print_discount(self):
        """"""
        testcase = """main: function void () {if(discount>0.05) printFloat(price*discount); else printFloat(price);}"""
        expect = """main,:,function,void,(,),{,if,(,discount,>,0.05,),printFloat,(,price,*,discount,),;,else,printFloat,(,price,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 142))

    def test_jeff(self):
        """"""
        testcase = """main: function void () {printString("Who are you?"); str:string="Ma nam is Jeff!";}"""
        expect = """main,:,function,void,(,),{,printString,(,Who are you?,),;,str,:,string,=,Ma nam is Jeff!,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 143))

    def test_dollar_to_vnd(self):
        """"""
        testcase = """main: function void () {n:float=readFloat(); writeFloat(24000*n);}"""
        expect = """main,:,function,void,(,),{,n,:,float,=,readFloat,(,),;,writeFloat,(,24000,*,n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 144))

    def test_check_only_divisible_by_5(self):
        """"""
        testcase = """main: function void () {n:integer=readInteger(); if(n%5==0 && n%10!=0) printBoolean(true); else printBoolean(false);}"""
        expect = """main,:,function,void,(,),{,n,:,integer,=,readInteger,(,),;,if,(,n,%,5,==,0,&&,n,%,10,!=,0,),printBoolean,(,true,),;,else,printBoolean,(,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 145))

    def test_pain(self):
        """"""
        testcase = """main: function void () {printString("I\'m in pain :(");}"""
        expect = """main,:,function,void,(,),{,printString,(,I'm in pain :(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 146))

    def test_gpa_10_to_4(self):
        """"""
        testcase = """main: function void () {n:float=readFloat(); writeFloat(n*4/10);}"""
        expect = """main,:,function,void,(,),{,n,:,float,=,readFloat,(,),;,writeFloat,(,n,*,4,/,10,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 147))

    def test_empty_if(self):
        """"""
        testcase = """main: function void () {if(true);}"""
        expect = """main,:,function,void,(,),{,if,(,true,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 148))

    def test_check_equal_to_3(self):
        """"""
        testcase = """main: function void () {printBoolean(1+1==3);}"""
        expect = """main,:,function,void,(,),{,printBoolean,(,1,+,1,==,3,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 149))

    def test_empty_if_else(self):
        """"""
        testcase = """main: function void () {if(true){}else{}}"""
        expect = """main,:,function,void,(,),{,if,(,true,),{,},else,{,},},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 150))

    def test_useless_loop(self):
        """"""
        testcase = """main: function void () {for(i=0,true,i+1) break;}"""
        expect = """main,:,function,void,(,),{,for,(,i,=,0,,,true,,,i,+,1,),break,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 151))

    def test_tired(self):
        """"""
        testcase = """main: function void () {printString("Sooooooooooooooo tired!!!!!!!!!!!!!!");}"""
        expect = """main,:,function,void,(,),{,printString,(,Sooooooooooooooo tired!!!!!!!!!!!!!!,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 152))

    def test_no_expr_while(self):
        """"""
        testcase = """main: function void () {while();}"""
        expect = """main,:,function,void,(,),{,while,(,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 153))

    def test_no_expr_do_while(self):
        """"""
        testcase = """main: function void () {do{}while()}"""
        expect = """main,:,function,void,(,),{,do,{,},while,(,),},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 154))

    def test_no_expr_if(self):
        """"""
        testcase = """main: function void () {if(){}}"""
        expect = """main,:,function,void,(,),{,if,(,),{,},},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 155))

    def test_missing_semi(self):
        """"""
        testcase = """main: function void () {if(true) print()}"""
        expect = """main,:,function,void,(,),{,if,(,true,),print,(,),},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 156))

    def test_missing_index(self):
        """"""
        testcase = """var_a:integer=arr[];"""
        expect = """var_a,:,integer,=,arr,[,],;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 157))

    def test_unkown_plusplus(self):
        """"""
        testcase = """n:integer=i++;"""
        expect = """n,:,integer,=,i,+,+,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 158))

    def test_missing_arg(self):
        """"""
        testcase = """main: function void () {foo(2,);}"""
        expect = """main,:,function,void,(,),{,foo,(,2,,,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 159))

    def test_missing_number(self):
        """"""
        testcase = """main: function void () {goo(4/);}"""
        expect = """main,:,function,void,(,),{,goo,(,4,/,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 160))

    def test_missing_closing_parenthesis(self):
        """"""
        testcase = """main: function void () {printInteger(;}"""
        expect = """main,:,function,void,(,),{,printInteger,(,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 161))

    def test_missing_openning_parenthesis(self):
        """"""
        testcase = """main: function void () {printFloat);}"""
        expect = """main,:,function,void,(,),{,printFloat,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 162))

    def test_missing_closing_curly(self):
        """"""
        testcase = """arr:array[] of float={1.3,5.6,4.2;"""
        expect = """arr,:,array,[,],of,float,=,{,1.3,,,5.6,,,4.2,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 163))

    def test_special_chars_string(self):
        """"""
        testcase = """main: function void () {printString("!@#$%^&*()\\\\\\t\\b\\n");}"""
        expect = """main,:,function,void,(,),{,printString,(,!@#$%^&*()\\\\\\t\\b\\n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 164))

    def test_array_of_booleans(self):
        """"""
        testcase = """arr:array[2] of boolean={true,false};"""
        expect = """arr,:,array,[,2,],of,boolean,=,{,true,,,false,},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 165))

    def test_compare_1(self):
        """"""
        testcase = """foo:function boolean(var_a:integer,var_b:integer){return a>b;}"""
        expect = """foo,:,function,boolean,(,var_a,:,integer,,,var_b,:,integer,),{,return,a,>,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 166))

    def test_compare_2(self):
        """"""
        testcase = """foo:function boolean(var_a:integer,var_b:integer){return a>=b;}"""
        expect = """foo,:,function,boolean,(,var_a,:,integer,,,var_b,:,integer,),{,return,a,>=,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 167))

    def test_compare_3(self):
        """"""
        testcase = """foo:function boolean(var_a:integer,var_b:integer){return a<b;}"""
        expect = """foo,:,function,boolean,(,var_a,:,integer,,,var_b,:,integer,),{,return,a,<,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 168))

    def test_compare_4(self):
        """"""
        testcase = """foo:function boolean(var_a:integer,var_b:integer){return a<b;}"""
        expect = """foo,:,function,boolean,(,var_a,:,integer,,,var_b,:,integer,),{,return,a,<,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 169))

    def test_compare_5(self):
        """"""
        testcase = """foo:function boolean(var_a:integer,var_b:integer){return a!=b;}"""
        expect = """foo,:,function,boolean,(,var_a,:,integer,,,var_b,:,integer,),{,return,a,!=,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 170))

    def test_compare_6(self):
        """"""
        testcase = """foo:function boolean(var_a:integer,var_b:integer){return a==b;}"""
        expect = """foo,:,function,boolean,(,var_a,:,integer,,,var_b,:,integer,),{,return,a,==,b,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 171))

    def test_compare_7(self):
        """"""
        testcase = """foo:function boolean(var_a:float,var_b:float) return a-b<10e-9;"""
        expect = """foo,:,function,boolean,(,var_a,:,float,,,var_b,:,float,),return,a,-,b,<,10e-9,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 172))

    def test_power_of_2(self):
        """"""
        testcase = """get_power2:function integer(n:integer){return n*n;}"""
        expect = """get_power2,:,function,integer,(,n,:,integer,),{,return,n,*,n,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 173))

    def test_power_of_3(self):
        """"""
        testcase = """get_power3:function integer(n:integer){return n*n*n;}"""
        expect = """get_power3,:,function,integer,(,n,:,integer,),{,return,n,*,n,*,n,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 174))

    def test_sqrt(self):
        """"""
        testcase = """get_sqrt: function float(n:integer) {return sqrt(n);}"""
        expect = """get_sqrt,:,function,float,(,n,:,integer,),{,return,sqrt,(,n,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 175))

    def test_get_negative(self):
        """"""
        testcase = """get_negative: function float(n:float) {if(n>0) return -n; return n;}"""
        expect = """get_negative,:,function,float,(,n,:,float,),{,if,(,n,>,0,),return,-,n,;,return,n,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 176))

    def test_sum_of_array(self):
        """"""
        testcase = """main: function void () {sum:integer=0; n=readInteger(); for(i=0,i<n,i+1) sum=sum+i; printInteger(sum);}"""
        expect = """main,:,function,void,(,),{,sum,:,integer,=,0,;,n,=,readInteger,(,),;,for,(,i,=,0,,,i,<,n,,,i,+,1,),sum,=,sum,+,i,;,printInteger,(,sum,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 177))

    def test_sum_of_even_elem(self):
        """"""
        testcase = """main: function void () {sum:integer=0; n=readInteger(); for(i=0,i<n,i+1) if(i%2==0) sum=sum+i; printInteger(sum);}"""
        expect = """main,:,function,void,(,),{,sum,:,integer,=,0,;,n,=,readInteger,(,),;,for,(,i,=,0,,,i,<,n,,,i,+,1,),if,(,i,%,2,==,0,),sum,=,sum,+,i,;,printInteger,(,sum,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 178))

    def test_sum_of_odd_elem(self):
        """"""
        testcase = """main: function void () {sum:integer=0; n=readInteger(); for(i=0,i<n,i+1)  if(i%2==1) sum=sum+i; printInteger(sum);}"""
        expect = """main,:,function,void,(,),{,sum,:,integer,=,0,;,n,=,readInteger,(,),;,for,(,i,=,0,,,i,<,n,,,i,+,1,),if,(,i,%,2,==,1,),sum,=,sum,+,i,;,printInteger,(,sum,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 179))

    def test_auto_var_noExpr(self):
        """"""
        testcase = """var_a:auto;"""
        expect = """var_a,:,auto,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 180))

    def test_auto_var_withExpr1(self):
        """"""
        testcase = """var_a:auto=3;"""
        expect = """var_a,:,auto,=,3,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 181))

    def test_auto_var_withExpr2(self):
        """"""
        testcase = """var_b:auto=3e-6;"""
        expect = """var_b,:,auto,=,3e-6,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 182))

    def test_auto_var_withExpr3(self):
        """"""
        testcase = """var_c:boolean=true||false;"""
        expect = """var_c,:,boolean,=,true,||,false,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 183))

    def test_unkown_type1(self):
        """"""
        testcase = """var_a:flaot;"""
        expect = """var_a,:,flaot,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 184))

    def test_unkown_type2(self):
        """"""
        testcase = """var_b:atuo;"""
        expect = """var_b,:,atuo,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 185))

    def test_unkown_type3(self):
        """"""
        testcase = """var_c:sitrng;"""
        expect = """var_c,:,sitrng,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 186))

    def test_incomplete_expr(self):
        """"""
        testcase = """var_a:auto=;"""
        expect = """var_a,:,auto,=,;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 187))

    def test_incorrect_keywords_order(self):
        """"""
        testcase = """foo:function void(out inherit id:integer){}"""
        expect = """foo,:,function,void,(,out,inherit,id,:,integer,),{,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 188))

    def test_string_expr_sucess(self):
        """"""
        testcase = """main: function void () {str="abc"::("def"::("ghi"::"jkl"));}"""
        expect = """main,:,function,void,(,),{,str,=,abc,::,(,def,::,(,ghi,::,jkl,),),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 189))

    def test_compare_string_expr_success(self):
        """"""
        testcase = """main: function void() {compare=a< (b > c) :: (a > b);}"""
        expect = """main,:,function,void,(,),{,compare,=,a,<,(,b,>,c,),::,(,a,>,b,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 190))

    def test_conditional_expr_in_if(self):
        """"""
        testcase = """main: function void () {n:integer=readInteger(); if((n%5==0) && (n%10!=0)) printBoolean(true); else printBoolean(false);}"""
        expect = """main,:,function,void,(,),{,n,:,integer,=,readInteger,(,),;,if,(,(,n,%,5,==,0,),&&,(,n,%,10,!=,0,),),printBoolean,(,true,),;,else,printBoolean,(,false,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 191))

    def test_MT22_header(self):
        """"""
        testcase = """grammar MT22;

    @lexer::header {
    from lexererr import *
    }

    options{
            language=Python3;
    }"""
        expect = """grammar,MT22,;,Error Token @"""
        self.assertTrue(TestLexer.test(testcase, expect, 192))

    def test_MT22_header_2(self):
        """"""
        testcase = """lexer::header {
    from lexererr import *
    }

    options{
            language=Python3;
    }"""
        expect = """lexer,::,header,{,from,lexererr,import,*,},options,{,language,=,Python3,;,},<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 193))

    def test_array__(self):
        """"""
        testcase = """a:array[1_8, 2_0_90_1, 12] of integer = {{12,0}, 1_3, {{{3_2}}}};"""
        expect = """a,:,array,[,18,,,20901,,,12,],of,integer,=,{,{,12,,,0,},,,13,,,{,{,{,32,},},},},;,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 194))

    def test_C_comment(self):
        """"""
        testcase = """/** C 2011 grammar built from the C11 Spec */
    /** C 2011 grammar built from the C11 Spec *****/
    // /* C 2011 grammar built from the C11 Spec
    */"""
        expect = """*,/,<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 195))

    def test_quote_enter_quote(self):
        """"""
        testcase = """ "

    " """
        expect = """Unclosed String: """
        self.assertTrue(TestLexer.test(testcase, expect, 196))

    def test_py_multiline_string(self):
        """"""
        testcase = """""" """"""
        expect = """<EOF>"""
        self.assertTrue(TestLexer.test(testcase, expect, 197))

    def test_keyword(self):
        """"""
        self.assertTrue(TestLexer.test("sTRIng false", "sTRIng,false,<EOF>", 198))

    def test_comment_identifier(self):
        self.assertTrue(TestLexer.test("/*hello my friend \n nothinghjhj \n love */ ntp", "ntp,<EOF>", 199))

