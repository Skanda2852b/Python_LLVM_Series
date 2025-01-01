# Episode 8 - Function parameters
Setting up the ability to add parameters to functions and call functions with params

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add the `COMMA` TokenType
3. Lexer.py
    - Add `,` to the `next_token` match statement
4. AST.py
    - Add the `FunctionParameter` NodeType
    - Add the `FunctionParameter` Node
    - Add typing to the `FunctionStatement` node to allow for `FunctionParameter`s
5. Parser.py
    - Import `FunctionParameter`
    - In the `__parse_function_statement` function, call the `__parse_function_parameters` function
    - Implement the `__parse_function_parameters` function
    - In the `__parse_call_expresion` function, call the `__parse_expression_list` function
    - Implement the `__parse_expression_list` function
6. Main.py
    - Toggle PARSER_DEBUG flag and ivestigate the ast
7. Compiler.py
    - Import `FunctionParameter`
    - Fix errors in `__visit_function_statement`
        - `params: list[**FunctionParameter**]`
        - `param_names: list[str] = [**p.name** for p in params]`
    - Add param handling to `__visit_function_statement`
    - Add param handling to `__visit_call_expression`
8. Main.py
    - Toggle COMPILER_DEBUG flag and investigate IR
    - Toggle the RUN_CODE flag and investigate output
