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
                    maior=(i, len(i.vizinhos))
        apslig.append(maior)
        maior[0].ligarPA()
        print(maior[0].id)
