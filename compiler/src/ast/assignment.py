from src.ast.symbol_reference import SymbolReferenceAst
from src.ast import Ast
from src.ast.expression import ExpressionAst


class AssignmentAst(Ast):
    def __init__(self, symbol: SymbolReferenceAst, value: ExpressionAst):
        super().__init__(symbol, value)
        self.symbol: SymbolReferenceAst = symbol
        self.value: ExpressionAst = value
