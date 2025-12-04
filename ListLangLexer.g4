lexer grammar ListLangLexer;

// Artificial tokens only for parser purposes


tokens { INDENT, DEDENT }

@lexer::header{
from ListLangDenterHelper import ListLangDenterHelper
from gen.ListLangParser import ListLangParser
}

@lexer::members {
denter = None

def nextToken(self):
    if not self.denter:
        self.denter = ListLangDenterHelper(
            self,
            self.NEWLINE,
            ListLangParser.INDENT,
            ListLangParser.DEDENT,
            False
        )
    return self.denter.next_token()
}

// --- Operators ---
// Logical



AND : '&&';
OR  : '||';
NOT : '!';
AMP  : '&'; // используется для передачи по результату



// Relations
LESS_THAN       : '<';
GREATER_THAN    : '>';
EQUALS          : '==';
LT_EQ           : '<=';
GT_EQ           : '>=';
NOT_EQ          : '!=';

ASSIGNMENT      : '=';

// Arithmetic
ADD         : '+';
MINUS       : '-';
MULT        : '*';
DIV         : '/';
MOD         : '%';

// --- Delimeters ---
DOT             : '.';
COMMA           : ',';
COLON           : ':';
SEMI_COLON      : ';';
OPEN_PAREN      : '(';
CLOSE_PAREN     : ')';
OPEN_BRACE      : '{';
CLOSE_BRACE     : '}';
OPEN_BRACKET    : '[';
CLOSE_BRACKET   : ']';

// --- Keywords ---
FUNC    : 'func';
RETURN  : 'return';
IF      : 'if';
ELSE    : 'else';
SWITCH  : 'switch';
CASE    : 'case';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
DEFAULT : 'default';
BREAK   : 'break';

// --- Literals ---
BOOLEAN         : 'true' | 'false' ;
FLOAT_NUMBER    : [0-9]* '.' [0-9]+ | [0-9]+ '.';
DECIMAL_INTEGER : [1-9] [0-9]* | '0'+;
STRING          : '"' ( ~["\\] | '\\' . )* '"' ;

NAME    : ID_START ID_CONTINUE*;

// --- Terminals ---
COMMENT : '#' ~[\r\n]* -> skip ;
NEWLINE : '\r'? '\n' ;
WS      : [ \t]+ -> skip ;

// --- Fragments ---

fragment ID_START:
    [A-Z]
    |[a-z]
    ;

fragment ID_CONTINUE:
    ID_START
    |[0-9]
    |'_'
    ;