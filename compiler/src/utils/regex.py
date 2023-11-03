class RegexUtils:
    @staticmethod
    def is_identifier(token: str):
        has_valid_start = token[0].isalpha() or token[0] == '_'
        return (
            has_valid_start
            if len(token) == 1
            else has_valid_start and token[1:].isalnum()
        )

    @staticmethod
    def is_keyword(token: str):
        return token in ['fn', 'let', 'if', 'else', 'while',
                         'for', 'return', 'true', 'false']

    @staticmethod
    def is_builtin_function(token: str):
        return token in ['print', 'println', 'read']

    @staticmethod
    def is_builtin_data_type(token: str):
        base_types = ['number', 'string', 'bool']
        list_types = [f'list.{base_type}' for base_type in base_types]
        return token in [*base_types, *list_types]

    @staticmethod
    def is_operator(token: str):
        return token in ['+', '-', '*', '/', '%', '>', '<', '!', '=', '&', '|']

    @staticmethod
    def is_assignment(token: str):
        return token == '='

    @staticmethod
    def is_number(token: str):
        return token.isdigit()

    @staticmethod
    def is_list_ctr(token: str):
        return token == '|'

    @staticmethod
    def is_opening_punctuation(token: str):
        return token in ['(', '{', '[']

    @staticmethod
    def is_closing_punctuation(token: str):
        return token in [')', '}', ']']

    @staticmethod
    def is_punctuation(token: str):
        return RegexUtils.is_opening_punctuation(token) or RegexUtils.is_closing_punctuation(token)

    @staticmethod
    def is_comment(token: str):
        return token[0] == '#'

    @staticmethod
    def is_whitespace(token: str):
        return token.isspace()
