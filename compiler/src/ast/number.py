from src.ast import Ast
from src.utils.token import Token


class NumberAst(Ast):
    def __init__(self, token: Token):
        super().__init__(token)
        self.value: Token = token.value
