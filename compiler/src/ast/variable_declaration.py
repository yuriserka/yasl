from src.ast.symbol_reference import SymbolReferenceAst
from src.ast import Ast
from src.utils.token import Token


class VariableDeclarationAst(Ast):
    def __init__(self, symbol: SymbolReferenceAst, type_hint: Token):
        super().__init__(symbol, type_hint)
        self.symbol: SymbolReferenceAst = symbol
        self.type_hint: Token = type_hint
