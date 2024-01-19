import ply.lex as lex

# Define tokens
tokens = ("ID", "NUMBER", "PLUS", "MINUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN",
          "LBRACE", "RBRACE", "SEMI", "EQUAL", "ARROW", "KEYWORD", "STRING","COMMA","COLON","LESSER","GREATER","DATA_TYPES","newline")

# Define regular expressions for tokens
keywords = {"var", "function", "class", "if", "while"}
data_types = {"void","int","float"}
id_regex = r"[a-zA-Z_][a-zA-Z0-9_\.]*"
number_regex = r"\d+"
string_regex = r'''("[^\"]*")|('[^\']*')'''



# Define rules for lexing
t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"\/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_SEMI = r"\;"
t_COLON = r"\:"

t_EQUAL = r"\="
t_ARROW = r"\=\>"
t_COMMA= r"\,"
t_LESSER = r"\<"
t_GREATER = r"\>"
t_STRING = string_regex
t_ID = id_regex
t_NUMBER = number_regex

# Define rules for keywords
def t_KEYWORD(t):
    r"\b(var|function|class|if|while)\b"
    return t

def t_DATA_TYPES(t):
    r"\b(void|int|float)\b"
    return t

# Define ignore characters
t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Create a lexer
lexer = lex.lex()

text = '''
while (i < 10) {
   console.log("hello");
   i++;
}
'''

# Give the lexer some input
lexer.input(text)

# Iterate over the tokens
while True:
    token = lexer.token()
    if not token:
        break  # No more input
    print(token)
