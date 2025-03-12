import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load embedding data
file_path = ".\\Datasets\\image segmentation\\output\\row_class_avg_rescale_100_300.bin"
emb_data = np.fromfile(file_path, dtype=np.float32).reshape(-1, 2)

# Load labels
data_file = ".\\Datasets\\image segmentation\\combined_data.csv"
data = pd.read_csv(data_file)
labels = data.iloc[:, 0].values

# Create scatter plot
plt.figure(figsize=(8, 6))
scatter = plt.scatter(emb_data[:, 0], emb_data[:, 1], c=labels, cmap='tab10', s=8, alpha=0.75)

# Add colorbar
plt.colorbar(label="Class Label")

# Title and labels
plt.title("2D Embedding of Segmentation Data")
plt.xlabel("Embedding Dimension 1")
plt.ylabel("Embedding Dimension 2")

# Save the plot as an image
save_path = ".\\Datasets\\image segmentation\\output\\row_class_avg_rescale_100_300.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight')

# Show plot (optional)
plt.show()
