import ply.yacc as yacc
from lex_test import tokens
# Tokens from lexer

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'), 
)

# Grammar rules 

def p_program(p):
    'program : statement_list'
    
def p_statement_list(p):
    '''statement_list : statement_list statement  
                      | statement
                      '''
                      
def p_statement(p):
    '''statement : var_decl
                 | fun_decl
                 | class_decl
                 | expression
                 | if_statement
                 | while_loop'''
                 
def p_var_decl(p):
    'var_decl : KEYWORD ID COLON type EQUAL expression SEMI'

def p_fun_decl(p):
    'fun_decl : KEYWORD ID LPAREN RPAREN COLON  block'

def p_class_decl(p):
    'class_decl : KEYWORD ID LBRACE class_body RBRACE'
    
def p_class_body(p): 
    'class_body : ID COLON type SEMI'

def p_if_statement(p):
    'if_statement : KEYWORD LPAREN expression RPAREN LBRACE block RBRACE'

def p_while_loop(p):
    'while_loop : KEYWORD LPAREN expression RPAREN LBRACE block block RBRACE'


def p_block(p):
    '''block : DATA_TYPES LBRACE statement_list RBRACE
             | ID LPAREN STRING RPAREN SEMI
             | ID LPAREN STRING RPAREN SEMI newline
             | ID PLUS PLUS SEMI
             | ID MINUS MINUS SEMI'''
    
def p_type(p):
    '''type : KEYWORD
            | ID'''
            
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression 
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQUAL expression
                  | expression GREATER expression
                  | expression LESSER expression
                  | LPAREN expression RPAREN
                  | ID LESSER NUMBER
                  | NUMBER 
                  | ID 
                  | STRING
                  | SEMI'''

def p_error(p):
    print("Syntax error!")
    # print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")

    
parser = yacc.yacc()

code = '''
while (i < 10) {
   console.log("hello");
   i++;
}
'''



parser.parse(code)


'''

function printHello(): void { console.log('Hello!'); } //done


class Person { name: string; } //done
var num:number = 5; //done

var i:number;
var factorial = 1;

if (num > 0) {                      //show this
  console.log("number is positive");
}


while (i < 10) {           //show this
   console.log("hello");
   i++;
}
'''