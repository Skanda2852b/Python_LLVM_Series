# Episode 8 - If Statements + Conditional Operators + Booleans
Setting up variable re-assignment

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add `LT`, `GT`, `EQ_EQ`, `NOT_EQ`, `LT_EQ`, `GT_EQ` TokenTypes
    - Add `IF`, `ELSE` TokenTypes
    - Add `TRUE`, `FALSE` TokenTypes
    - Add `IF`, `ELSE`, `TRUE`, `FALSE` to `KEYWORDS` and `ALT_KEYWORDS`
3. Lexer.py
    - Add `<` `>` `<=` `>=` `==` `!=` to `next_token` match case
4. AST.py
    - Add `IfStatement` NodeType
    - Add `BooleanLiteral` NodeType
    - Add `IfStatement` Node
    - Add `BooleanLiteral` Node
5. Parser.py
    - Import `IfStatement`, `BooleanLiteral`
    - Add new PRECEDENCES to the dict
    - Add new `infix_parse_fns` to the dict
    - Add new `IF` (`__parse_if_statement`),`TRUE` and `FALSE` (`__parse_boolean`) key to the `prefix_parse_fns`
    - Create/Implement `__parse_if_statement`
    - Create/Implement `__parse_boolean`
6. Main.py
    - Toggle the PARSER_DEBUG flag and investigate AST
7. Compiler.py
    - Import `IfStatement`, `BooleanLiteral`
    - Add the `IfStatement` to the compile method
    - Create/Implement the `__visit_if_statement` method
    - Add all new symbols to `__visit_infix_expression`
    - Add `BooleanLiteral` to the `__resolve_value` method
    - Add `bool` to the `type_map`
    - Call `__initialize_builtins()` method in `__init__`
    - Implement `__initialize_builtins()` and the inner `__init_booleans` method
    - Set the `true` and `false` reserved keywords in the global environment
8. Main.py
    - Toggle the COMPILER_DEBUG flag and investigate the IR
    - Toggle the RUN_CODE flag and investigate the output


    