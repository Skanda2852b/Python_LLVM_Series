# Episode 8 - Function calling
Setting up the ability to call functions

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. AST.py
    - Add the `CallExpression` NodeType
    - Add the `CallExpression` Node
3. Parser.py
    - Import `CallExpression`
    - Add `LPAREN` to the PRECEDENCES mapping
    - Add `LPAREN` to the `infix_parse_fns` mapping for `__parse_call_expression`
    - Implement `__parse_call_expression`
4. Main.py
    - Toggle PARSER_DEBUG flag and investigate AST
5. Compiler.py
    - Import `CallExpression`
    - Add `CallExpression` to compile method with `__visit_call_expression`
    - Implement `__visit_call_expression`
    - Add `CallExpression` case to `__resolve_value`
6. Main.py
    - Toggle COMPILER_DEBUG flag and investigate IR
    - Toggle RUN_CODE flag and investigate output
    