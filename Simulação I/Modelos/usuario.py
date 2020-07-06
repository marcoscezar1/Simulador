class Usuario:
    def __init__(self, id, tempo_de_chegada, tempo_de_saida):
        self.id = id
        self.tempo_de_chegada = tempo_de_chegada
        self.tempo_de_saida = tempo_de_saida
        self.node_associado = None

    def adcNode(self, node):
        if(self.node_associado == None):
            self.node_associado = node
        raise Exception("O usuario já está conectado a um ap")
