import networkx as nx

def inicializaGrafo(grafo):
    grafo_aux = sorted(grafo, key=lambda node: len(node.vizinhos))
    tam = len(grafo_aux) - 1
    while tam > 0:
        node = grafo_aux[tam]
        nao_tem_vizinho_ligado = True
        for vizinho in node.vizinhos:
            if(vizinho.status):
                nao_tem_vizinho_ligado = False
                break
        if(nao_tem_vizinho_ligado):
            node.ligarPA()
        tam -= 1

def inicializaGrafoMaiorQtdVizinhos(grafo):
    grafo_aux = sorted(grafo, key=lambda node: len(node.vizinhos))
    tam = len(grafo_aux) - 1
    maior_qtd = len(grafo_aux[tam - 1].vizinhos)
    while (tam > 0 and len(grafo_aux[tam].vizinhos) == maior_qtd):
        grafo_aux[tam].ligarPA()
        tam -= 1


'''
def inicializaVizinhos(grafo):
    apslig=[]
    for ind in range(6):
        maior=(None, 0)
        for i in grafo.nodes:
            if len(i.vizinhos)>=maior[1]:
                jaExiste=False
                for j in range(len(apslig)):
                    if i.id==apslig[j][0].id:
                        jaExiste=True
                        break
                if jaExiste==False:
                    ehVizinho=False
                    for j in range(len(apslig)):
                        for z in apslig[j][0].vizinhos:
                            if z.id==i.id:
                                ehVizinho=True
                                break
                    if ehVizinho==False:
                        maior=(i, len(i.vizinhos))
        apslig.append(maior)
        maior[0].ligarPA()
        print(maior[0].id)

'''

def acha_ap_pra_ligar(lista_de_nodes):
    lista_de_nodes_aux = sorted(lista_de_nodes, key=lambda node: len(node.vizinhos))

    tam = len(lista_de_nodes) - 1
    verificador = False
    while tam > 0:
        node = lista_de_nodes_aux[tam]
        for vizinho in node.vizinhos:
            if (vizinho.status == True):
                verificador = True
        if (verificador == False):
            return node
        else:
            tam -= 1
            verificador = False

    return lista_de_nodes_aux[len(lista_de_nodes) - 1]


def inicializaComClique(grafo):
    cliques = nx.find_cliques(grafo)
    for nodes in cliques:
        para_ligar = acha_ap_pra_ligar(nodes)
        para_ligar.status = True