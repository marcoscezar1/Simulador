'''class Graph:
    def __init__(self):
        self.nodes = []
        self.arcs = []
        self.nao_servido = 0

    def createNode(self, node):
        self.nodes.append(node)

    def createArcs(self):
        for i in self.nodes:
            for j in i.vizinhos:
                if ((i.id, j.id) not in self.arcs) and((j.id, i.id) not in self.arcs):
                    self.arcs.append((i,j))

    def increment_nao_servido(self):
        self.nao_servido += 1'''


import networkx as nx
from node import Node


class Graph(nx.Graph):
    def __init__(self):
        super().__init__()
        self.arcs=[]
        self.nao_servido = 0

    def increment_nao_servido(self):
        self.nao_servido += 1

    def decrement_nao_servido(self):
        self.nao_servido -= 1

    def create_node(self, id: str) -> Node:
        node = Node(id)
        return node

    def create_nodes(self, matrix):
        listaN = []
        dict_ap = {}
        for i in range(1, len(matrix[0])):
            node_name = matrix[0][i]
            node = self.create_node(node_name)
            listaN.append(node)
            dict_ap[node_name] = node
        self.add_nodes_from(listaN)
        multiple = set()
        i = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == '1':
                    if(not (matrix[0][j], matrix[i][0]) in multiple):
                        dict_ap[matrix[0][j]].add_neighbor(
                            dict_ap[matrix[i][0]])
                        dict_ap[matrix[i][0]].add_neighbor(
                            dict_ap[matrix[0][j]])
                        self.add_edge(dict_ap[matrix[0][j]],
                                      dict_ap[matrix[i][0]])
                        multiple.add((matrix[0][j], matrix[i][0]))
                        multiple.add((matrix[i][0], matrix[0][j]))

    def create_arcs(self):
        for i in self.nodes:
            for j in i.vizinhos:
                if ((i.id, j.id) not in self.arcs) and ((j.id, i.id) not in self.arcs):
                    self.arcs.append((i, j))
