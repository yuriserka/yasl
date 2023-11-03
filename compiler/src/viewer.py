from src.ast.expression import ExpressionAst
from src.ast.function_call import FunctionCallAst
from src.ast.function_parameters_declaration import FunctionParametersDeclarationAst
from src.ast.jump import JumpAst
from src.ast.number import NumberAst
from src.ast.string_literal import StringLiteralAst
from src.ast.symbol_reference import SymbolReferenceAst
from src.ast.variable_declaration import VariableDeclarationAst
from src.ast.assignment import AssignmentAst
from src.ast.code_block import CodeBlockAst
from src.ast.function_declaration import FunctionDeclarationAst
from src.ast import Ast


class Viewer:
    def __init__(self, program_ast: Ast):
        self.program_ast: Ast = program_ast

    def view(self, indent: int = 0):
        for node in self.program_ast.nodes:
            self.view_node(node, indent)
            print()

    def view_node(self, node: Ast, indent: int = 0):
        if not node:
            return
        {
            AssignmentAst: self.view_assignment,
            CodeBlockAst: self.view_code_block,
            ExpressionAst: self.view_expression,
            FunctionCallAst: self.view_function_call,
            FunctionDeclarationAst: self.view_function_declaration,
            FunctionParametersDeclarationAst: self.view_function_parameters_declaration,
            JumpAst: self.view_jump,
            NumberAst: self.view_number,
            StringLiteralAst: self.view_string_literal,
            SymbolReferenceAst: self.view_symbol_reference,
            VariableDeclarationAst: self.view_variable_declaration,
        }[type(node)](node, indent)

    def view_assignment(self, node: AssignmentAst, indent: int = 0):
        self._print_indented("assignment:", indent)

        self._print_indented("identifier:", indent + 1)
        self._print_indented(node.symbol.identifier.value, indent + 2)

        self._print_indented("value:", indent + 1)
        self.view_node(node.value, indent + 2)

    def view_expression(self, node: ExpressionAst, indent: int = 0):
        self._print_indented("expression:", indent)
        self.view_node(node.left, indent + 1)
        self._print_indented(node.operator.value, indent + 1)
        self.view_node(node.right, indent + 1)

    def view_function_call(self, node: FunctionCallAst, indent: int = 0):
        self._print_indented("function call:", indent)

        self._print_indented("identifier:", indent + 1)
        self._print_indented(node.symbol.identifier.value, indent + 2)

        self._print_indented("arguments:", indent + 1)
        for argument in node.arguments:
            self.view_node(argument, indent + 2)

    def view_function_parameters_declaration(self, node: FunctionParametersDeclarationAst, indent: int = 0):
        self._print_indented("function parameters declaration:", indent)

        for parameter in node.parameters:
            self.view_node(parameter, indent + 1)

    def view_jump(self, node: JumpAst, indent: int = 0):
        self._print_indented("jump:", indent)
        self._print_indented("expression:", indent + 1)

        self.view_node(node.expression, indent + 2)

    def view_number(self, node: NumberAst, indent: int = 0):
        self._print_indented("number:", indent)
        self._print_indented(node.value, indent + 1)

    def view_string_literal(self, node: StringLiteralAst, indent: int = 0):
        self._print_indented("string literal:", indent)
        self._print_indented(node.value, indent + 1)

    def view_symbol_reference(self, node: SymbolReferenceAst, indent: int = 0):
        self._print_indented("symbol reference:", indent)
        self._print_indented(node.identifier.value, indent + 1)

    def view_variable_declaration(self, node: VariableDeclarationAst, indent: int = 0):
        self._print_indented("variable declaration:", indent)

        self._print_indented("identifier:", indent + 1)
        self._print_indented(node.symbol.identifier.value, indent + 2)

        self._print_indented("type:", indent + 1)
        self._print_indented(node.type_hint.value, indent + 2)

    def view_code_block(self, node: CodeBlockAst, indent: int = 0):
        self._print_indented("code block:", indent)

        for expression in node.expressions:
            self.view_node(expression, indent + 1)

    def view_function_declaration(self, node: FunctionDeclarationAst, indent: int = 0):
        self._print_indented("function declaration:", indent)

        self._print_indented("identifier:", indent + 1)
        self._print_indented(node.symbol.identifier.value, indent + 2)

        self._print_indented("parameters:", indent + 1)
        for parameter in node.parameters.parameters:
            self.view_node(parameter, indent + 2)

        self._print_indented("return type:", indent + 1)
        self._print_indented(node.return_type.value, indent + 2)

        self._print_indented("body:", indent + 1)
        self.view_node(node.block, indent + 2)

    def _print_indented(self, value: str, indent: int, end: str = "\n"):
        print(f"{'    ' * indent}{value}", end=end)
