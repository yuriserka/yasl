from src.utils.token import Token
from src.ast import Ast


class ExpressionAst(Ast):
    def __init__(self, left: Ast, operator: Token, right: Ast):
        super().__init__(left, operator, right)
        self.left: Ast = left
        self.operator: Token = operator
        self.right: Ast = right
