import lexer

def lex_string(string):
    m = lexer.Lexer()
    m.build()
    return m.test(string)

a = lex_string("pixle")
print(a)
