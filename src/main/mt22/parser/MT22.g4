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
    :   functionDefinition
    |   declaration
    ;

declaration
    :   shortDeclaration
    |   fullDeclaration
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
    |   Identifier (Colon typeSpecifier Equal) expression
    ;


functionDefinition
    :   Identifier Colon Function typeSpecifier LeftParen parameterList RightParen inheritance compoundStatement
    ;


inheritance
    :   Inherit Identifier
    |
    ;



parameterList
    :   (Inherit |) (Out |) identifierList
    ;

typeSpecifier
    :   Integer
    |   Bool
    |   Float
    |   String
    |   Void
    ;

statement
    :   compoundStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    ;

compoundStatement
    :   LeftBrace blockItemList? LeftBrace
    ;

blockItemList
    :   blockItem+
    ;

blockItem
    :   statement
    |   declaration
    ;

expressionStatement
    :   expression? Semi
    ;

selectionStatement
    :   If LeftParen expression RightParen statement (Else statement)?
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
    :
    ;

forExpression
    :   assignmentExpression (',' assignmentExpression)*
    ;

updateExpression

expression
    :
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

Div: '/';

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
    :   Digitsequence {self.text = self.text.replace("_", "")}
    ;

FloatingLiteral
    :   Digitsequence DecimalPart ExponentPart? {self.text = self.text.replace("_", "")}
	|   Digitsequence DecimalPart? ExponentPart {self.text = self.text.replace("_", "")}
	|   Digitsequence? DecimalPart ExponentPart {self.text = self.text.replace("_", "")}
	;

BooleanLiteral: False_ | True_;

StringLiteral: '"' StringCharacter* '"';

/*  */

Identifier
    :   [a-z_A-Z][a-z_A-Z0-9]+
    ;

fragment DIGIT: [0-9];

fragment NONZERODIGIT: [1-9];

fragment SIGN: [+-];

fragment Digitsequence
    :   '0' | NONZERODIGIT ('_'? DIGIT)*
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
