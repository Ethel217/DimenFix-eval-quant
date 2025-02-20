import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from sklearn.manifold import trustworthiness
from clustme import ClustMe

# Metric functions
def neighborhood_hit(embedding, labels, k=10):
    from sklearn.neighbors import NearestNeighbors
    nbrs = NearestNeighbors(n_neighbors=k + 1).fit(embedding)
    _, indices = nbrs.kneighbors(embedding)
    hits = sum(np.mean(labels[indices[:, 1:]] == labels[:, None], axis=1))
    return hits / len(labels)

def continuity(high_d_data, embedding, k=10):
    dist_hd = pairwise_distances(high_d_data)
    dist_ld = pairwise_distances(embedding)
    knn_hd = np.argsort(dist_hd, axis=1)[:, 1:k + 1]
    knn_ld = np.argsort(dist_ld, axis=1)[:, 1:k + 1]
    continuity_score = np.mean([len(np.intersect1d(knn_hd[i], knn_ld[i])) / k for i in range(len(high_d_data))])
    return continuity_score

def distance_consistency(high_d_data, embedding):
    dist_hd = pairwise_distances(high_d_data)
    dist_ld = pairwise_distances(embedding)
    return np.corrcoef(dist_hd.flatten(), dist_ld.flatten())[0, 1]

def projection_precision_score(high_d_data, embedding):
    dist_hd = pairwise_distances(high_d_data)
    dist_ld = pairwise_distances(embedding)
    knn_hd = np.argsort(dist_hd, axis=1)[:, 1:6]
    knn_ld = np.argsort(dist_ld, axis=1)[:, 1:6]
    precision = np.mean([len(np.intersect1d(knn_hd[i], knn_ld[i])) / 5 for i in range(len(high_d_data))])
    return precision

def average_local_error(high_d_data, embedding):
    dist_hd = pairwise_distances(high_d_data)
    dist_ld = pairwise_distances(embedding)
    local_error = np.mean(np.abs(dist_hd - dist_ld))
    return local_error

def clumpy_agnostic(embedding):
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(embedding.T)
    return np.std(kde(embedding.T))

def average_same_class_neighbors(embedding, labels, k=10):
    from sklearn.neighbors import NearestNeighbors
    nbrs = NearestNeighbors(n_neighbors=k + 1).fit(embedding)
    _, indices = nbrs.kneighbors(embedding)
    same_class_proportion = np.mean([np.mean(labels[indices[i, 1:]] == labels[i]) for i in range(len(labels))])
    return same_class_proportion

# Main script
def main(embedding_file, data_file):
    # file_path = ".\\Datasets\\iris\\output\\iris.bin"
    embedding = np.fromfile(embedding_file, dtype=np.float32)
    embedding = embedding.reshape(-1, 2)
    data = pd.read_csv(data_file)
    labels = data.iloc[:, -1].values
    high_d_data = data.iloc[:, :-1].values

    metrics = {
        "Trustworthiness": trustworthiness(high_d_data, embedding),
        "Continuity": continuity(high_d_data, embedding),
        "Neighborhood Hit": neighborhood_hit(embedding, labels),
        "Distance Consistency": distance_consistency(high_d_data, embedding),
        "Projection Precision Score": projection_precision_score(high_d_data, embedding),
        "Average Local Error": average_local_error(high_d_data, embedding),
        "Average Same-Class Neighbors": average_same_class_neighbors(embedding, labels),
        "Clumpy Agnostic": clumpy_agnostic(embedding)
    }

    try:
        cm = ClustMe()
        cm.fit(embedding)
        metrics["ClustMe"] = cm.clustme_score
    except Exception as e:
        metrics["ClustMe"] = f"Error: {str(e)}"

    print("--- Metrics ---")
    for key, value in metrics.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python embedding_metrics.py <embedding.bin> <data.csv>")
    else:
        main(sys.argv[1], sys.argv[2])
