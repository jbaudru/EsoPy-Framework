class Interpreter:
    def __init__(self, lexer, full_text):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.symbol_table = {}
        self.full_text = full_text
        
    def error(self, line, type):
        print("\n[GRRRR] You made a dumb syntax error in line " + str(line))
        print("[GRRRR] Error in " + type + "\n")
        exit(1)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(self.current_token.line, "eat")
    
    def goto(self):
        self.eat('GOTO')
        if self.current_token.type == 'NUMBER':
            self.lexer.line = self.current_token.value - 1
            self.lexer.text = self.full_text[self.lexer.line]
            
        else:
            self.error(self.current_token.line, "goto")
            
    def goif(self):
        self.eat('GOIF')
        if self.current_token.type == 'NUMBER':
            line_number = self.current_token.value
            self.eat('NUMBER')
            if self.current_token.type == 'IDENTIFIER':
                var_name = self.current_token.value
                self.eat('IDENTIFIER')
                if var_name in self.symbol_table:
                    condition = self.symbol_table[var_name]
                    
                    if condition == 0:
                        self.lexer.line = line_number - 1
                        self.lexer.text = self.full_text[self.lexer.line]
        else:
            self.error(self.current_token.line, "goif")
            
    def input_value(self):
        self.eat('INPUT')
        if self.current_token.type == 'IDENTIFIER':
            var_name = self.current_token.value
            self.eat('IDENTIFIER')
            inp = input("INPUT> ")
            if(isinstance(inp, str) and inp.isdigit()):
                    inp = int(inp)
            self.symbol_table[var_name] = inp
        else:
            self.error(self.current_token.line, "input")
    
    def print_value(self):
        self.eat('PRINT')
        if self.current_token.type == 'IDENTIFIER':
            var_name = self.current_token.value
            self.eat('IDENTIFIER')
            if var_name in self.symbol_table:
                print(self.symbol_table[var_name])
            else:
                self.error(self.current_token.line, "print")
        else:
            print(self.expr())

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return token.value
        
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            
            self.eat('RPAREN')
            return result

    def expr(self):
        while self.current_token.type not in ('EOF'):
            if self.current_token.type == 'GOTO':
                self.goto()
            elif self.current_token.type == 'GOIF':
                self.goif()
            elif self.current_token.type == 'INPUT':
                self.input_value()
            elif self.current_token.type == 'PRINT':
                self.print_value()
            elif self.current_token.type == 'END':
                quit()
            elif self.current_token.type == 'IDENTIFIER':
                var_name = self.current_token.value
                self.eat('IDENTIFIER')

                if self.current_token.type == 'EQUALS':
                    self.eat('EQUALS')
                    if self.current_token.type == 'STRING':
                        result = self.current_token.value
                        self.eat('STRING')
                    else:
                        result = self.term()  # Handle the multiplication operation first
                    
                    while self.current_token.type in ('PLUS', 'MINUS'):
                        token = self.current_token
                        if token.type == 'PLUS':
                            self.eat('PLUS')
                            result = result + self.term()
                        elif token.type == 'MINUS':
                            self.eat('MINUS')
                            result = result - self.term()

                    self.symbol_table[var_name] = result  # Then assign the result to the variable
                    return self.symbol_table[var_name]

                """
                if var_name in self.symbol_table:
                    print(self.symbol_table[var_name]) # Print the value of the variable 
                    return self.symbol_table[var_name]
                else:
                    self.error(self.current_token.line, "identifier")
                """
            else:
                result = self.term()
                while self.current_token.type in ('PLUS', 'MINUS'):
                    token = self.current_token
                    if token.type == 'PLUS':
                        self.eat('PLUS')
                        result = result + self.term()
                    elif token.type == 'MINUS':
                        self.eat('MINUS')
                        result = result - self.term()

                return result
                

    def term(self):
        result = self.factor()
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token.type == 'MULTIPLY':
                self.eat('MULTIPLY')
                result = result * self.factor()
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
                result = result / self.factor()

        return result
    
    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return token.value
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            result = self.expr()
            self.eat('RPAREN')
            return result
        elif token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            if token.value in self.symbol_table:
                return self.symbol_table[token.value]
            else:
                self.error(self.current_token.line, "factor")