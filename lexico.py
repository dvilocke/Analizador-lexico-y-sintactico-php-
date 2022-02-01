#Se importan las librerias
"""
Estudiantes:
Miguel Angel Ramirez Echeverry
Santiago Ramirez Arenas
Juan Sebastian Ossa
"""
#https://www.php.net/manual/es/tokens.php
import ply.lex as lex
import sys 

#creacion de los tokens
tokens = (
    # Reserverd words
    "CONST", #new
    "PUBLIC",
    "PROTECTED",
    "PRIVATE",
    "CLASS",
    "PHP",
    "FUNCTION",
    "ECHO",
    "NEW",
    "IF",
    "ELSE",
    "EXTENDS",
    "FOR",
    "RETURN",
    "OR",
    "AND",

    # Symbols
    "ARROW",
    "COMILLASDOBLES", #"
    "PLUS", #+
    "INC",
    "MINUSMINUS", 
    "MINUS", #-
    "TIMES", #*
    "DIVIDE",# /
    "IS_EQUAL", #NEW
    "ASSIGN", # =
    "LPAREN", #(
    "RPAREN", #)
    "LESSEQUAL", #new
    "LESS",  #<
    "GREATER", #> 
    "LBLOCK", #{
    "RBLOCK", #}
    "COMMA", #,
    "SEMICOLON", #;
    "DOLLAR", #$
    "PREG", #?
    "PORCENT", # %
    "COMILLASIMPLE", #'
    "JUMP",
    "COMMENT",
    "UNDERSCORE", #NEW


    # Others 
    'ID2',
    "ID",
    "NUMBER",
    "NEWLINE",
    "STRING" #NEW

)

#expresiones regulares para los simbolos
t_ARROW = r'->'
t_COMILLASDOBLES = r'\"'
t_PLUS = r'\+'
t_INC = r'\+\+'
t_MINUSMINUS = r'--'
t_MINUS = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_IS_EQUAL= r'=='
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LESS = r'<'
t_GREATER = r'>'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOLLAR = r'\$'
t_PREG  = r'\?'
t_PORCENT = r'%'
t_COMILLASIMPLE = r'\''
t_JUMP = r'\n'
t_UNDERSCORE = r'_'

#palabras reservadas

def t_CONST(t):
    r'const'
    return t


def t_PUBLIC(t):
    r'public'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_PHP(t):
    r'php'
    return t

def t_FUNCTION(t):
    r'function'
    return t



def t_ECHO(t):
    r'echo'
    return t

def t_NEW(t):
    r'new'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FOR(t):
    r'for'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_OR(t):
    r'or'
    return t 

def t_AND(t):
    r'and'
    return t 

t_ignore = '  \t'


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t


def t_ID2(t):
    r'\w+'
    return t

def t_ID(t):
    r'(\$\w+|\w+)'
    return t

def t_LESSEQUAL(t):
	r'<='
	return t   

def t_STRING(t):
    r'\"(.)+\"|\'(.)+\''
    return t



def t_COMMENT(t):
    r'(\/\/.*)|(\/\*.*\*\/)'
    return t

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)


lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'nombreDocumento.txt'
	f = open(fin, 'r')
	data = f.read()
	lexer.input(data)
	test(data, lexer)
	#input()
