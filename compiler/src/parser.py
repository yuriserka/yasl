from src.ast.string_literal import StringLiteralAst
from src.ast.number import NumberAst
from src.ast.symbol_reference import SymbolReferenceAst
from src.ast.jump import JumpAst
from src.ast.assignment import AssignmentAst
from src.ast.function_call import FunctionCallAst
from src.ast.expression import ExpressionAst
from src.ast.code_block import CodeBlockAst
from src.ast.function_declaration import FunctionDeclarationAst
from src.ast.function_parameters_declaration import FunctionParametersDeclarationAst
from src.ast.variable_declaration import VariableDeclarationAst
from src.utils.exceptions import UnexpectedTokenException
from src.utils.token import Token, TokenType
from src.ast import Ast


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens: list[Token] = tokens
        self._idx: int = 0

    def parse(self) -> Ast:
        ast = Ast()
        while not self._eot():
            token = self._peek()
            if token.value == 'fn':
                ast.append(self.parse_function_definition())
            elif token.value == 'let':
                ast.append(self.parse_variable_declaration())
            else:
                raise UnexpectedTokenException(self.tokens, self._idx)

        return ast

    def parse_function_definition(self) -> Ast:
        self._consume()	 # fn
        fn_id = self.parse_symbol_reference()
        self._consume()  # (
        parameters = self.parse_function_parameters_declaration()
        self._consume()	 # )
        fn_type = self.parse_type_hint()
        fn_block = self.parse_code_block()

        return FunctionDeclarationAst(fn_id, parameters, fn_type, fn_block)

    def parse_function_parameters_declaration(self) -> Ast:
        parameters = []

        while self._peek().value != ')':
            param_id = self.parse_symbol_reference()
            param_type = self.parse_type_hint()

            parameters.append(VariableDeclarationAst(param_id, param_type))

            if self._peek().token_type == TokenType.COMMA:
                self._consume()  # ,

        return FunctionParametersDeclarationAst(parameters)

    def parse_code_block(self) -> Ast:
        self._consume()  # {
        expressions = []
        while self._peek().value != '}':
            if self._peek().value == 'let':
                expressions.append(self.parse_variable_declaration())
            else:
                expressions.append(self.parse_statement())
        self._consume()  # }
        ast = CodeBlockAst(expressions)

        return ast

    def parse_statement(self) -> ExpressionAst:
        if self._peek().value == '{':
            return self.parse_code_block()
        elif self._peek().value == 'return':
            return self.parse_return_statement()
        # TODO: add if,for,builtin statements
        else:
            return self.parse_expression()

    def parse_return_statement(self) -> Ast:
        self._consume()  # return
        expression = self.parse_or_expression()
        self._consume()  # ;
        return JumpAst(expression)

    def parse_expression(self) -> Ast:
        if self._peek().token_type == TokenType.IDENTIFIER:
            if self._peek(look_ahead=1).token_type == TokenType.ASSIGN:
                assignment = self.parse_assignment()
                self._consume()  # ;
                return assignment

        expression = self.parse_or_expression()
        self._consume()  # ;
        return expression

    def parse_assignment(self) -> Ast:
        var_id = self.parse_symbol_reference()
        self._consume()  # =
        expression = self.parse_or_expression()

        return AssignmentAst(var_id, expression)

    def parse_or_expression(self) -> Ast:
        return self._parse_expression_with_operator(
            ['||'],
            self.parse_and_expression
        )

    def parse_and_expression(self) -> Ast:
        return self._parse_expression_with_operator(
            ['&&'],
            self.parse_equality_expression
        )

    def parse_equality_expression(self) -> Ast:
        return self._parse_expression_with_operator(
            ['==', '!='],
            self.parse_comparison_expression
        )

    def parse_comparison_expression(self) -> Ast:
        return self._parse_expression_with_operator(
            ['<', '>', '<=', '>='],
            self.parse_addition_expression
        )

    def parse_addition_expression(self) -> Ast:
        return self._parse_expression_with_operator(
            ['+', '-'],
            self.parse_multiplication_expression
        )

    def parse_multiplication_expression(self) -> Ast:
        return self._parse_expression_with_operator(
            ['*', '/', '%'],
            self.parse_unary_expression
        )

    # TODO: add list constructor

    def parse_unary_expression(self) -> Ast:
        if self._peek().value in ['!', '-']:
            operator = self._consume()
            return ExpressionAst(
                None,
                operator,
                self.parse_unary_expression()
            )
        return self.parse_postfix_expression()

    def parse_postfix_expression(self) -> Ast:
        if self._peek().token_type == TokenType.IDENTIFIER:
            if self._peek(look_ahead=1).value == '(':
                return self.parse_function_call()

        return self.parse_primary_expression()

    def parse_primary_expression(self) -> Ast:
        if self._peek().token_type == TokenType.IDENTIFIER:
            return self.parse_symbol_reference()
        elif self._peek().token_type == TokenType.NUMBER or self._peek().value in ['true', 'false']:
            return NumberAst(self._consume())
        elif self._peek().token_type == TokenType.STRING:
            return StringLiteralAst(self._consume())
        elif self._peek().value == '(':
            return self.parse_parenthesized_expression()

    def parse_parenthesized_expression(self) -> Ast:
        self._consume()  # (
        expression = self.parse_expression()
        self._consume()  # )
        return expression

    def parse_function_call(self) -> Ast:
        fn_id = self.parse_symbol_reference()
        self._consume()  # (
        params = []

        while self._peek().value != ')':
            params.append(self.parse_or_expression())
            if self._peek().token_type == TokenType.COMMA:
                self._consume()  # ,

        self._consume()  # )

        return FunctionCallAst(fn_id, params)

    def parse_type_hint(self) -> Token:
        self._consume()  # :
        return self._consume()

    def parse_symbol_reference(self) -> Ast:
        return SymbolReferenceAst(self._consume())

    def parse_variable_declaration(self) -> Ast:
        self._consume()  # let
        var_id = self.parse_symbol_reference()
        type_hint = self.parse_type_hint()
        self._consume()  # ;
        return VariableDeclarationAst(var_id, type_hint)

    def _parse_expression_with_operator(
        self,
        operators: list[str],
        next_expression_parser: callable
    ) -> Ast:
        expression = next_expression_parser()
        while self._peek().value in operators:
            operator = self._consume()
            expression = ExpressionAst(
                expression,
                operator,
                next_expression_parser()
            )
        return expression

    def _safe_consume_while(self, comparator) -> list[Token]:
        tokens = []
        while not self._eot() and comparator(self._peek()):
            tokens.append(self._consume())
        return tokens

    def _consume(self, look_ahead: int = 1) -> Token:
        content = self.tokens[self._idx:self._idx + look_ahead]
        self._idx += look_ahead
        return content if look_ahead > 1 else content[0]

    def _peek(self, look_ahead: int = 0) -> Token:
        return self.tokens[self._idx + look_ahead]

    def _eot(self) -> bool:
        return self._idx >= len(self.tokens)
