# Episode 11 - Strings and the Printf function
Strings and the Printf function

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add the `STRING` token type
    - Add the `str`, `void` type keywords
3. Lexer.py
    - Add the new case statement for `"`
    - Implement the `__read_string` function
4. AST.py
    - Add `StringLiteral` NodeType
    - Implement `StringLiteral` Node
5. Parser.py
    - Import `StringLiteral` Node
    - Add `TokenType.STRING` to prefex_parse_fns
    - Implement `__parse_string_literal` function
6. Compiler.py
    - Import `StringLiteral` Node
    - Add `void` and `str` types to the type_map
    - Start with the printf function by modifying `__initialize_builtins`
    - Add `StringLiteral` case to __resolve_value
    - Implement the `__convert_string` function
    - Now below it implement the `builtin_printf` function
    - Navigate to `__visit_call_expression` and implement the case for printf
7. main.py