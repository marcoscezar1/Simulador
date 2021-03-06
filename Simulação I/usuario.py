class Usuario:
    def __init__(self, id, tempo_de_chegada, tempo_de_saida, ap, byteRecebido, byteEnviado):
        self.id = id
        self.tempo_de_chegada = tempo_de_chegada
        self.tempo_de_saida = tempo_de_saida
        self.node_associado = None
        self.conectado = False
        self.ap_preferencial=ap
        self.byteRecebido=byteRecebido
        self.byteEnviado=byteEnviado
        self.naoServido=False

    def adcNode(self, node):
        if(self.node_associado == None):
            self.node_associado = node

    def removeNode(self, node):
        self.node_associado = None
    
    def estaConectado(self):
        return self.conectado

    def desconecta(self):
        self.conectado=False

    def conecta(self):
        self.conectado=True



    def mudarTemposInOut(self, tempoChegada, tempoSaida):

        self.tempo_de_chegada=tempoChegada
        self.tempo_de_saida=tempoSaida


    def naofoiServido(self):
        self.naoServido=True

    def estaServido(self):
        self.naoServido=False
