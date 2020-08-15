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




cluster = cls.Clusterizador("matriz-adj.csv")
cluster.abrirDataSet()
cluster.gerarDendograma()

'''
grafo= graph.Graph()
matrizAdj= lerArq("matriz-adj.csv")

grafo.create_nodes(matrizAdj)
grafo.create_arcs()
APsIniciais.inicializaVizinhos(grafo)

simula=simulador.Simulador(0,grafo)
numLinhas=ArqNumLinha("dataset-filtrado(1).csv")
f=open("dataset-filtrado(1).csv", newline='')
dataset=csv.reader(f)
simula.realizaSimulacao(dataset, numLinhas)
f.close()'''
