import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = ".\Datasets\iris\output\iris.bin"
emb_data = np.fromfile(file_path, dtype=np.float32)
emb_data = emb_data.reshape(-1, 2)

data_file = ".\Datasets\iris\iris_data_stored.csv"
data = pd.read_csv(data_file)
labels = data.iloc[:, -1].values
high_d_data = data.iloc[:, :-1].values

from sklearn.manifold import trustworthiness

print(f"{trustworthiness(high_d_data, emb_data, n_neighbors=5):.2f}")