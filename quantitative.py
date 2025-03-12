import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from sklearn.neighbors import NearestNeighbors

# assuming embedding is 2d
# assuming original data last col is numeric label

# load iris
# file_path = ".\\Datasets\\iris\\output\\base-iris.bin"
# emb_data = np.fromfile(file_path, dtype=np.float32)
# emb_data = emb_data.reshape(-1, 2)

# data_file = ".\\Datasets\\iris\\iris_data_stored.csv"
# data = pd.read_csv(data_file)
# labels = data.iloc[:, -1].values
# high_d_data = data.iloc[:, :-1].values

# load segmentation
# file_path = ".\\Datasets\\image segmentation\\output\\row_class_avg_rescale_100_300.bin"
# emb_data = np.fromfile(file_path, dtype=np.float32)
# emb_data = emb_data.reshape(-1, 2)

# data_file = ".\\Datasets\\image segmentation\\combined_data.csv"
# data = pd.read_csv(data_file)
# labels = data.iloc[:, 0].values
# high_d_data = data.iloc[:, 1:].values

# load cells
file_path = ".\\Datasets\\Cells\\output\\testrandom.bin"
emb_data = np.fromfile(file_path, dtype=np.float32)
emb_data = emb_data.reshape(-1, 2)

data_file = ".\\Datasets\\Cells\\input\\smFISH_clean_ori.bin"
# data = pd.read_csv(data_file)
# labels = data.iloc[:, 0].values
high_d_data = np.fromfile(data_file, dtype=np.float32)
high_d_data = high_d_data.reshape(-1, 627)

from sklearn.manifold import trustworthiness

print(f"trustworthiness: {trustworthiness(high_d_data, emb_data, n_neighbors=5):.4f}")

from scipy.spatial import distance_matrix
from scipy.stats import spearmanr

def compute_continuity(X_high, X_low, k=10):
    n = X_high.shape[0]

    # Use NearestNeighbors to find k-NN indices
    knn_high = NearestNeighbors(n_neighbors=k+1, algorithm='auto').fit(X_high).kneighbors(X_high, return_distance=False)[:, 1:]
    knn_low = NearestNeighbors(n_neighbors=k+1, algorithm='auto').fit(X_low).kneighbors(X_low, return_distance=False)[:, 1:]

    # Compute continuity score
    intersection_counts = np.array([len(set(knn_high[i]) & set(knn_low[i])) for i in range(n)])
    
    return np.mean(intersection_counts / k)

def outside_continuity(X_high, X_low, labels, k=10):
    n = X_high.shape[0]
    dist_high = distance_matrix(X_high, X_high)
    dist_low = distance_matrix(X_low, X_low)

    nn_high_all = np.argsort(dist_high, axis=1)
    nn_low_all = np.argsort(dist_low, axis=1)

    knn_high = np.full((n, k), -1, dtype=int)
    knn_low = np.full((n, k), -1, dtype=int)

    for i in range(n):
        count = 0
        j = 1
        while count < k and j < n:
            if labels[nn_high_all[i, j]] != labels[i]:  # Different class
                knn_high[i, count] = nn_high_all[i, j]
                count += 1
            j += 1

        count = 0
        j = 1
        while count < k and j < n:
            if labels[nn_low_all[i, j]] != labels[i]:  # Different class
                knn_low[i, count] = nn_low_all[i, j]
                count += 1
            j += 1

    # Compute continuity score
    continuity_sum = 0
    for i in range(n):
        intersection = len(set(knn_high[i]) & set(knn_low[i]))
        continuity_sum += intersection / k  # Normalize by k

    continuity_score = continuity_sum / n  # Normalize by number of points
    return continuity_score



continuity_score = compute_continuity(high_d_data, emb_data)

print(f"Continuity Score: {continuity_score:.4f}")

# continuity_score_exc = outside_continuity(high_d_data, emb_data, labels)

# print(f"Continuity Score Excluding Same Class: {continuity_score_exc:.4f}")

from snc.snc import SNC

print("Calculate SnC: ")

parameter = { "k": 'sqrt', "alpha": 0.1 }

metrics = SNC(
  raw=high_d_data, 
  emb=emb_data, 
  iteration=300, 
  dist_parameter = parameter
)
metrics.fit()
print(metrics.steadiness(), metrics.cohesiveness())


# measure label T&C

# import sys
# sys.path.append("../ltnc/src")

# from ltnc import ltnc
# label_tnc = ltnc.LabelTNC(high_d_data, emb_data, labels, cvm="btw_ch")

# # Run the algorithm and get the results
# results = label_tnc.run()

# # Access the Label-Trustworthiness (LT) and Label-Continuity (LC) scores
# lt_score = results["lt"]
# lc_score = results["lc"]

# print("Label-Trustworthiness (LT):", lt_score)
# print("Label-Continuity (LC):", lc_score)