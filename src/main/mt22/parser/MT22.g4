/*
    Ho Chi Minh City University of Technology - HCMUT
    Principle of programming language - CO3005
    Tran Ha Tuan Kiet - 2011493
    Feb 10, 2023
    MT22 Specification
*/

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*Basic concepts*/

compilationUnit: translationUnit EOF ;

/* Declaration */

translationUnit
    :   externalDeclaration translationUnit
    |   externalDeclaration
    ;

externalDeclaration
    :   functionDeclaration
    |   declaration
    ;

declaration
    :   (shortDeclaration | fullDeclaration) Semi
    ;

identifierList
    :   Identifier Comma identifierList
    |   Identifier
    ;

shortDeclaration
    :   identifierList Colon typeSpecifier
    ;


fullDeclaration
    :   Identifier Comma fullDeclaration Comma expression
    |   Identifier Colon typeSpecifier Assign expression
    ;


functionDeclaration
    :   Identifier Colon Function typeSpecifier paramDeclarator inheritance compoundStatement
    ;

paramDeclarator
    :   LeftParen (parameterList |) RightParen
    ;

inheritance
    :   Inherit Identifier
    |
    ;

parameterList
    :   parameter Comma parameterList
    |   parameter
    ;

parameter
    :   (Inherit |) (Out |) Identifier Colon typeSpecifier
    ;

typeSpecifier
    :   atomicType
    |   voidType
    |   arrayType
    ;

atomicType
    :   Integer
    |   Bool
    |   Float
    |   String
    ;

voidType
    :   Void
    ;

arrayType
    :   Array LeftBracket dimension RightBracket Of atomicType
    ;

dimension
    :   IntegerLiteral Comma dimension
    |   IntegerLiteral
    ;

/* Statements */

statement
    :   compoundStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
    ;

compoundStatement
    :   LeftBrace (blockItemList |) RightBrace
    ;

blockItemList
    :   blockItem blockItemList
    |   blockItem
    ;

blockItem
    :   statement
    |   declaration
    ;

expressionStatement
    :   expression Semi
    ;

selectionStatement
    :   If LeftParen expression RightParen statement ((Else statement) | )
    ;

iterationStatement
    :   While LeftParen expression RightParen statement
    |   Do statement While LeftParen expression RightParen Semi
    |   For LeftParen forCondition RightParen statement
    ;

//    |   'for' LeftParen expression? ';' expression?  ';' forUpdate? RightParen statement
//    |   For LeftParen declaration  expression? ';' expression? RightParen statement

forCondition
	:   forDeclaration Colon conditionExpression Colon updateExpression
	;

forDeclaration
    : Identifier Equal expression
    ;

conditionExpression
    :   assignmentExpression (',' assignmentExpression)*
    ;

updateExpression
    :   stringExpression
    ;

jumpStatement
    :   (
            Return (expression | )
        |   ( Continue | Break )
        )   Semi
    ;

/* Expressions */
expression
    :   assignmentExpression Comma expression
    |   assignmentExpression
    ;

assignmentExpression
    :   stringExpression
    |   unaryExpression Assign assignmentExpression
    ;

stringExpression
    :   relationalExpression Doublecolon relationalExpression
    |   relationalExpression
    ;

relationalExpression
    :   logicalExpression (Less|Greater|LessEqual|GreaterEqual |Equal| NotEqual) logicalExpression
    |   logicalExpression
    ;

logicalExpression
    :   logicalExpression (AndAnd | OrOr) additiveExpression
    |   additiveExpression
    ;

additiveExpression
    :   additiveExpression (Plus | Minus) multiplicativeExpression
    |   multiplicativeExpression
    ;

multiplicativeExpression
    :   unaryExpression (Star| Slash | Mod) multiplicativeExpression
    |   unaryExpression
    ;



unaryExpression
    :   postfixExpression
    |   unaryOperator Identifier
    ;

unaryOperator
    :   Minus
    |   Not
    ;

primaryExpression
    :   Identifier
    |   literal
    |   LeftParen expression RightParen
    ;

postfixExpression
    :   primaryExpression
	|   postfixExpression LeftBracket expression RightBracket
	|   postfixExpression LeftParen (expression| ) RightParen
	;




literal
    :   IntegerLiteral
    |   FloatingLiteral
    |   StringLiteral
    |   BooleanLiteral
    ;

/*--TOKENS--*/

/*Keywords*/

Array: 'array';

Auto: 'auto';

Bool: 'bool';

Break: 'break';

Continue: 'continue';

Do: 'do';

Else: 'else';

False_: 'false';

Float: 'float';

For: 'for';

Function: 'function';

If: 'if';

Inherit: 'inherit';

Integer: 'integer';

Of: 'of';

Out: 'out';

Return: 'return';

String: 'string';

True_: 'true';

While: 'while';

Void: 'void';

/*Seperators*/

LeftParen: '(';

RightParen: ')';

LeftBracket: '[';

RightBracket: ']';

LeftBrace: '{';

RightBrace: '}';

Assign: '=';

Comma: ',';

Colon: ':';

Semi: ';';

Dot: '.';

/*Operators*/
Plus: '+';

Minus: '-';

Star: '*';

Slash: '/';

Mod: '%';

Not: '!';

AndAnd: '&&';

OrOr: '||';

Equal: '==';

NotEqual: '!=';

LessEqual: '<=';

GreaterEqual: '>=';

Less: '<';

Greater: '>';

Doublecolon: '::';

/* Literal */

IntegerLiteral
    :   Digitsequence
    ;

FloatingLiteral
    :   Digitsequence DecimalPart ExponentPart?
	|   Digitsequence DecimalPart? ExponentPart
	|   Digitsequence? DecimalPart ExponentPart
	;

BooleanLiteral: False_ | True_;

StringLiteral: '"' StringCharacter* '"' {self.text = self.text[1:-1]};

/*  */

Identifier
    :   [a-zA-Z_][a-zA-Z_0-9]*
    ;

fragment DIGIT: [0-9];

fragment NONZERODIGIT: [1-9];

fragment SIGN: [+-];

fragment Digitsequence
    :   '0' | NONZERODIGIT ('_'? DIGIT)*  {self.text = self.text.replace("_", "")}
    ;

fragment DecimalPart
    :   '.' DIGIT*
    ;

fragment ExponentPart
    :   [eE] SIGN? DIGIT+
    ;

fragment StringCharacter
    :   ~["\\\r\n] | EscapeSequence
    ;

fragment EscapeSequence
	:   '\\' [btnfr"'\\]
	;

Whitespace
    :   [ \t\r\n\b\f]+ -> skip
    ; // skip spaces, tabs, newlines, backspace, feed

Newline: '\n' -> skip;

/* Comment */
BlockComment: '/*' .*? '*/' -> skip;

LineComment: '//' ~ [\r\n]* -> skip;


UNCLOSE_STRING: '"' StringCharacter*  EOF? {
		y = str(self.text)
		raise UncloseString(y[0:])
	};

ILLEGAL_ESCAPE: '"' StringCharacter* ('\\' ~[bfrnt"\\]) {
		y = str(self.text)
		raise IllegalEscape(y[0:])
	};

ERROR_CHAR: .{raise ErrorToken(self.text)};
