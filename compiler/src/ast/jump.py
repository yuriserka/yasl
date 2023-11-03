from src.ast import Ast
from src.ast.expression import ExpressionAst


class JumpAst(Ast):
    def __init__(self, expression: ExpressionAst):
        super().__init__(expression)
        self.expression: ExpressionAst = expression
