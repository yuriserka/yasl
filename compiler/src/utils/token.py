from enum import Enum


class TokenType(Enum):
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    OPERATOR = 'OPERATOR'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    PUNCTUATION = 'PUNCTUATION'
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'
    ASSIGN = 'ASSIGN'
    COLON = 'COLON'
    SEMICOLON = 'SEMICOLON'
    COMMA = 'COMMA'
    BUILTIN_FUNCTION = 'BUILTIN_FUNCTION'
    BUILTIN_DATA_TYPE = 'BUILTIN_DATA_TYPE'
    LIST_CTR = 'LIST_CTR'


class Token:
    def __init__(self, value: str, token_type: TokenType):
        self.value: str = value
        self.token_type: TokenType = token_type

    def __repr__(self):
        return f'<{self.token_type}, "{self.value}">'
