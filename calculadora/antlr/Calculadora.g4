grammar Calculadora;

program : statement* EOF ;

statement
    : assignStmt ';'                       # assignStatement
    | ifStmt                               # ifStatement
    ;

assignStmt
    : ID '=' expr                          # assign
    ;

ifStmt
    : 'if' '(' condition ')' block         # ifStructure
    ;

condition
    : expr relop expr                      # compare
    ;

relop : '>' | '<' | '>=' | '<=' | '==' | '!=' ;

block
    : '{' statement* '}'                   # codeBlock
    ;

expr
    : expr op=('*'|'/') expr               # MulDiv
    | expr op=('+'|'-') expr               # AddSub
    | ID                                   # Id
    | INT                                  # Int
    | '(' expr ')'                         # Parens
    ;

ID  : [a-zA-Z_] [a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;