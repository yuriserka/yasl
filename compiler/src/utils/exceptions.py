from src.utils.token import Token


class LexerException(Exception):
    def __init__(self, file: str, row: int, col: int, exception: Exception):
        super().__init__(f'{exception.message} at {file}:{row}:{col}')


class UnexpectedCharacterException(Exception):
    def __init__(self, ch: str):
        self.message = f'Unexpected character: "{ch}"'
        super().__init__(self.message)


class ParserException(Exception):
    def __init__(self, row: int, col: int, exception: Exception):
        super().__init__(f'{exception.message} at {row}:{col}')


class UnexpectedTokenException(Exception):
    def __init__(self, tokens: list[Token], current_index: int):
        self.message = f'Unexpected token: "{tokens[current_index]}" ' \
                       f'surrounded by {tokens[current_index - 1]} and ' \
                       f'{tokens[current_index + 1]}'
        super().__init__(self.message)
