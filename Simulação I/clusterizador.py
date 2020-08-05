'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn_extra.cluster import KMedoids
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans


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
        # Applying PCA
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        tabela = pca.fit_transform(self.dataset)

        model = KMedoids(n_clusters=4, random_state=42)
        kmedoids = model.fit(tabela)

        plt.scatter(tabela[kmedoids == 0, 0], tabela[kmedoids == 0, 1], s=100, c='red', label='Cluster 1')
        plt.scatter(tabela[kmedoids == 1, 0], tabela[kmedoids == 1, 1], s=100, c='blue', label='Cluster 2')
        plt.scatter(tabela[kmedoids == 2, 0], tabela[kmedoids == 2, 1], s=100, c='green', label='Cluster 3')
        plt.scatter(tabela[kmedoids == 3, 0], tabela[kmedoids == 3, 1], s=100, c='cyan', label='Cluster 4')
        plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
        plt.title('Clusters')
        plt.legend()
        plt.show()

    def gerarGrafico(self):
        model = KMeans()
        visualizer = KElbowVisualizer(model, k=(1, 10))
        visualizer.fit(self.dataset)
        visualizer.show()'''