class Graph:
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def createNode(self, node):
        self.nodes.append(node)

    def createArcs(self):
        for i in self.nodes:
            for j in i.vizinhos:
                if ((i.id, j.id) not in self.arcs) and((j.id, i.id) not in self.arcs):
                    self.arcs.append((i,j))
