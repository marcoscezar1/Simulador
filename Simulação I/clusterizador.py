import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import sklearn.metrics as metrics
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
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

    def plot_dendrogram(self, model, **kwargs):
        # Create linkage matrix and then plot the dendrogram

        # create the counts of samples under each node
        counts = np.zeros(model.children_.shape[0])
        n_samples = len(model.labels_)
        for i, merge in enumerate(model.children_):
            current_count = 0
            for child_idx in merge:
                if child_idx < n_samples:
                    current_count += 1  # leaf node
                else:
                    current_count += counts[child_idx - n_samples]
            counts[i] = current_count

        linkage_matrix = np.column_stack([model.children_, model.distances_,
                                        counts]).astype(float)

        # Plot the corresponding dendrogram
        sch.dendrogram(linkage_matrix, **kwargs)

    def gerarDendogramaSKL(self):
        #criando o modelo
        model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
        model = model.fit(self.dataset)

        #plotando o dendograma
        self.plot_dendrogram(model, truncate_mode='level', p=3)
        plt.title('Dendrogram')
        plt.xlabel('Aps')
        plt.ylabel('Euclidean distances')
        plt.show()

        #vendo a acurácia do modelo aplicando o n° de clusters apontado pelo dendograma
        model = AgglomerativeClustering( n_clusters=10)
        model = model.fit(self.dataset)
        labels = model.labels_
        #usando calinski score
        score = metrics.calinski_harabasz_score(self.dataset, labels)
        print(score)
        #usando silhouette score
        score = metrics.silhouette_score(self.dataset, labels)
        print(score)
        #alterando o número de clusters verifica-se que 2 é o mais eficiente

    def gerarDendogramaSP(self):
        dendogram = sch.dendrogram(sch.linkage(self.dataset, method="ward"))
        plt.title('Dendrogram')
        plt.xlabel('Aps')
        plt.ylabel('Euclidean distances')
        plt.show()

    def gerarElbow(self):
        model = KMeans(n_clusters=8)
        visualizer = KElbowVisualizer(model, k=(1,10))
        visualizer = visualizer.fit(self.dataset)     
        visualizer.show()

        labels = model.labels_
        #usando calinski score
        score = metrics.calinski_harabasz_score(self.dataset, labels)
        print("calinski = ", score)
        #usando silhouette score
        score = metrics.silhouette_score(self.dataset, labels)
        print("silhouette = ", score)
        #5 é o mais eficiente com KMeans mas menos que Hierarquico

    def gerarDBSCAN(self):
        model = DBSCAN()
        model = model.fit(self.dataset)
        labels = model.labels_

        #usando calinski score
        score = metrics.calinski_harabasz_score(self.dataset, labels)
        print("calinski = ", score)
        #usando silhouette score
        score = metrics.silhouette_score(self.dataset, labels)
        print("silhouette = ", score)
        #coeficientes muito baixos