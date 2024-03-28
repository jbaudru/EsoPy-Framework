class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 0
        self.special_characters = ["?", "!", ">", "<", "@", "&", "|", "^", "~", "%", "$", "#", "_", "`", ":", ";", ",", ".", "[", "]", "{", "}", "\\", '"', "'"]
        # Modify the keywords and symbols to match the language you want to create
        # {system_token: user_token}
        """
        self.keywords = {"PRINT":"PRINT", "GOTO": "GOTO", "GOIF": "GOIF", "INPUT": "INPUT", "END": "END"}
        self.symbols = {"=":"=", "+":"+", "-":"-", "*":"*", "/":"/", "(":"(", ")":")", "@":"@"}
        """
        # Example: Esolang 1
        self.keywords = {"PRINT":"<<<", "GOTO": "!!!", "GOIF": "???", "INPUT": ">>>", "END": "..."}
        self.symbols = {"=":"+-+", "+":"---", "-":"+++", "*":"***", "/":"///", "(":"(", ")":")", "@":"@@@"}
        
        # Example: Esolang 2 
        self.keywords = {"PRINT":"show", "GOTO": "jumpTo", "GOIF": "ifZeroJumpTo", "INPUT": "writeIn", "END": "finish"}
        self.symbols = {"=":"is", "+":"plus", "-":"minus", "*":"times", "/":"div", "(":"(", ")":")", "@":"//"}
        
    def error(self):
        print("\n[GRRRR] I don't know the f*cking character " + self.text[self.pos] + " in line " + str(self.line) + "\n")
        exit(1)
        
    def keyword_token(self):
        start = self.pos
        while self.pos < len(self.text) and (self.text[self.pos].isalpha() or self.text[self.pos] in self.special_characters):
            self.pos += 1
        user_token = self.text[start:self.pos]
        
        for token, user_token_ref in self.keywords.items():
            if(user_token == user_token_ref):
                return Token(token, token, self.line)
        else:
            self.pos = start  # Reset the position if it's not a keyword

    def get_next_token(self):
        while self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
                continue
            
            comment = self.symbols["@"]
            #print(comment)
            #print(len(comment))
            if self.text[self.pos:self.pos+len(comment)] == comment:
                while self.pos < len(self.text) and self.text[self.pos] != '\n':
                    self.pos += 1
                continue
                
            if self.text[self.pos].isdigit():
                start = self.pos
                while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
                    self.pos += 1
                value = self.text[start:self.pos]
                if '.' in value:
                    return Token('NUMBER', float(value), self.line)
                else:
                    return Token('NUMBER', int(value), self.line)
            
            if self.text[self.pos] == '"':
                start = self.pos + 1
                self.pos += 1
                while self.pos < len(self.text) and self.text[self.pos] != '"':
                    self.pos += 1
                end = self.pos
                self.pos += 1  # Skip the closing quotation mark
                return Token('STRING', self.text[start:end], self.line)

            
            if self.text[self.pos].isalpha() or self.text[self.pos] in self.special_characters:
                token = self.keyword_token()
                if token:
                    return token

            equal = self.symbols["="]
            if self.text[self.pos:self.pos+len(equal)] == equal:
                self.pos += len(equal)
                return Token('EQUALS', '=', self.line)
            
            plus = self.symbols["+"]
            if self.text[self.pos:self.pos+len(plus)] == plus:
                self.pos += len(plus)
                return Token('PLUS', '+', self.line)
            
            minus = self.symbols["-"]
            if self.text[self.pos:self.pos+len(minus)] == minus:
                self.pos += len(minus)
                return Token('MINUS', '-', self.line)

            mul = self.symbols["*"]
            if self.text[self.pos:self.pos+len(mul)] == mul:
                self.pos += len(mul)
                return Token('MULTIPLY', '*', self.line)
            
            div = self.symbols["/"]
            if self.text[self.pos:self.pos+len(div)] == div:
                self.pos += len(div)
                return Token('DIVIDE', '/', self.line)

            lpar = self.symbols["("]
            if self.text[self.pos:self.pos+len(lpar)] == lpar:
                self.pos += len(lpar)
                return Token('LPAREN', '(', self.line)

            rpar = self.symbols[")"]
            if self.text[self.pos:self.pos+len(rpar)] == rpar:
                self.pos += len(rpar)
                return Token('RPAREN', ')', self.line)

            end = self.keywords["END"]
            if self.text[self.pos:self.pos+len(end)] == end:
                self.pos += len(end)
                return Token('END', 'END', self.line)
            
            if (self.text[self.pos].isalpha() or self.text[self.pos] in self.special_characters):
                start = self.pos
                while self.pos < len(self.text) and (self.text[self.pos].isalpha() or self.text[self.pos] in self.special_characters):
                    self.pos += 1
                return Token('IDENTIFIER', self.text[start:self.pos], self.line)
            
            
            self.error()
        return Token('EOF', None, self.line)