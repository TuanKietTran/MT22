import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_Label(self):
        """Description"""
        input = """Testcase"""
        expect = """Expect"""
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_short_decl_1_id(self):
        """basic declaration"""
        input = """a:float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_full_decl_1_id(self):
        """"""
        input = """a:float=1;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_full_decl_2_ids(self):
        """"""
        input = """a,b:float=1,2;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_full_decl_unbalance(self):
        """"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = """Error on line 1 col 29: ;"""
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_func_def(self):
        """"""
        input = """main: function void() {}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_func_1_stmt(self):
        """"""
        input = """abc: function integer() {a = 1;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_func_block_stmt(self):
        """"""
        input = """abc: function integer() {{}}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_func_def_func_call(self):
        """"""
        input = """abc: function integer() {abc();}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_func_stmts_return(self):
        """"""
        input = """abc: function integer() {a=1;
            b=1;
            return 0;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_short_decl_2_ids(self):
        """"""
        input = """a,b:float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_miss_semi(self):
        """"""
        input = """a,b:float=1,2"""
        expect = """Error on line 1 col 13: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_miss_colon(self):
        """"""
        input = """a,b float=1,2;"""
        expect = """Error on line 1 col 4: float"""
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_miss_id(self):
        """"""
        input = """:float=1;"""
        expect = """Error on line 1 col 0: :"""
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_miss_exp_full_decl(self):
        """"""
        input = """a:float=;"""
        expect = """Error on line 1 col 8: ;"""
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_miss_assign(self):
        """"""
        input = """a:float 1;"""
        expect = """Error on line 1 col 8: 1"""
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_miss_type_assign(self):
        """"""
        input = """a:1;"""
        expect = """Error on line 1 col 2: 1"""
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_line_cmt(self):
        """"""
        input = """//abc: functionwshjfuiovhsiuod void(){}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_decl_list(self):
        """"""
        input = """a:float;
            abc:function void(){}
            //end
            b:integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_block_cmt(self):
        """"""
        input = """/*@@@@@@@@@@@@@*/
    a:integer=1+a;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_line_cmt_many(self):
        """"""
        input = """///////////////////
            a:integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_string_expr(self):
        """"""
        input = """main: function void () {a= "abc"::"xyz";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_call_expr(self):
        """"""
        input = """main: function void() {
        printString("abc")
    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_assign_expr(self):
        """"""
        input = """main: function void () {a= "abc";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_full_decl_string(self):
        """"""
        input = """a,b,c:string= "abc","a","""""
        expect = """Error on line 1 col 24: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_full_decl_str_unbalance(self):
        """"""
        input = """a,b,c:string= "a","a" ;"""
        expect = """Error on line 1 col 22: ;"""
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_func_is_even(self):
        """"""
        input = """isEven: function boolean(a:integer){if(a%2==0) return true; else return false;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_io_integer(self):
        """"""
        input = """main: function void () {a=readInteger(); printInteger(a);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_io_float(self):
        """"""
        input = """main: function void () {n=readFloat(); printFloat(n);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_io_string(self):
        """"""
        input = """main: function void () {str=readString(); printString(str);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_short_decl_array_2d(self):
        """"""
        input = """arr: array[5,5] of integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_short_decl_array_1d(self):
        """"""
        input = """arr: array[10] of integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_full_decl_array_1d(self):
        """"""
        input = """arr: array[5] of integer={1,2,3,4,5};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_full_decl_array_1d(self):
        """"""
        input = """arr: array[5,5] of integer={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_print_int_cal(self):
        """"""
        input = """main: function void () {printInteger(10+11);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_print_float_cal(self):
        """"""
        input = """main: function void () {printFloat(2e-7+3e-1);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_print_bool_cal(self):
        """"""
        input = """main: function void () {printBoolean(var_a && var_b || var_c);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_bool_cal(self):
        """"""
        input = """main: function void () {value=true && false || true;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_super_func(self):
        """"""
        input = """main: function void () {super("name",age);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_preventDefault(self):
        """"""
        input = """main: function void () {preventDefault();}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_cal_C_of_circle(self):
        """"""
        input = """main: function void () {r=readFloat(); pi=3.14; C=2*r*pi; writeFloat(C);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_cal_absolute(self):
        """"""
        input = """main: function void () {abs(100-560-741);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_get_fibonum(self):
        """"""
        input = """main: function void () {fibonacci(5);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_convert_to_string(self):
        """"""
        input = """main: function void () {stringConverter(120.485);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_print_string(self):
        """"""
        input = """main: function void () {printString("Hello World!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_print_string_2(self):
        """"""
        input = """str:string="Hello \\nWorld!";"""
        expect = """Illegal Escape !!!"""
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_print_string_3(self):
        """"""
        input = """str:string="Hello World!"""
        expect = """Unclose String !!!"""
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_assign_int_expr(self):
        """"""
        input = """a:integer=5+6-(123*10+(24-30));"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_assign_int_list(self):
        """"""
        input = """a,b,c:intger=2,3;"""
        expect = """Error on line 1 col 6: intger"""
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_print_elem(self):
        """"""
        input = """main: function void () {printInteger(arr[0,1]);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_assign_elem(self):
        """"""
        input = """main: function void () {arr[3]=3.14;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_validate_zero(self):
        """"""
        input = """main: function void () {a:integer=readInteger(); if(a!=0) printString("Non-zero"); else printString("Zero!!!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_empty_func(self):
        """"""
        input = """print: function void(){printString("Empty function!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_compare(self):
        """"""
        input = """main: function void () {printBoolean(2>3);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_multiple_concat(self):
        """"""
        input = """main: function void () {str="abc"::"def"::("ghi"::"jkl");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_return_int_0(self):
        """no viable alternative at input 'foo:functionint'"""
        input = """foo:function int(){return 0;}"""
        expect = """Error on line 1 col 13: int"""
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_return_float_0_001(self):
        """"""
        input = """foo:function float(){return 0.001;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_return_string_zero(self):
        """"""
        input = """foo:function string(){return "zero";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_print_double_not(self):
        """"""
        input = """main: function void () {printBoolean(!!false);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_print_triple_sign(self):
        """"""
        input = """main: function void () {printInteger(---3);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_fibo_function(self):
        """"""
        input = """fibonacci:function integer(n:integer){if(n==0)return 1;else return fibonacci(n-1)+fibonacci(n-2);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_check_positive(self):
        """"""
        input = """main: function void () {if(n>0) printBoolean(true); else printBoolean(false);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_break_down_string(self):
        """"""
        input = """main: function void () {breakDownString("Hello My Name Is Jeff");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_empty_array(self):
        """"""
        input = """arr:array[] of string={};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_unknown_size_array(self):
        """"""
        input = """arr:array[] of string={"string1","string2","string3"};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_check_proplayer(self):
        """"""
        input = """main: function void () {if(level==max) printString("I\'m a global elite!!!"); else printString("I\'m noob :(");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_check_rich(self):
        """"""
        input = """main: function void () {if(money>1e6) printString("I\'m rich!"); else printString("Poor peasant!!!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_another_float(self):
        """"""
        input = """var_a:float=1.547e-3;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_big_float(self):
        """"""
        input = """var_a:float=1.5e10;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_sum_of_two(self):
        """"""
        input = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a+b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_subtraction_of_two(self):
        """"""
        input = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a-b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_multiplication_of_two(self):
        """"""
        input = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a*b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_division_of_two(self):
        """"""
        input = """main: function void () {a:integer=readInteger(); b:integer=readInteger(); printInteger(a/b);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_print_loop(self):
        """"""
        input = """n:integer=readInteger(); main: function void () {for(i=0,i<n,i+1) printInteger(i);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_infinite_empty_loop(self):
        """"""
        input = """main: function void () {while(true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_infinite_loop(self):
        """"""
        input = """main: function void () {do{printString("looping!");}while(true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_athur_morgan(self):
        """"""
        input = """main: function void () {str=readString(); if(str=="Athur Morgan") printString("Wanted: dead or alive $5000+");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_bored(self):
        """"""
        input = """main: function void () {str=readString(); if(str="bored") printString("You are bored af!"); else printString("Keep doing testcases then!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_sleepy(self):
        """"""
        input = """main: function void () {str=readString(); if(str="sleepy") printString("To bed we go!"); else printString("Working we continue!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_print_discount(self):
        """"""
        input = """main: function void () {if(discount>0.05) printFloat(price*discount); else printFloat(price);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_jeff(self):
        """"""
        input = """main: function void () {printString("Who are you?"); str:string="Ma nam is Jeff!";}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_dollar_to_vnd(self):
        """"""
        input = """main: function void () {n:float=readFloat(); writeFloat(24000*n);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_check_only_divisible_by_5(self):
        """n%5==0 && n%10!=0 -> (n%5)==(0 && (n %10)) != 0
      None Associative"""
        input = """main: function void () {n:integer=readInteger(); if(n%5==0 && n%10!=0) printBoolean(true); else printBoolean(false);}"""
        expect = """Error on line 1 col 66: !="""
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_pain(self):
        """"""
        input = """main: function void () {printString("I\'m in pain :(");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_gpa_10_to_4(self):
        """"""
        input = """main: function void () {n:float=readFloat(); writeFloat(n*4/10);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_empty_if(self):
        """"""
        input = """main: function void () {if(true);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_check_equal_to_3(self):
        """"""
        input = """main: function void () {printBoolean(1+1==3);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_empty_if_else(self):
        """"""
        input = """main: function void () {if(true){}else{}}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_useless_loop(self):
        """"""
        input = """main: function void () {for(i=0,true,i+1) break;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_tired(self):
        """"""
        input = """main: function void () {printString("Sooooooooooooooo tired!!!!!!!!!!!!!!");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_no_expr_while(self):
        """"""
        input = """main: function void () {while();}"""
        expect = """Error on line 1 col 30: )"""
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_no_expr_do_while(self):
        """"""
        input = """main: function void () {do{}while()}"""
        expect = """Error on line 1 col 34: )"""
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_no_expr_if(self):
        """"""
        input = """main: function void () {if(){}}"""
        expect = """Error on line 1 col 27: )"""
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_missing_semi(self):
        """"""
        input = """main: function void () {if(true) print()}"""
        expect = """Error on line 1 col 40: }"""
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_missing_index(self):
        """"""
        input = """var_a:integer=arr[];"""
        expect = """Error on line 1 col 18: ]"""
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_unkown_plusplus(self):
        """"""
        input = """n:integer=i++;"""
        expect = """Error on line 1 col 12: +"""
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_missing_arg(self):
        """"""
        input = """main: function void () {foo(2,);}"""
        expect = """Error on line 1 col 30: )"""
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_missing_number(self):
        """"""
        input = """main: function void () {goo(4/);}"""
        expect = """Error on line 1 col 30: )"""
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_missing_closing_parenthesis(self):
        """"""
        input = """main: function void () {printInteger(;}"""
        expect = """Error on line 1 col 37: ;"""
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_missing_openning_parenthesis(self):
        """"""
        input = """main: function void () {printFloat);}"""
        expect = """Error on line 1 col 34: )"""
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_missing_closing_curly(self):
        """"""
        input = """arr:array[] of float={1.3,5.6,4.2;"""
        expect = """Error on line 1 col 10: ]"""
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_special_chars_string(self):
        """"""
        input = """main: function void () {printString("!@#$%^&*()\\\\\\t\\b\\n");}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 301))

    def test_array_of_booleans(self):
        """"""
        input = """arr:array[2] of boolean={true,false};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 302))

    def test_compare_1(self):
        """"""
        input = """foo:function boolean(var_a:integer,var_b:integer){return a>b;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 303))

    def test_compare_2(self):
        """"""
        input = """foo:function boolean(var_a:integer,var_b:integer){return a>=b;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_compare_3(self):
        """"""
        input = """foo:function boolean(var_a:integer,var_b:integer){return a<b;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 305))

    def test_compare_4(self):
        """"""
        input = """foo:function boolean(var_a:integer,var_b:integer){return a<b;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_compare_5(self):
        """"""
        input = """foo:function boolean(var_a:integer,var_b:integer){return a!=b;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 307))

    def test_compare_6(self):
        """"""
        input = """foo:function boolean(var_a:integer,var_b:integer){return a==b;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 308))

    def test_compare_7(self):
        """no block-statement"""
        input = """foo:function boolean(var_a:float,var_b:float) return a-b<10e-9;"""
        expect = """Error on line 1 col 46: return"""
        self.assertTrue(TestParser.test(input, expect, 309))

    def test_power_of_2(self):
        """"""
        input = """get_power2:function integer(n:integer){return n*n;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 310))

    def test_power_of_3(self):
        """"""
        input = """get_power3:function integer(n:integer){return n*n*n;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 311))

    def test_sqrt(self):
        """"""
        input = """get_sqrt: function float(n:integer) {return sqrt(n);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 312))

    def test_get_negative(self):
        """"""
        input = """get_negative: function float(n:float) {if(n>0) return -n; return n;}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 313))

    def test_sum_of_array(self):
        """"""
        input = """main: function void () {sum:integer=0; n=readInteger(); for(i=0,i<n,i+1) sum=sum+i; printInteger(sum);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 314))

    def test_sum_of_even_elem(self):
        """"""
        input = """main: function void () {sum:integer=0; n=readInteger(); for(i=0,i<n,i+1) if(i%2==0) sum=sum+i; printInteger(sum);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 315))

    def test_sum_of_odd_elem(self):
        """"""
        input = """main: function void () {sum:integer=0; n=readInteger(); for(i=0,i<n,i+1)  if(i%2==1) sum=sum+i; printInteger(sum);}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 316))

    def test_auto_var_noExpr(self):
        """"""
        input = """var_a:auto;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 317))

    def test_auto_var_withExpr1(self):
        """"""
        input = """var_a:auto=3;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 318))

    def test_auto_var_withExpr2(self):
        """"""
        input = """var_b:auto=3e-6;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 319))

    def test_auto_var_withExpr3(self):
        """"""
        input = """var_c:boolean=true||false;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 320))

    def test_unkown_type1(self):
        """"""
        input = """var_a:flaot;"""
        expect = """Error on line 1 col 6: flaot"""
        self.assertTrue(TestParser.test(input, expect, 321))

    def test_unkown_type2(self):
        """"""
        input = """var_b:atuo;"""
        expect = """Error on line 1 col 6: atuo"""
        self.assertTrue(TestParser.test(input, expect, 322))

    def test_unkown_type3(self):
        """"""
        input = """var_c:sitrng;"""
        expect = """Error on line 1 col 6: sitrng"""
        self.assertTrue(TestParser.test(input, expect, 323))

    def test_incomplete_expr(self):
        """"""
        input = """var_a:auto=;"""
        expect = """Error on line 1 col 11: ;"""
        self.assertTrue(TestParser.test(input, expect, 324))

    def test_incorrect_keywords_order(self):
        """"""
        input = """foo:function void(out inherit id:integer){}"""
        expect = """Error on line 1 col 22: inherit"""
        self.assertTrue(TestParser.test(input, expect, 325))

    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 298))
    #
    # def test_full_definition(self):
    #     input = """a, b, c, d: integer = 3, 4, 6;"""
    #     expect = "Error on line 1 col 29: ;"
    #     self.assertTrue(TestParser.test(input, expect, 299))