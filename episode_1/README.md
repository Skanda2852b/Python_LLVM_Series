# Episode 1 - Project Setup, Token Class, Lexer Class
Setting up tokens and basic lexer for a calculator language

## Project Setup
1. Install Miniconda or another python env manager
2. `conda create --name lime_language python=3.12`
3. `conda activate lime_language`
4. Create main.py file
5. Create tok.py file
6. Create Token class
    - Setting up TokenType(Enum) class
    - Setting up `__init__`
    - Setting up `__str__` and `__repr__`
7. Create Lexer class
    - Setting up `__init__`
    - Setting up `__read_char`
    - Setting up `next_token`
        - Setting up `__skip_whitespace`
        - Setting up the main `match` statement
            - Setting up `__new_token`
            - Setting up `__is_digit`
                - Setting up `__read_number`
8. Modify `main.py`
    - Setting up reading from input file
        - Create the tests/lexer.lime file
    - Setting up LEXER_DEBUG flag
        - Demostrate the lexer working with a few examples
