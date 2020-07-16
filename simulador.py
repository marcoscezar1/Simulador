class Simulador:
    def __init__(self, eventos, grafo, usuarios):
        self.duracao_simulacao = 86400000
        self.momento_autal = 0
        self.grafo = grafo
        self.tempo_de_atualizacao = 300000
        self.eventos = eventos
        self.usuarios = usuarios

    def realizaSimulacao(self):
        while self.momento_autal!=self.duracao_simulacao:
            self.momento_autal+=1
            if(self.momento_autal%self.tempo_de_atualizacao==0):

                break
        pass

