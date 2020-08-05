from graph import Graph
from node import Node


class Logger:
    def __init__(self, write_file: str):
        self.write_file = write_file
        self.file = None

    def open_file(self) -> None:
        self.file = open(self.write_file, 'w')

    def close_file(self) -> None:
        self.file.close()

    def write_in_file(self, graph: Graph) -> None:
        for node in graph.nodes:
            self.file.write("[{}, {}, {}] ".format(node.id, node.status, node.qtd_de_usuarios))
        self.file.write("\n")
        self.file.write(str(graph.nao_servido) + "\n")
