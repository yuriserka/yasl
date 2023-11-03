from src.ast.symbol_reference import SymbolReferenceAst
from src.ast import Ast
from src.ast.expression import ExpressionAst


class FunctionCallAst(Ast):
    def __init__(self, symbol: SymbolReferenceAst, arguments: list[ExpressionAst]):
        super().__init__(symbol, *arguments)
        self.symbol: SymbolReferenceAst = symbol
        self.arguments: list[ExpressionAst] = arguments
