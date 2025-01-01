# Episode 7 - Variable Re-Assignment
Setting up variable re-assignment

## Episode Timeline
1. test.lime
    - Set up the piece of code we will be compiling in this episode
2. AST.py
    - Add the `AssignStatement` NodeType
    - Add the `AssignStatement` Node
3. Parser.py
    - Import `AssignStatement`
    - Modify `__parse_statement` to include if statement for checking whether or not to parse an assignment statement
    - Implement `__parse_assignment_statement`
4. Main.py
    - Add RUN_CODE flag and guard the running portion
    - Toggle PARSER_DEBUG and investigate ast.json
5. Compiler.py
    - Import `AssignStatement`
    - Add a `self.errors` list to the `__init__`
    - Add `AssignStatement` to the `compile` match case
    - Implement `__visit_assign_statement`
6. Main.py
    - Toggle COMPILER_DEBUG to investigate IR
    - Add a `RUN_CODE` flag and put all the llvm running code behind the flag
    - Add a compiler errors check to print them out and stop the execution
    - After investigating IR, toggle the `RUN_CODE` flag and mess around with what the program returns with assign statements


    