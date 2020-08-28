from graph import Graph
from node import Node

class Logger:
    def __init__(self, write_file: str):
        self.write_file = write_file
        self.file = None
        self.bytes_forward_file_name = 'bytes-fowrward'
        self.bytes_backward_file_name = 'bytes-backward'
        self.bytes_forward = None
        self.bytes_backward = None

    def open_file(self) -> None:
        self.file = open(self.write_file, 'w')
        self.bytes_backward = open(self.bytes_backward_file_name, 'w')
        self.bytes_forward = open(self.bytes_forward_file_name, 'w')

    def close_file(self) -> None:
        self.file.close()
        self.bytes_backward.close()
        self.bytes_forward.close()

    def write_in_file(self, graph: Graph, bytes_forward, bytes_backward) -> None:
        for node in graph.nodes:
            self.file.write("[{}, {}, {}] ".format(node.id, node.status, node.qtd_de_usuarios))
        self.file.write("\n")
        self.file.write(str(graph.nao_servido) + "\n")
        
        self.bytes_forward.write(str(bytes_forward) + "\n")
        self.bytes_backward.write(str(bytes_backward) + "\n")
