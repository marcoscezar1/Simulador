
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
x = True

a = {1: 'a'}
print(a[1])'''


from simulador import Simulador
from Modelos import graph
from Modelos import node
from Modelos import usuario
import csv
import pandas as pd



def lerArq(n):
    global leitorArq
    leitorArq=[]
    with open(n) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=",")
        for linha in csvReader:
            leitorArq.append(linha)



def criandoNode():
    for j in range(1, len(matrizAdj[0])):
        listaN.append(node.Node(matrizAdj[0][j]))
        grafo.createNode(listaN[j-1])
    for i in range(1, len(matrizAdj)):
        for j in range(1, len(matrizAdj[i])):
            if matrizAdj[i][j]=='1':
                if matrizAdj[0][j]==listaN[j-1].id:
                    listaN[j-1].adcVizinho(listaN[i-1])



'''def alocaInfoDataset():
    campos=[]
    for j in range(1, len(leitorArq[0])):
        for i in range(len(leitorArq)):
            print(leitorArq[j][i])'''



grafo= graph.Graph()
lerArq("matriz-adj.csv")
matrizAdj=leitorArq
listaN=[]
criandoNode()
grafo.createArcs()



'''lerArq("C://Users//mbela//Downloads//dataset-filtrado.csv")
matizInfoDS=leitorArq
alocaInfoDataset()'''


simula=Simulador(0,grafo)
f=open("dataset-filtrado(1).csv", newline='')
dataset=csv.reader(f)



simula.realizaSimulacao(dataset)



'''300000'''