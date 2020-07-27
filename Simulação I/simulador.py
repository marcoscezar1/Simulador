from Modelos import usuario
class Simulador:
    def __init__(self, eventos, grafo):
        self.duracao_simulacao = 86400000
        self.momento_autal = 0
        self.grafo = grafo
        self.tempo_de_atualizacao = 300000
        self.eventos = eventos
        self.usuarios = []
        self.tempoInicial = 1523997983.56



    def adicionaUser(self, user):
        self.usuarios.append(user)

    '''def tirarConexao(self, user, node):'''


    def verificaConexao(self):
        for i in self.usuarios:
            if self.momento_autal>=i.tempo_de_saida:
                for j in self.grafo.nodes:
                    if(i.node_associado!=None) and (j.id==i.node_associado.id):

                        j.removeUsuario(i)
                        i.removeNode(j)
                        i.desconecta()

                        if j.qtd_de_usuarios==0:
                            j.desligarPA()



    def realizaSimulacao(self, dataset):
        ultimaLinha = None
        campos=next(dataset)
        while self.momento_autal!=self.duracao_simulacao:
            jaExiste=False


            linha = []
            if self.momento_autal != 0:
                linha.append(ultimaLinha)
            while True:
                linha.append(next(dataset))
                if float(linha[len(linha) - 1][3])- self.tempoInicial >= self.momento_autal + 1000:
                    ultimaLinha = linha[len(linha) - 1]

                    break
                '''criar um if para caso o arquivo terminar'''

            for conex in range(len(linha)-2):

                id=linha[conex][5]
                tempoChegada=float(linha[conex][3])-self.tempoInicial
                tempoSaida=(float(linha[conex][3])-self.tempoInicial)+float(linha[conex][4])+self.tempo_de_atualizacao
                ap=linha[conex][6]


                for i in self.usuarios:
                    if id == i.id:
                        i.mudarTemposInOut(tempoChegada, tempoSaida)
                        jaExiste=True


                        if i.estaConectado() == False:

                            for j in self.grafo.nodes:
                                if j.id == ap:

                                    if j.status == False:
                                        j.ligarPA()

                                    j.adcUsuario(i)
                                    if j.situacao_inadequada==False:
                                        i.adcNode(j)
                                        i.conecta()



                if jaExiste==False:
                    user=usuario.Usuario(id, tempoChegada, tempoSaida)
                    Simulador.adicionaUser(self, user)

                    for i in self.grafo.nodes:
                        if i.id==ap:

                            if i.status==False:
                                i.ligarPA()

                            i.adcUsuario(user)

                            if i.situacao_inadequada==False:
                                user.adcNode(i)
                                user.conecta()


            Simulador.verificaConexao(self)

            '''if(self.momento_autal%self.tempo_de_atualizacao==0)and(self.momento_autal!=0):
                for i in self.grafo.nodes:
                    print()
                pass'''

            a=input()
            for i in self.usuarios:
                print(i.id ," - ",i.tempo_de_chegada," - ",i.tempo_de_saida," - ",i.node_associado," - ",i.conectado)
                print("-------------------------")




            '''print(self.usuarios[0].estaConectado(), self.usuarios[0].id, self.usuarios[0].tempo_de_saida, self.momento_autal, self.usuarios[0].node_associado)'''
            '''print(self.usuarios[len(self.usuarios)-1].id,self.usuarios[len(self.usuarios)-1].tempo_de_chegada, self.usuarios[len(self.usuarios)-1].tempo_de_saida)'''
            
            self.momento_autal += 60000
            '''60000'''






