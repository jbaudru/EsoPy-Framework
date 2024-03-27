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


    def error(self):
        print("\n[GRRRR] I don't know the f*cking character " + self.text[self.pos] + " in line " + str(self.line) + "\n")
        exit(1)
        
    def keyword_token(self):
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos].isalpha():
            self.pos += 1
        token = self.text[start:self.pos]
        if token in ['GOTO', 'INPUT']:
            return Token(token, token, self.line)
        else:
            self.pos = start  # Reset the position if it's not a keyword

    def get_next_token(self):
        while self.pos < len(self.text):
            if self.text[self.pos].isspace():
                self.pos += 1
                continue
            
            if self.text[self.pos:self.pos+1] == '@':
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

            
            if self.text[self.pos].isalpha():
                token = self.keyword_token()
                if token:
                    return token

                start = self.pos
                while self.pos < len(self.text) and self.text[self.pos].isalpha():
                    self.pos += 1
                return Token('IDENTIFIER', self.text[start:self.pos], self.line)


            if self.text[self.pos] == '=':
                self.pos += 1
                return Token('EQUALS', '=', self.line)
            if self.text[self.pos] == '+':
                self.pos += 1
                return Token('PLUS', '+', self.line)
            if self.text[self.pos] == '-':
                self.pos += 1
                return Token('MINUS', '-', self.line)
            if self.text[self.pos] == '*':
                self.pos += 1
                return Token('MULTIPLY', '*', self.line)
            if self.text[self.pos] == '/':
                self.pos += 1
                return Token('DIVIDE', '/', self.line)
            if self.text[self.pos] == '(':
                self.pos += 1
                return Token('LPAREN', '(', self.line)
            if self.text[self.pos] == ')':
                self.pos += 1
                return Token('RPAREN', ')', self.line)

            
            self.error()
        return Token('EOF', None, self.line)