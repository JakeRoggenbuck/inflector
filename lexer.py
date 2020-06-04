import ply.lex as lex

class Lexer(object):
    tokens = (
        'PIX',
        'TIX',
        'KIX',
        'NX',
        'OX',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'
    )
    
    t_PIX = r'pix'
    t_TIX = r'tix'
    t_KIX = r'kix'
    t_NX = r'nx'
    t_OX = r'ox'
    t_A = r'a'
    t_B = r'b'
    t_C = r'c'
    t_D = r'd'
    t_E = r'e'
    t_F = r'f'
    t_G = r'g'
    t_H = r'h'
    t_I = r'i'
    t_J = r'j'
    t_K = r'k'
    t_L = r'l'
    t_M = r'm'
    t_N = r'n'
    t_O = r'o'
    t_P = r'p'
    t_Q = r'q'
    t_R = r'r'
    t_S = r's'
    t_T = r't'
    t_U = r'u'
    t_V = r'v'
    t_W = r'w'
    t_X = r'x'
    t_Y = r'y'
    t_Z = r'z'
    
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    
    t_ignore  = ' \t'
    
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self,data):
        lexed = []
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             lexed.append(tok.value)
        return lexed
