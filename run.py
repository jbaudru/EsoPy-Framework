import sys
from classes.lexer import Lexer
from classes.interpreter import Interpreter

def main():
    if len(sys.argv) != 2:
        print('\n[GRRRR] You should try: python run.py <filename.eso> \n')
        return

    filename = sys.argv[1]
    if not filename.endswith('.eso'):
        print('\n[GRRRR] Invalid file type. Dude please provide a .eso file. \n')
        return

    text = []
    with open(filename, 'r') as file:
        txt = file.readlines()
        text = [line.strip() for line in txt]
    
    lexer = Lexer('')
    interpreter = Interpreter(lexer, text)

    i = 0
    while i != len(text):
        line = text[i]
        lexer.text = line
        lexer.pos = 0
        lexer.line += 1
        interpreter.current_token = lexer.get_next_token()
        result = interpreter.expr()
        i = lexer.line

if __name__ == '__main__':
    main()