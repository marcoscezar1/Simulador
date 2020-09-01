  
from graph import Graph
from node import Node

class Logger:
    def __init__(self):
        self.write_file = 'Resultados/aps.txt'
        self.file = None
        self.bytes_forward_file_name = 'Resultados/bytes-forward.txt'
        self.bytes_backward_file_name = 'Resultados/bytes-backward.txt'
        self.nao_servidos_file_name = 'Resultados/nao_servidos.txt'
        self.bytes_forward = None
        self.bytes_backward = None

    def open_file(self) -> None:
        self.file = open(self.write_file, 'w')
        self.bytes_backward = open(self.bytes_backward_file_name, 'w')
        self.bytes_forward = open(self.bytes_forward_file_name, 'w')
        self.nao_servidos_file = open(self.nao_servidos_file_name, 'w')

    def close_file(self) -> None:
        self.file.close()
        self.bytes_backward.close()
        self.bytes_forward.close()
        self.nao_servidos_file.close()

    def write_in_file(self, graph: Graph, bytes_forward: int, bytes_backward: int) -> None:
        for node in graph.nodes:
            self.file.write("[{}, {}, {}];".format(node.id, node.status, node.qtd_de_usuarios))
        self.file.write("\n")
        self.nao_servidos_file.write(str(graph.nao_servido) + '\n')
        self.bytes_forward.write(str(bytes_forward) + "\n")
        self.bytes_backward.write(str(bytes_backward) + "\n")
    