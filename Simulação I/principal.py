'''from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from yellowbrick.cluster import KElbowVisualizer
df = pd.read_csv("../matriz-adj.csv")
df = df.drop(columns='Unnamed: 0')
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(self.dataset)
visualizer.show()'''

x = True

a = {1: 'a'}
print(a[1])