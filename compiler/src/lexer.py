from src.utils.regex import RegexUtils
from src.utils.token import Token, TokenType
from src.utils.exceptions import UnexpectedCharacterException, LexerException


class Lexer:
    def __init__(self, file_name: str):
        self.file_name: str = file_name
        with open(file_name, "r") as file:
            source_code = file.read()
            self.file_content: str = source_code
        self._idx: int = 0
        self._col: int = 1
        self._row: int = 1

    def tokenize(self) -> list[Token]:
        tokens: list[Token] = []
        while not self._eof():
            ch = self._peek()
            if RegexUtils.is_whitespace(ch):
                if ch == '\n':
                    self._row += 1
                    self._col = 1
                self._consume()
            elif RegexUtils.is_comment(ch):
                self.tokenize_comment()
            elif RegexUtils.is_identifier(ch):
                tokens.append(self.tokenize_identifier())
            elif RegexUtils.is_number(ch):
                tokens.append(self.tokenize_number())
            elif RegexUtils.is_operator(ch):
                tokens.append(self.tokenize_operator())
            elif ch == '"' or ch == "'":
                tokens.append(self.tokenize_string())
            elif RegexUtils.is_punctuation(ch):
                tokens.append(Token(self._consume(), TokenType.PUNCTUATION))
            elif ch == ':':
                tokens.append(Token(self._consume(), TokenType.COLON))
            elif ch == ',':
                tokens.append(Token(self._consume(), TokenType.COMMA))
            elif ch == ';':
                tokens.append(Token(self._consume(), TokenType.SEMICOLON))
            else:
                raise LexerException(
                    self.file_name,
                    self._row,
                    self._col,
                    UnexpectedCharacterException(ch)
                )

        return tokens

    def tokenize_identifier(self) -> Token:
        token = self._safe_consume_while(RegexUtils.is_identifier)
        if self._peek() == '.':
            token += self._consume() + self._safe_consume_while(RegexUtils.is_identifier)

        if RegexUtils.is_keyword(token):
            return Token(token, TokenType.KEYWORD)
        if RegexUtils.is_builtin_function(token):
            return Token(token, TokenType.BUILTIN_FUNCTION)
        if RegexUtils.is_builtin_data_type(token):
            return Token(token, TokenType.BUILTIN_DATA_TYPE)
        return Token(token, TokenType.IDENTIFIER)

    def tokenize_number(self) -> Token:
        token = self._safe_consume_while(RegexUtils.is_number)
        if (self._peek() == '.'):
            token += self._consume() + self._safe_consume_while(RegexUtils.is_number)
        return Token(token, TokenType.NUMBER)

    def tokenize_comment(self) -> Token:
        self._safe_consume_while(lambda ch: ch != '\n')

    def tokenize_operator(self) -> Token:
        token = self._consume()
        if (token in ['>', '<', '!', '='] and self._peek() == '=') or (token in ['&', '|'] and self._peek() == token):
            token += self._consume()
        if RegexUtils.is_assignment(token):
            return Token(token, TokenType.ASSIGN)
        if RegexUtils.is_list_ctr(token):
            return Token(token, TokenType.LIST_CTR)
        return Token(token, TokenType.OPERATOR)

    def tokenize_string(self) -> Token:
        token = self._consume()
        token = self._safe_consume_while(lambda ch: ch != token[0])
        self._consume()
        return Token(token, TokenType.STRING)

    def _safe_consume_while(self, comparator) -> str:
        token = ''
        while not self._eof() and comparator(self._peek()):
            token += self._consume()
        return token

    def _consume(self, look_ahead: int = 1) -> str:
        content = self.file_content[self._idx:self._idx + look_ahead]
        self._idx += look_ahead
        self._col += look_ahead
        return content if look_ahead > 1 else content[0]

    def _peek(self, look_ahead: int = 0) -> str:
        return self.file_content[self._idx + look_ahead]

    def _eof(self) -> bool:
        return self._idx >= len(self.file_content)
