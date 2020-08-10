import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering



class Clusterizador:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dataset = None
        self.delimitadores = dict()

    def abrirDataSet(self):
        self.dataset = pd.read_csv(self.nome_arquivo)
        self.dataset = self.dataset.drop(columns='Unnamed: 0')

    def fecharDataSet(self):
        self.dataset = []

    def gerarDendograma(self):
        dendrogram = sch.dendrogram(sch.linkage(self.dataset, method = 'ward'))
        plt.title('Dendrogram')
        plt.xlabel('Aps')
        plt.ylabel('Euclidean distances')
        plt.show()