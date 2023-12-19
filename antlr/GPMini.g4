grammar GPMini;

program: statement* EOF
    ;

statement
    : loopStatement
    | conditionalStatement
    | outputStatement
    | variableStatement
    ;

statementBlock
    : loopStatement
    | conditionalStatement
    | outputStatement
    | variableStatement
    | breakStatement
    ;

loopStatement
    : 'while' '(' expression ')' block
    ;

conditionalStatement
    : 'if' '(' expression ')' block
    ;

block
    : '{' statementBlock* '}'
    ;

breakStatement
    : 'break' ';'
    ;

inputStatement
    : 'input'
    ;

outputStatement
    : 'output' expression ';'
    ;

variable
    : ID
    ;

variableStatement
    : variable '=' expression ';'
    ;

expression
    : expression ( 'and' | 'or' | '^' ) expression
    | expression ( '==' | '!=' | '<' | '<=' | '>' | '>=' ) expression
    | expression ( '+' | '-' | '*' | '//' ) expression
    | '(' expression ')'
    | 'not' expression
    | 'not' value
    | value
    ;
    
value
    : variable
    | numericValue
    | logicValue
    | inputStatement
    ;

numericValue: INT;

logicValue: TRUE | FALSE;

TRUE: 'true';

FALSE: 'false';

INT: ('-')?[0-9]+;

ID: 'var'[0-9]*;

WS: [ \t\r\n]+ -> skip;
