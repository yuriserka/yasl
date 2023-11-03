import sys
from src.viewer import Viewer
from src.lexer import Lexer
from src.parser import Parser


if __name__ == "__main__":
    parser = Parser(Lexer(file_name=sys.argv[1]).tokenize())
    ast = parser.parse()

    Viewer(ast).view()
