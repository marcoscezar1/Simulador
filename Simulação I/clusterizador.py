import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import scipy.cluster.vq
import scipy.spatial.distance
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from yellowbrick.cluster import KElbowVisualizer

dst = scipy.spatial.distance.euclidean


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

    def gerarElbow(self):
        model = KMeans()
        visualizer = KElbowVisualizer(model, k=(1,10))
        visualizer.fit(self.dataset)     
        visualizer.show()

    def gap(self, refs=None, nrefs=20, ks=range(1,11)):
        shape = self.dataset.shape
        if refs==None:
            tops = self.dataset.max(axis=0)
            bots = self.dataset.min(axis=0)
            dists = np.matrix(np.diag(tops-bots))
            

            rands = np.random.random_sample(size=(shape[0],shape[1],nrefs))
            for i in range(nrefs):
                rands[:,:,i] = rands[:,:,i]*dists+bots
        else:
            rands = refs

        gaps = np.zeros((len(ks),))
        for (i,k) in enumerate(ks):
            (kmc,kml) = np.cluster.vq.kmeans2(self.dataset, k)
            disp = sum([dst(self.dataset[m,:],kmc[kml[m],:]) for m in range(shape[0])])

            refdisps = np.zeros((rands.shape[2],))
            for j in range(rands.shape[2]):
                (kmc,kml) = np.cluster.vq.kmeans2(rands[:,:,j], k)
                refdisps[j] = sum([dst(rands[m,:,j],kmc[kml[m],:]) for m in range(shape[0])])
            gaps[i] = np.mean(np.log(refdisps))-np.log(disp)
        return gaps