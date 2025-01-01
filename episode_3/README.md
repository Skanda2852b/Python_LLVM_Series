# Episode 3 - Compiler Class, LLVM Introduction
Setting up the compiler class, setting up necessary llvm components, setting up main function

## Episode Timeline
1. `conda install llvmlite`
2. Create the tests/compiler.lime file
3. Create the Compiler.py file
4. Setting up the Compiler class
    - Setting up `__init__`
    - Setting up `compile`
        - Setting up `__visit_program`
        - Setting up `__visit_expression_statement`
        - Setting up `__visit_infix_expression`
            - Setting up `__resolve_value`
5. Setting up main.py to use the compiler
    - Setting a debug flag to print the IR to a file
    - Going over briefly the IR we generated
