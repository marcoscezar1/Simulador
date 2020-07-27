class Node:
    def __init__(self, id):
        self.id = id
        self.vizinhos = []
        self.qtd_de_usuarios = 0
        self.usuarios = []
        self.limite_de_usuarios = 15
        self.status = False
        self.situacao_inadequada = False
   
    def adcUsuario(self, usuario):
        self.situacao_inadequada=False
        if(not self.status):
            raise Exception("AP desligado")

        if(self.qtd_de_usuarios >= self.limite_de_usuarios):
            print("AP lotado")
            self.situacao_inadequada=True
        self.usuarios.append(usuario)
        self.qtd_de_usuarios += 1


    def removeUsuario(self, usuario):
        if(not self.status):
            raise Exception("AP desligado")

        if(usuario == []):
            raise Exception("Não há usuarios no AP")
        self.usuarios.append(usuario)
        self.qtd_de_usuarios -= 1

    def adcVizinho(self, node):
        self.vizinhos.append(node)

    def ligarPA(self):
        self.status = True

    def desligarPA(self):
        self.status = False
        '''antes o valor era True'''
