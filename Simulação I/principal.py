
'''from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from yellowbrick.cluster import KElbowVisualizer
df = pd.read_csv("../matriz-adj.csv")
df = df.drop(columns='Unnamed: 0')
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(self.dataset)
visualizer.show()
self.dataset = True

a = {1: 'a'}
print(a[1])'''


from simulador import Simulador
import graph
import node
import usuario
import clusterizador as cls
import csv



def lerArq(n):
    leitorArq=[]
    with open(n) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")

        for linha in csvReader:
            leitorArq.append(linha)
    return leitorArq



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


def createElbow(dir):
    cluster = cls.Clusterizador(dir)
    cluster.abrirDataSet()
    cluster.gerarGrafico()



'''def alocaInfoDataset():
    campos=[]
    for j in range(1, len(leitorArq[0])):
        for i in range(len(leitorArq)):
            print(leitorArq[j][i])'''



grafo= graph.Graph()
matrizAdj= lerArq("matriz-adj.csv")

criandoNode(matrizAdj)
grafo.createArcs()


cluster = cls.Clusterizador("matriz-adj.csv")
cluster.abrirDataSet()
cluster.gerarClusters()


simula=simulador.Simulador(0,grafo)
f=open("dataset-filtrado(1).csv", newline='')
dataset=csv.reader(f)
simula.realizaSimulacao(dataset)

