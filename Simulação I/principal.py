import pandas as pd

if __name__ == "__main__":
    usuarios_csv = pd.read_csv("dataset-filtrado.csv")
    print(usuarios_csv)