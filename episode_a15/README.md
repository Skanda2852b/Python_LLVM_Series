# Episode 15 - Postfix Operators (i++, i--)

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add the `PLUS_PLUS` + `MINUS_MINUS` token types
3. Lexer.py
    - Handle the `PLUS_PLUS` + `MINUS_MINUS` conditions in the match statement
4. AST.py
    - Add the `PostfixExpression` Node type
    - Add the `PostfixExpression` Node
5. Parser.py
    - Import `PostfixExpression`
    - Add the `PLUS_PLUS` + `MINUS_MINUS` Precedence mappings
    - Add the `PLUS_PLUS` + `MINUS_MINUS` infix_parse_fns
    - Implement `__parse_postfix_expression`
    - Modify `__parse_for_statement` action to default expressions
6. Compiler.py
    - Import `PostfixExpression`
    - Implement `__visit_postfix_expression`
    - Add the case statement for `PostfixExpression` in `compile`