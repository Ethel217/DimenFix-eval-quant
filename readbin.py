import csv
import numpy as np
from sklearn import preprocessing
from sklearn.datasets import fetch_openml

# Load MNIST dataset
mnist = fetch_openml('mnist_784', version=1, data_home=".\\scikit_learn_data")
X = mnist.data.to_numpy()

# Select 1000 random samples
# sample_indices = np.random.choice(X.shape[0], size=1000, replace=False)
# X = X[sample_indices]

# Scale the data
X = preprocessing.MinMaxScaler().fit_transform(X)

# Extract labels and scale them
label = mnist.target.to_numpy().astype(int)
# label = label[sample_indices].astype(int)

# Combine X and label into one array for saving
data_with_labels = np.hstack((X, label.reshape(-1, 1)))

# Save the data to a CSV file
with open('mnist_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header (optional)
    header = [f'pixel_{i}' for i in range(X.shape[1])] + ['label']
    writer.writerow(header)
    
    # Write the data rows
    writer.writerows(data_with_labels)
    
print("MNIST data has been stored in 'mnist_data.csv'")

np.savetxt('mnist_labels.txt', label, fmt='%d')

print("MNIST labels have been stored in 'mnist_labels.txt'")
