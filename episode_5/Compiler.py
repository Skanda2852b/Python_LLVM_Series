from llvmlite import ir

from AST import Node, NodeType, Program, Expression
from AST import ExpressionStatement, LetStatement
from AST import InfixExpression
from AST import IntegerLiteral, FloatLiteral, IdentifierLiteral

from Environment import Environment

class Compiler:
    def __init__(self) -> None:
        self.type_map: dict[str, ir.Type] = {
            'int': ir.IntType(32),
            'float': ir.FloatType()
        }

        # Initialize the main module
        self.module: ir.Module = ir.Module('main')

        # Current Builder
        self.builder: ir.IRBuilder = ir.IRBuilder()

        # Counter for unique block names
        self.counter: int = 0

        # Environment reference for the currently compiling scope
        self.env: Environment = Environment()

    def __increment_counter(self) -> int:
        self.counter += 1
        return self.counter

    def compile(self, node: Node) -> None:
        """ Main Recursive loop for compiling the AST """
        match node.type():
            case NodeType.Program:
                self.__visit_program(node)

            # Statements
            case NodeType.ExpressionStatement:
                self.__visit_expression_statement(node)
            case NodeType.LetStatement:
                self.__visit_let_statement(node)

            # Expressions
            case NodeType.InfixExpression:
                self.__visit_infix_expression(node)

    # region Visit Methods
    def __visit_program(self, node: Program) -> None:
        """ Generates the main function, then compiles code into it """
        func_name: str = "main"
        param_types: list[ir.Type] = []
        return_type: ir.Type = self.type_map["int"]

        # Define the function type and actual function
        fnty = ir.FunctionType(return_type, param_types)
        func = ir.Function(self.module, fnty, name=func_name)

        # Define the function's block
        block = func.append_basic_block(f"{func_name}_entry")

        # Set the current builder
        self.builder = ir.IRBuilder(block)

        # Compile the body
        for stmt in node.statements:
            self.compile(stmt)

        return_value: ir.Constant = ir.Constant(self.type_map["int"], 69)
        self.builder.ret(return_value)

    # region Statements
    def __visit_expression_statement(self, node: ExpressionStatement) -> None:
        self.compile(node.expr)

    def __visit_let_statement(self, node: LetStatement) -> None:
        name: str = node.name.value
        value: Expression = node.value
        value_type: str  = node.value_type # TODO: We'll use this more for type checking and other types like int64 later on

        value, Type = self.__resolve_value(node=value)

        if self.env.lookup(name) is None:
            # Define and allocate the variable
            ptr = self.builder.alloca(Type)

            # Storing the value to the pointer
            self.builder.store(value, ptr)

            # Add the variable to the environment
            self.env.define(name, value, Type)
        else:
            ptr, _ = self.env.lookup(name)
            self.builder.store(value, ptr)

    # endregion
        
    # region Expressions
    def __visit_infix_expression(self, node: InfixExpression) -> None:
        operator: str = node.operator
        left_value, left_type = self.__resolve_value(node.left_node)
        right_value, right_type = self.__resolve_value(node.right_node)

        value = None
        Type = None
        if isinstance(right_type, ir.IntType) and isinstance(left_type, ir.IntType):
            Type = self.type_map['int']
            match operator:
                case '+':
                    value = self.builder.add(left_value, right_value)
                case '-':
                    value = self.builder.sub(left_value, right_value)
                case '*':
                    value = self.builder.mul(left_value, right_value)
                case '/':
                    value = self.builder.sdiv(left_value, right_value)
                case '%':
                    value = self.builder.srem(left_value, right_value)
                case '^':
                    # TODO: Implement this (Having an issue off camera implementing this)
                    pass
        elif isinstance(right_type, ir.FloatType) and isinstance(left_type, ir.FloatType):
            Type = ir.FloatType()
            match operator:
                case '+':
                    value = self.builder.fadd(left_value, right_value)
                case '-':
                    value = self.builder.fsub(left_value, right_value)
                case '*':
                    value = self.builder.fmul(left_value, right_value)
                case '/':
                    value = self.builder.fdiv(left_value, right_value)
                case '%':
                    value = self.builder.frem(left_value, right_value)
                case '^':
                    # TODO: Implement this (Having an issue off camera implementing this)
                    pass

        return value, Type
    # endregion
    
    # endregion
        
    # region Helper Methods
    def __resolve_value(self, node: Expression) -> tuple[ir.Value, ir.Type]:
        """ Resolves a value and returns a tuple (ir_value, ir_type) """
        match node.type():
            # Literals
            case NodeType.IntegerLiteral:
                node: IntegerLiteral = node
                value, Type = node.value, self.type_map['int']
                return ir.Constant(Type, value), Type
            case NodeType.FloatLiteral:
                node: FloatLiteral = node
                value, Type = node.value, self.type_map['float']
                return ir.Constant(Type, value), Type
            case NodeType.IdentifierLiteral:
                node: IdentifierLiteral = node
                ptr, Type = self.env.lookup(node.value)
                return self.builder.load(ptr), Type
            
            # Expression Values
            case NodeType.InfixExpression:
                return self.__visit_infix_expression(node)
    # endregion
    