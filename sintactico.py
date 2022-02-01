import ply.yacc as yacc
from lexico import tokens
import lexico
import sys 

#which of them has higher priority
#https://www.php.net/manual/es/language.operators.precedence.php
#http://opac.pucv.cl/pucv_txt/txt-1000/UCC1494_01.pdf

'''
Estudiantes:
Miguel Angel Ramirez Echeverry
Santiago Ramirez Arenas
Juan Sebastian Ossa
'''

VERBOSE = 1

precedence = (
    ('right','ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'PORCENT'),
    ('right', 'INC'),
    ('left', 'LPAREN', 'RPAREN')
)

def p_program(p):
    '''program : LESS PREG PHP declaration_list PREG GREATER'''
    pass

def p_declaration_list_1(P):
    '''declaration_list : declaration_list declaration'''
    pass

def p_declaration_list_2(p):
    '''declaration_list : declaration'''
    pass

#Aqui debo ingresar mas
def p_declaration(p):
    '''declaration : var_declaration
                   | echo_stmt
                   | fun_declaration
                   | selection_stmt
                   | iteration_stmt 
                   | class_stmt
    '''
    pass

def p_class_1(p):
    '''class_stmt : CLASS ID LBLOCK attributes_class statement RBLOCK
                  | CLASS ID EXTENDS ID LBLOCK attributes_class statement RBLOCK'''
    pass


def p_class_2(p):
    '''attributes_class : var_declaration3'''
    pass

#--------------DECLARACIONES DE ECHO-----------------
def p_echo_stmt(p):
    '''echo_stmt : ECHO STRING SEMICOLON
                 | ECHO ID SEMICOLON
                 | ECHO NUMBER SEMICOLON
                 | ECHO ID ARROW encap SEMICOLON
                 | empty
    '''
    pass

#--------------CIERRE DE DECLARACIONES DE ECHO-----------


#-------------DECLARACIONES DE VARIABLES--------------

def p_var_declaration_1(p):
    '''var_declaration3 : encap ID SEMICOLON'''
    pass

def p_var_declaration_2(p):
    '''var_declaration3 : encap ID ASSIGN NUMBER SEMICOLON'''
    pass


def p_var_declaration_3(p):
    '''var_declaration3 : encap ID ASSIGN STRING SEMICOLON'''
    pass

def p_var_declaration_4(p):
    '''var_declaration3 : encap ID ASSIGN ope symbols ope SEMICOLON'''
    pass


def p_var_declaration_5(p):
    '''var_declaration : ID ASSIGN SEMICOLON'''
    pass

def p_var_declaration_6(p):
    '''var_declaration : ID ASSIGN NUMBER SEMICOLON'''
    pass

def p_var_declaration_7(p):
    '''var_declaration : ID ASSIGN STRING SEMICOLON'''
    pass

def p_var_declaration_8(p):
    '''var_declaration : ID ASSIGN ope symbols ope SEMICOLON'''
    pass
def p_var_declaration_9(p):
    '''var_declaration : ID ARROW call_to_function'''
    pass

def p_var_declaration_10(p):
    '''var_declaration : ID ASSIGN ID
                       | ID ASSIGN STRING
    '''
    pass

def p_var_declaration_12(p):
    '''var_declaration : ID ASSIGN NEW call_to_function'''
    pass

def p_var_declaration_13(p):
    '''var_declaration : CONST ID ASSIGN STRING SEMICOLON
                       | CONST ID ASSIGN NUMBER SEMICOLON
    '''
    pass

#bucles
def p_var_declaration_11(p):
    '''var_declaration2 : ID ASSIGN NUMBER
                        | ID ASSIGN ID
                        | ID
    '''
    pass


#------- CIERRE DE LAS DECLARACIONES DE VARIABLES---------


#------- DECLARACIONES DE PROPIEDADES ----------------
def p_encap(p):
    '''encap : PUBLIC
             | PROTECTED
             | PRIVATE
             | empty
    '''
    pass
#------------------ CIERRE DE LAS DECLARACIONES DE PROPIEDADES ----

def p_operator_1(p):
    '''ope : ID
           | NUMBER
    '''
    pass

def p_symbols_1(p):
    '''symbols : PLUS
               | MINUS
               | TIMES
               | DIVIDE
               | PORCENT
    '''
    pass

#-------------------Declraciones de funciones---------------

def p_call_to_function(p):
    '''call_to_function : ID LPAREN param_list RPAREN SEMICOLON'''
    pass

def p_fun_declaration(p):
    '''fun_declaration : FUNCTION ID2 LPAREN param_list RPAREN compount_stmt'''
    pass

def p_param_list_1(p):
    '''param_list : param_list COMMA param'''
    pass

def p_param_list_2(p):
    '''param_list : param'''
    pass

def p_param_list_3(p):
    '''param_list : empty'''
    pass

def p_param_1(p):
	'''param : ID
			| NUMBER
			| STRING'''
	pass

def p_compount_stmt(p):
    '''compount_stmt : LBLOCK statement_list RBLOCK'''
    pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'
	pass

def p_statement(p):
	'''statement : iteration_stmt 
                | selection_stmt 
                | return_stmt
                | call_to_function 
                | echo_stmt
				| var_declaration
				| fun_declaration
                | COMMENT
	'''
	pass



#-------------------Cierre de declaraciones de funciones---------------

def p_selection_stmt_1(p):
	'''selection_stmt : IF LPAREN simple_expression RPAREN LBLOCK statement_list RBLOCK'''
	pass

def p_selection_stmt_2(p):
    '''selection_stmt : IF LPAREN simple_expression RPAREN LBLOCK statement_list RBLOCK ELSE LBLOCK statement_list RBLOCK'''
    pass

def p_iteration_stmt_1(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON  simple_expression SEMICOLON additive_expression RPAREN LBLOCK statement_list RBLOCK'
	pass

def p_simple_expression(p):
    '''simple_expression : ope2 relop ope2
                         | simple_expression OR simple_expression
                         | simple_expression AND simple_expression
    '''
    pass

def p_additive_expression_1(p):
    '''additive_expression : ID INC
                           | ID MINUSMINUS
    '''
    pass

def p_ope_2(p):
    '''ope2 : ID
            | NUMBER
            | STRING
            | ope symbols ope 
    '''
    pass

def p_return_stmt_1(p):
	'''return_stmt : RETURN SEMICOLON
                   | RETURN ID SEMICOLON
                   | RETURN NUMBER SEMICOLON
                   | RETURN STRING SEMICOLON
                   | RETURN ope symbols  ope SEMICOLON
                   | RETURN ope relop ope SEMICOLON
    '''
	pass

def p_relop(p):
    '''relop : LESS
             | GREATER
             | IS_EQUAL
             | LESSEQUAL
    '''
    pass

def p_empty(p):
    '''empty : '''
    pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(lexico.lexer.lineno))
	else:
		raise Exception('syntax', 'error')



parser = yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        fin = 'prueba2.txt'

    f = open(fin, 'r')
    data = f.read()
    #print (data)
    parser.parse(data, tracking=True)
    print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
        #input()