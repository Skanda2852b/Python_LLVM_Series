# Episode 4 - Variables, Environment
Setting up declaring variables and our SymbolTable / Environment

## Episode Timeline
1. Delete all test files, and make one called `test.lime`
    - Insert one normal `let` statement and one `lit` statement
2. Main.py
    - Modify the with open function to take in the new `test.lime` file
3. Token.py
    - Add `LET` token
    - Add `IDENT` token
    - Add `COLON` token
    - Add `TYPE` token
    - Add `EQ` token
    - Add `KEYWORDS` dict
    - Add `ALT_KEYWORDS` dict
    - Add `TYPE_KEYWORDS` dict
    - Add the `lookup_ident` function
4. Lexer.py
    - import `lookup_ident` from Token
    - Add `=` to the match statement
    - Add `"` to the match statement
    - Add identifier/keyword handling to default case if statement
    - Implement `__is_letter`
    - Implement `__read_identifier`
5. AST.py
    - Create the `LetStatement` NodeType
    - Create the `IdentifierLiteral` NodeType
    - Create the `LetStatement` Node
    - Create the `IdentifierLiteral` Node
6. Parser.py
    - import `LetStatement` + `IdentifierLiteral` from AST
    - implement `__current_token_is` function
    - Add `TokenType.LET` to `__parse_statement` match case
        - `__parse_let_statement` function
    - Implement the `__parse_let_statement` function
7. Main.py
    - Turn on the PARSER_DEBUG flag
    - Examine and verifiy the AST is correct
8. Environment.py
    - Create the `Environment` class
    - implement `define` method
    - implement `__resolve` private method
    - implement `lookup` method
9. Compiler.py
    - import `Environment` from Environment.py
    - import `LetStatement` + `IdentifierLiteral` from AST
    - Add `self.env: Environment = Environment()` to the `__init__`
    - add `LetStatement` to the compile match case
    - implement `__visit_let_statement` function
    - add `IdentifierLiteral` to `__resolve_value` function
10. Main.py + ir.ll
    - Turn on the COMPILER_DEBUG flag
    - run the program and investigate the IR code in `ir.ll`
    - Talk over the instructions

