# Episode 6 - User defined functions, main function, running our program
Setting up user defined functions, and enforcing the user to declare a main function as their entry point

## Episode Timeline
1. test.lime
    - Show what we should be able to compile at the end of this episode
2. Token.py
    - Add `FN` TokenType (TT)
    - Add `ARROW` TT
    - Add `LBRACE` + `RBRACE` TT
    - Add `RETURN` TT
    - Add `FN` + `RETURN` to the KEYWORDS/ALT_KEYWORDS
3. Lexer.py
    - Add the helper function `__peek_char`
    - Add the `->` case statement to `next_token`
    - Add the `{` + `}` case statements to `next_token`
4. Main.py
    - Mark the LEXER_DEBUG flag and test the lexer
5. AST.py
    - Add the `FunctionStatement` NodeType
    - Add the `ReturnStatement` NodeType
    - Add the `BlockStatement` NodeType
    - Add the `ReturnStatement` Node
    - Add the `ReturnStatement` Node
    - Add the `FunctionStatement` Node
6. Parser.py
    - import `FunctionStatement`, `ReturnStatement`, `BlockStatement`
    - Add the `prefix_parse_fn` for `IDENT`
    - Implement `__parse_identifier` function
    - `__parse_statement` add cases for `FN` and `RETURN`
    - Define `__parse_function_statement`
    - Define `__parse_return_statement`
    - Define `__parse_block_statement`
    - Implement `__parse_block_statement` + `__parse_return_statement` first
    - Implement `__parse_function_statement`
7. Main.py
    - Toggle the PARSER_DEBUG flag and investigate `ast.json`
8. Compiler.py
    - Import `FunctionStatement`, `ReturnStatement`, `BlockStatement`
    - Add `FunctionStatement`, `ReturnStatement`, `BlockStatement` to the `compile` match case
    - Implement `__visit_block_statement`
    - Implement `__visit_return_statement`
    - Implement `__visit_function_statement`
    - Remove non-needed code from `__visit_program` for making main function and returning
    - **BUG FIX**
        - `__visit_let_statement` in the if statement, final line of `if self.env.lookup(name) is None:` must be: `self.env.define(name, *ptr*, Type)`
9. Main.py
    - Mark the COMPILER_DEBUG flag and investigate `ir.ll`
    - Import `time`
    - Parse the IR and run the code via MCJIT
    