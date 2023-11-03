from src.ast import Ast
from src.utils.token import Token


class SymbolReferenceAst(Ast):
    def __init__(self, identifier: Token):
        super().__init__(identifier)
        self.identifier: Token = identifier
