from src.ast.expression import ExpressionAst
from src.ast import Ast


class CodeBlockAst(Ast):
    def __init__(self, expressions: list[ExpressionAst]):
        super().__init__(*expressions)
        self.expressions: list[ExpressionAst] = expressions
