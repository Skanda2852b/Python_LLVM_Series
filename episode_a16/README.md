# Episode 15 - Postfix Operators (i++, i--)

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add the `IMPORT` TokenType
    - Add `import` to the Keywords mapping
    - Add `gib` to the alt_keywords mapping
3. AST.py
    - Add the `ImportStatement` node type
    - Add the `ImportStatement` node
4. Parser.py
    - Import `ImportStatement`
    - Add the `IMPORT` case statement in `__parse_statement`
    - Implement `__parse_import_statement` function
5. Compiler.py
    - Import `os`, `ImportStatement`, `Lexer`, and `Parser`
    - Add `global_parsed_pallets` to `__init__` method
    - Add the case statement to the `compile` method
    - Implement `__visit_import_statement`