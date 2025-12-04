parser grammar ListLangParser;

options {
    tokenVocab=ListLangLexer;
}

program : NEWLINE* (statement (NEWLINE*) )* EOF;


// --- Statements ---

// -- Simple statements --
simple_stmt
    : expression_stmt
    | assignment_stmt
    | return_stmt
    | break_stmt
    ;

assignment_stmt
    : target_list ASSIGNMENT expression_list
    ;

target_list
    : NAME (COMMA NAME)*
    ;

expression_stmt
    : expression
    ;

return_stmt
    : RETURN expression_list
    ;

break_stmt
    : BREAK
    ;

// -- Compound statements --

compound_statement
    : func_decl
    | if_statement
    | while_statement
    | for_statement
    | switch_statement
    ;

suite
    : statement NEWLINE
    | NEWLINE+ INDENT statement+ DEDENT
    ;

statement
    : stmt_list NEWLINE
    | compound_statement
    | NEWLINE // TODO
    ;

stmt_list
    : simple_stmt (SEMI_COLON simple_stmt)*
    ;

// - Functions -
func_decl:
    FUNC NAME OPEN_PAREN parameter_list? CLOSE_PAREN COLON suite;

parameter_list
    : param (COMMA param)*
    ;

param
    : AMP? NAME
    ;

// - If statement
if_statement
    : IF expression COLON suite
    (ELSE COLON suite)?
    ;

while_statement
    : WHILE expression COLON suite
    ;

for_statement
    : FOR target_list IN expression_list COLON suite
    ;

switch_statement
    : SWITCH expression COLON NEWLINE
    INDENT
    case_block+
    default_block?
    DEDENT
    ;

case_block
    : CASE expression COLON suite
    ;

default_block
    : DEFAULT COLON suite
    ;


// --- Expressions ---
expression_list
    : expression (COMMA expression)*
    ;

expression
    : expression op=(MULT | DIV | MOD) expression
    | expression op=(ADD | MINUS) expression
    | expression op=(EQUALS | NOT_EQ | LESS_THAN | GREATER_THAN | LT_EQ | GT_EQ) expression
    | expression op=(AND | OR) expression
    | NOT expression
    | atom
    ;

atom
    : literal
    | NAME
    | NAME DOT NAME                                         // member access
    | NAME DOT NAME OPEN_PAREN arg_list? CLOSE_PAREN  // method call
    | NAME OPEN_PAREN arg_list? CLOSE_PAREN           // func call
    | OPEN_PAREN expression CLOSE_PAREN
    ;

arg_list
    : expression (COMMA expression)*
    ;

// --- Literals ---

literal
    : DECIMAL_INTEGER
    | FLOAT_NUMBER
    | STRING
    | BOOLEAN
    | OPEN_BRACKET CLOSE_BRACKET   // []
    ;

