from src.ast.symbol_reference import SymbolReferenceAst
from src.ast.function_parameters_declaration import FunctionParametersDeclarationAst
from src.ast.code_block import CodeBlockAst
from src.utils.token import Token
from src.ast import Ast


class FunctionDeclarationAst(Ast):
    def __init__(
        self,
        symbol: SymbolReferenceAst,
        parameters: FunctionParametersDeclarationAst,
        return_type: Token,
        block: CodeBlockAst
    ):
        super().__init__(symbol, parameters, return_type, block)
        self.symbol: SymbolReferenceAst = symbol
        self.parameters: FunctionParametersDeclarationAst = parameters
        self.return_type: Token = return_type
        self.block: CodeBlockAst = block
