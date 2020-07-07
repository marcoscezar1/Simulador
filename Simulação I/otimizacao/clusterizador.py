import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer


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

    def gerarElbow(self):
        pass

    def gerar(self):
        pass

    def gerarClusters(self):
        pass
    
    def gerarGrafico(self):
        model = KMeans()
        visualizer = KElbowVisualizer(model, k=(1,10))
        visualizer.fit(self.dataset)
        visualizer.show()
