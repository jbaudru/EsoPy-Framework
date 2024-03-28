![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![GitHub](https://img.shields.io/github/license/jbaudru/esolang?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/jbaudru/esolang?style=for-the-badge)

# EsoPy Template

Esoteric programming languages, or esolangs, are programming languages designed as a test of the boundaries of computer programming language design, as a joke, or as a proof of concept. They're not designed for conventional use, but to explore alternative ways of expressing computational logic. You can learn more about esolangs on [Wikipedia](https://en.wikipedia.org/wiki/Esoteric_programming_language) or on the [Esolangs wiki](https://esolangs.org/wiki/Main_Page).

[EsoPy Wiki](https://esolangs.org/wiki/EsoPy_Framework)

**This project provides a Python template for building esoteric programming languages. It includes a lexer and an interpreter, and a main file that ties everything together.**

If you want to define your own esoteric programming language, you can modify the `keywords` and `symbols` dictionaries in the `interpreter.py` file. 
```
# dic = {system_token: user_token}
self.keywords = {"PRINT":"PRINT", "GOTO": "GOTO", "GOIF": "GOIF", "INPUT": "INPUT", "END": "END"}
self.symbols = {"=":"=", "+":"+", "-":"-", "*":"*", "/":"/", "(":"(", ")":")", "@":"@"}
```

You can also modify the `special_characters` list to include any special characters you want to be use as variables names.
```
self.special_characters = ["?", "!", ">", "<", "@", "&", "|", "^", "~", "%", "$", "#", "_", "`", ":", ";", ",", ".", "[", "]", "{", "}", "\\", '"', "'"]
```

## Files
- `run.py`: This is the entry point of the project. It reads a *.eso* file line by line, passes each line to the lexer and interpreter, and prints the interpreter's symbol table after each line.
- `lexer.py`: This file contains the Lexer class which is responsible for breaking the input code into tokens. It also contains the Token class which represents a token.
- `interpreter.py`: This file contains the Interpreter class which is responsible for parsing and interpreting the tokens produced by the lexer.

## Features
The basic language proposed in this framework appears to be Turing complete. A Turing complete language is one that can simulate a Turing machine, meaning it can solve any problem that a Turing machine can, given enough time and memory.

- **Arithmetic operations**: The interpreter supports basic arithmetic operations like addition (+), subtraction (-), multiplication (*), and division (/).
- **Variable assignments**: The interpreter allows assigning values to variables. The assigned value can be a number, a string, or an arithmetic expression.
- **Comments**: The interpreter supports comments. Any text following the `@` symbol until the end of the line is considered a comment and is ignored by the interpreter.
- **Error handling**: The interpreter has basic error handling. If it encounters a syntax error, it will print an error message and exit.
- **Jump statement**: The interpreter supports the `GOTO` statement which allows jumping to a specific line in the code.
- **Conditional jump statement**: The interpreter supports the `GOIF` statement which allows conditional jumps based on the value of a variable. Its syntax is `GOIF <line_number> <variable_0_or_not>`. If the value of variable is 0, the program jumps to the line number specified. Otherwise, it continues to the next line. This allows for conditional logic and loop creation in the program.
- **Input statement**: The interpreter supports the `INPUT` statement which allows user input during runtime.
- **Print statement**: The interpreter supports the `PRINT` statement which allows printing the value of a variable to the console.
- **End statement**: The interpreter supports the `END` statement which allows terminating the program.

These features collectively allow the language to perform any computation that can be described algorithmically, which is the definition of Turing completeness. However, a formal proof would be required to definitively establish Turing completeness.

## Usage
To use the template, you need to create a *.eso* file with the code you want to interpret. Then, you can run the main.py file. It will read the *.eso* file line by line, pass each line to the lexer and interpreter, and print the interpreter's symbol table after each line.

**Here is how to run a file**:
```
python run.py example.eso
```
Here is the default code for `example_fibo.eso`:
```
@ Fibonacci sequence
i = 0
j = 1
INPUT counter
PRINT j
k = i + j
i = j
j = k
counter = counter - 1
GOIF 12 counter
GOTO 5
END
```
Here is how the user can modify the keywords and symbols to complexify the code. Code from `esolang1_fibo.eso`:
```
@@@ Fibonacci sequence
& +-+ 0
$$ +-+ 1
>>> #
<<< $$
: +-+ & --- $$
& +-+ $$
$$ +-+ :
# +-+ # +++ 1
??? 12 #
!!! 5
...
```
This is language use the following keywords and symbols:
```
self.keywords = {"PRINT":"<<<", "GOTO": "!!!", "GOIF": "???", "INPUT": ">>>", "END": "..."}
self.symbols = {"=":"+-+", "+":"---", "-":"+++", "*":"***", "/":"///", "(":"(", ")":")", "@":"@@@"}
``` 

Another example. Code from `esolang2_fibo.eso`:
```
// Fibonacci sequence
firstValue is 0
secondValue is 1
writeIn counter
show secondValue
tempoValue is firstValue plus secondValue
firstValue is secondValue
secondValue is tempoValue
counter is counter minus 1
ifZeroJumpTo 12 counter
jumpTo 5
finish
```
This is language use the following keywords and symbols:
```
self.keywords = {"PRINT":"show", "GOTO": "jumpTo", "GOIF": "ifZeroJumpTo", "INPUT": "writeIn", "END": "finish"}
self.symbols = {"=":"is", "+":"plus", "-":"minus", "*":"times", "/":"div", "(":"(", ")":")", "@":"//"}
``` 

Some example of simple programs in the default language are provided in the `examples` folder. You can use these as a reference when creating your own scripts. 


## Limitations
- Fix the parentheses issue. The interpreter does not handle nested parentheses correctly. 
- The interpreter does not perform any type checking. If you try to perform an operation with incompatible types, it will raise an error.
- The interpreter does not support string operations. You can assign a string to a variable, but you cannot use it in an arithmetic expression.

## Future Work
- Improve error handling by providing more detailed error messages.
