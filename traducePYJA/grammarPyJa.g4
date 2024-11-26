// Definición de la gramática: grammarPyJa.g4

grammar grammarPyJa;

// Reglas léxicas
DEF: 'def';
RETURN: 'return';
PRINT: 'print';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
COLON: ':';
ASTERISK: '*';
MINUS: '-';
ASSIGN: '=';

// Reglas sintácticas
program: (functionDefinition | printStatement | assignment)*;

functionDefinition: DEF IDENTIFIER LPAREN parameters RPAREN COLON statement+ RETURN expression;

parameters: IDENTIFIER (COMMA IDENTIFIER)*;

statement: assignment | printStatement;

assignment: IDENTIFIER ASSIGN expression;

expression: expression ASTERISK expression
          | expression MINUS expression
          | IDENTIFIER
          | NUMBER;
functionCall
    : IDENTIFIER '(' arguments? ')'
    ;

arguments
    : expression (',' expression)*
    ;

printStatement: PRINT LPAREN expression RPAREN;
