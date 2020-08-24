import simulador
import graph
import node
import usuario
import clusterizador as cls
import csv
import APsIniciais

def lerArq(n):
    leitorArq=[]
    with open(n) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")

        for linha in csvReader:
            leitorArq.append(linha)
    return leitorArq

def ArqNumLinha(n):
    qtdLinhas=0
    with open(n) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for linha in csvReader:
            qtdLinhas+=1
    return qtdLinhas

def criandoNode(mat):
    listaN=[]
    for j in range(1, len(mat[0])):
        listaN.append(node.Node(mat[0][j]))
        grafo.createNode(listaN[j-1])
    for i in range(1, len(mat)):
        for j in range(1, len(mat[i])):
            if mat[i][j]=='1':
                if mat[0][j]==listaN[j-1].id:
                    listaN[j-1].vizinhos.append(listaN[i-1])

grafo= graph.Graph()
matrizAdj= lerArq("matriz-adj.csv")

criandoNode(matrizAdj)
grafo.createArcs()
APsIniciais.inicializaVizinhos(grafo)

simula=simulador.Simulador(0,grafo)
numLinhas=ArqNumLinha("dataset-filtrado(1).csv")
f=open("dataset-filtrado(1).csv", newline='')
dataset=csv.reader(f)
simula.realizaSimulacao(dataset, numLinhas)
f.close()
