# Episode 2 - Parser Class, AST Nodes
Setting up the parser class to consume tokens from the lexer and build an AST

## Episode Timeline
1. Create the tests/parser.lime file
2. Create the parser.py file and the Parser class
    - Setting up `__init__`
    - Setting up `__next_token`
    - Declare `parse_program`
    - Setting up AST.py
        - Setting up NodeType(Enum)
        - Setting up Node abstract parent class
        - Setting up Statement Node abstraction
        - Setting up Expression Node abstraction
        - Setting up Program Node
            - Setting up `__init__`
            - Setting up all parent methods
    - Implement `parse_program`
        - Setting up `__parse_statement`
        - Setting up `__parse_expression_statement`
            - Setting up ExpressionStatement Node
            - Setting up PrecedenceType(Enum)
            - Setting up PRECEDENCES mapping
            - Setting up prefix_parse_fns for numbers
                - Setting up IntegerLiteral and FloatLiteral Nodes
                - Setting up `__parse_int_literal`
                - Setting up `__parse_float_literal`
                - Setting up `__parse_grouped_expression`
                    - Setting up `__exprect_peek`
                        - Setting up `__peek_error`
            - Setting up `__parse_expression`
                - Setting up `__no_prefix_parse_fn_error`
                - Setting up `__peek_token_is`
                - Setting up `__peek_precedence`
                - Setting up infix_parse_fns for arithmetic operations
                - Setting up `__parse_infix_expression`
                    - Setting up InfixExpression Node
            - Finishing the `__parse_expression_statement` function
        - Finishing the `parse_program` function
3. Implement parser in main.py
    - Add debug flag to save the AST to a json file
        - Create /debug folder for ast json
    - Demonstrate the AST and how the parser works
        - Show how precedence is handled using the AST
