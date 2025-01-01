# Episode 12 - While loops
while loops

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. Token.py
    - Add the `WHILE` token type
    - Add the `while` and `wee` keywords
3. AST.py
    - Add the `WhileStatement` NodeType
    - Add the `WhileStatement` Node
4. Parser.py
    - Import `WhileStatement` Node
    - Add `WHILE` case to __parse_statement
    - Implement `__parse_while_statement`
5. Compiler.py
    - Import `WhileStatement` node
    - Add `NodeType.WhileStatement` case statement to compile method
    - Implement `__visit_while_statement`