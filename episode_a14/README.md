# Episode 14 - CPrefix Operators (!true, -1) + Assignment Operators (+= -= *= /=)

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add the `BANG`, `PLUS_EQ`, `MINUS_EQ`, `MUL_EQ`, `DIV_EQ` TokenTypes
3. Lexer.py
    - Add the `BANG`, `PLUS_EQ`, `MINUS_EQ`, `MUL_EQ`, `DIV_EQ` case statements
4. AST.py
    - Add the `PrefixExpression` node type
    - Modify the `AssignStatment` node to include an operator
    - Add the `PrefixExpression` node
5. Parser.py
    - Import the `PrefixExpression` node
    - Add `MINUS` + `BANG` to the `prefix_parse_fns`
    - Implement `__parse_prefix_expression`
    - Implement the `__peek_token_is_assignment` function
    - Use the function in the `__parse_statement` method
    - Modify the `__parse_assignment_statement` function to handle operators
6. Compiler.py
    - Import the `PrefixExpression` node
    - Implement the `__visit_prefix_expression` method
    - Add the `PrefixExpression` case statement to `__resolve_value`
    - Modify `__visit_assign_statement` function to handle different operator operations