import csv

input_data = []
name = "iris"

# Define label mapping
label_mapping = {
    "Iris-setosa": 0,
    "Iris-versicolor": 1,
    "Iris-virginica": 2
}

with open(f'.\\Datasets\\{name}\\{name}.data', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if row:  # Ensure row is not empty
            row[-1] = label_mapping[row[-1]]  # Map the last column (class label) to an integer
            input_data.append(row)

num_instances = len(input_data)
print(f"Total number of instances: {num_instances}")

# Define the header
header = ["sepal length", "sepal width", "petal length", "petal width", "class"]

# Save the processed data
with open(f'.\\Datasets\\{name}\\{name}_data_stored.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)  # Write the header row
    writer.writerows(input_data)  # Write the dataset rows

print("Processed dataset saved successfully!")