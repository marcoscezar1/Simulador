import usuario
class Simulador:
    def __init__(self, eventos, grafo):
        self.duracao_simulacao = 8640000000
        self.momento_autal = 0
        self.grafo = grafo
        self.tempo_de_atualizacao = 300000
        self.eventos = eventos
        self.usuarios = []
        self.tempoInicial = 1523997983560



    def adicionaUser(self, user):
        self.usuarios.append(user)

    '''def tirarConexao(self, user, node):'''

    def transferirUsuarios(self, apSai, apEntra):
        for i in apSai.usuarios:
            apSai.removeUsuario(i)
            i.removeNode(apSai)

            apEntra.adcUsuario(i)
            i.adcNode(apEntra)
        apSai.desligarPA()



    def reorganizaUsuarios(self):
        for i in self.grafo.nodes:
            if i.status==True and i.qtd_de_usuarios>0:
                for j in i.vizinhos:
                    if j.status==True and i.status==True:
                        if i.qtd_de_usuarios<=j.qtd_de_usuarios:
                            if i.qtd_de_usuarios+j.qtd_de_usuarios<=15:
                                '''passar usuarios de i para j'''
                                self.transferirUsuarios(i, j)





    def verificaConexao(self):
        for i in self.usuarios:
            if self.momento_autal>=i.tempo_de_saida:
                estavaLotado=False
                for j in self.grafo.nodes:

                    if(i.node_associado!=None) and (j.id==i.node_associado.id):

                        j.removeUsuario(i)
                        i.removeNode(j)
                        i.desconecta()


                        if j.qtd_de_usuarios==0 :
                            j.desligarPA()



    def realocaAPLigar(self, ap):
        for i in self.usuarios:
            if i.node_associado != None:
                if i.node_associado.id!=i.ap_preferencial:
                    if ap.id==i.ap_preferencial:
                        '''desassociar'''
                        aptemp=i.node_associado
                        aptemp.removeUsuario(i)
                        i.removeNode(aptemp)

                        '''associar'''
                        ap.adcUsuario(i)
                        if ap.situacao_inadequada==False:
                            i.adcNode(ap)
        ap_primeiro_elem=ap.usuarios[0]
        for i in self.grafo.nodes:
            if i.id==ap_primeiro_elem.ap_preferencial:
                if i.qtd_de_usuarios<15:
                    '''desassociar'''
                    ap.removeUsuario(ap_primeiro_elem)
                    ap_primeiro_elem.removeNode(ap)

                    '''associar'''
                    i.adcUsuario(ap_primeiro_elem)
                    ap_primeiro_elem.adcNode(i)








    def ligaraoAP(self, ap, usuario):
        '''se o AP estiver desligado'''
        if ap.status == False:
            maior = (None, -1)
            '''busca por AP vizinho com maior número de usuários'''

            for i in ap.vizinhos:
                if i.status == True and i.qtd_de_usuarios < 15 and maior[1] < i.qtd_de_usuarios:


                    maior = (i, i.qtd_de_usuarios)
            '''Se tiver AP vizinho ligado e válido'''
            if maior[0] != None:
                maior[0].adcUsuario(usuario)
                usuario.adcNode(maior[0])
                usuario.conecta()

            '''Se não tiver AP vizinho ligado ou válido'''
            if maior[0] == None:
                ap.ligarPA()
                ap.adcUsuario(usuario)
                usuario.adcNode(ap)
                usuario.conecta()
                self.realocaAPLigar(ap)



        elif ap.status == True:
            '''observar se da erro'''
            '''Se o AP estiver Ligado'''
            ap.adcUsuario(usuario)
            '''Se o AP for válido(não estiver lotado)'''
            if ap.situacao_inadequada == False:
                usuario.adcNode(ap)
                usuario.conecta()
            '''Se o AP nâo for vàlido(estiver lotado)'''
            if ap.situacao_inadequada == True:
                '''apsLig=[]'''
                maior=(None, -1)
                '''busca por AP vizinho com maior número de usuários'''
                for i in ap.vizinhos:
                    if i.status==True and i.qtd_de_usuarios<15 and maior[1]<i.qtd_de_usuarios:
                        maior=(i, i.qtd_de_usuarios)
                '''Se tiver AP vizinho ligado e válido'''
                if maior[0]!=None:
                    maior[0].adcUsuario(usuario)
                    usuario.adcNode(maior[0])
                    usuario.conecta()
                '''Se não tiver AP vizinho ligado ou válido'''
                if maior[0] == None:
                    maior2=(None, -1)
                    for i in ap.vizinhos:
                        '''Comparo os APs vizinhos desligados para ligar o que tem maior número de vizinhos'''
                        if i.status==False and maior2[1]<len(i.vizinhos):
                            maior2=(i, len(i.vizinhos))
                    '''Se existir AP vizinho desligado'''
                    if maior2[0]!=None:
                        maior2[0].ligarPA()
                        maior2[0].adcUsuario(usuario)
                        usuario.adcNode(maior2[0])
                        usuario.conecta()
                        self.realocaAPLigar(maior2[0])
                    '''Se não existir AP vizinho desligado'''
                    if maior2[0] == None:
                        print("Usuario nao conseguiu se conectar!!!!")



    def realizaSimulacao(self, dataset):
        ultimaLinha = None
        campos=next(dataset)
        while self.momento_autal!=self.duracao_simulacao:
            '''jaExiste = False'''
            '''linha=next(dataset)'''


            linha = []
            if self.momento_autal != 0:
                linha.append(ultimaLinha)
            while True:
                linha.append(next(dataset))
                if (float(linha[len(linha) - 1][3])*1000)- self.tempoInicial >= self.momento_autal + 60000:
                    ultimaLinha = linha[len(linha) - 1]

                    break
            '''criar um if para caso o arquivo terminar'''

            for conex in range(len(linha)-2):
                jaExiste = False

                id=linha[conex][5]
                tempoChegada=(float(linha[conex][3])*1000)-self.tempoInicial
                tempoSaida=((float(linha[conex][3])*1000)-self.tempoInicial)+(float(linha[conex][4])*1000)+(float(self.tempo_de_atualizacao)*1000)
                ap=linha[conex][6]


                for i in self.usuarios:
                    if id == i.id:
                        i.mudarTemposInOut(tempoChegada, tempoSaida)
                        jaExiste=True


                        if i.estaConectado() == False:

                            for j in self.grafo.nodes:
                                if j.id == ap:
                                    self.ligaraoAP(j, i)
                                    '''if j.status == False:
                                        j.ligarPA()
    
                                    j.adcUsuario(i)
                                    if j.situacao_inadequada==False:
                                        i.adcNode(j)
                                        i.conecta()'''



                if jaExiste==False:
                    user=usuario.Usuario(id, tempoChegada, tempoSaida, ap)
                    Simulador.adicionaUser(self, user)

                    for i in self.grafo.nodes:
                        if i.id==ap:
                            self.ligaraoAP(i, user)
                            '''if i.status==False:
                                i.ligarPA()
    
                            i.adcUsuario(user)
    
                            if i.situacao_inadequada==False:
                                user.adcNode(i)
                                user.conecta()'''


            Simulador.verificaConexao(self)
            self.reorganizaUsuarios()

            '''if(self.momento_autal%self.tempo_de_atualizacao==0)and(self.momento_autal!=0):
                for i in self.grafo.nodes:
                    print()
                pass'''

            a=input()
            for i in self.usuarios:
                print(i.id ," - ",i.tempo_de_chegada," - ",i.tempo_de_saida," - ",i.node_associado.id," - ",i.conectado, " - ", i.ap_preferencial)
                for j in i.node_associado.vizinhos:
                    print("---",j.id ,"---")
                print("-------------------------")

            for i in self.grafo.nodes:
                if i.status==True:
                    print(i.id, i.qtd_de_usuarios, i.status)
                '''for j in i.vizinhos:
                    if i.status==True:
                        print("--", j.id,"--", j.status, end="")
                print()'''




            '''print(self.usuarios[0].estaConectado(), self.usuarios[0].id, self.usuarios[0].tempo_de_saida, self.momento_autal, self.usuarios[0].node_associado)'''
            '''print(self.usuarios[len(self.usuarios)-1].id,self.usuarios[len(self.usuarios)-1].tempo_de_chegada, self.usuarios[len(self.usuarios)-1].tempo_de_saida)'''
            
            self.momento_autal += 60000
            '''60000'''




