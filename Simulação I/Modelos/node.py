class Node:
    def __init__(self):
        self.id = "s"
        self.local = "s"
        self.vizinhos = []
        self.qtd_de_usuarios = 0
        self.usuarios = []
        self.limite_de_usuarios = 14

    def adcUsuario(self, usuario):
        if(self.qtd_de_usuarios >= self.limite_de_usuarios):
            raise Exception("Não há como colocar mais usuarios no AP")
        self.usuarios.append(usuario)
        self.qtd_de_usuarios += 1

    def removeUsuario(self, usuario):
        if(usuario == []):
            raise Exception("Não há usuarios no AP")
        self.usuarios.append(usuario)
        self.qtd_de_usuarios -= 1

    def adcVizinho(self, node):
        self.vizinhos.append(node)