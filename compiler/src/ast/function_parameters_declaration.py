from src.ast.variable_declaration import VariableDeclarationAst
from src.ast import Ast


class FunctionParametersDeclarationAst(Ast):
    def __init__(self, parameters: list[VariableDeclarationAst]):
        super().__init__(*parameters)
        self.parameters: list[VariableDeclarationAst] = parameters
