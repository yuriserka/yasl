from abc import ABC


class Ast(ABC):
    def __init__(self, *args):
        self.nodes: list[Ast] = list(args)

    def append(self, node):
        self.nodes.append(node)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nodes})"
