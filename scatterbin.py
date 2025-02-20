import numpy as np
import matplotlib.pyplot as plt

# Load the binary file
file_path = ".\Datasets\image segmentation\segemtation-base.bin"  # Update this with the correct path if needed
data = np.fromfile(file_path, dtype=np.float32)  # Load as 32-bit float

# Reshape into (150, 2) since we have 150 points in 2D
data = data.reshape(-1, 2)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c='blue', alpha=0.6, edgecolors='k')
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.title("t-SNE Embedding of Iris Dataset")
plt.grid(True)
plt.show()

# TODO: add some metric to evaluate the embedding