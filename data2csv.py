import csv

# List of files to combine
file_paths = [
    ".\\Datasets\\image segmentation\\segmentation.data",
    ".\\Datasets\\image segmentation\\segmentation.test"
]  

combined_data = []
header = None  # Store the header row

# Define label mapping (uppercase class labels)
label_mapping = {
    "BRICKFACE": 0,
    "SKY": 1,
    "FOLIAGE": 2,
    "CEMENT": 3,
    "WINDOW": 4,
    "PATH": 5,
    "GRASS": 6
}

for index, file_path in enumerate(file_paths):
    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            # Skip comment lines
            if row and not row[0].startswith(";;;"):
                if header is None:  # Store header from the first file only
                    header = row
                else:
                    # Map class label (first column) to integer
                    if row[0] in label_mapping:
                        row[0] = label_mapping[row[0]]
                        combined_data.append(row)

# Write combined data to a new CSV file
with open("combined_data.csv", mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)  # Write the header from the first file
    writer.writerows(combined_data)  # Write the data rows

print(f"Combined {len(combined_data)} rows into 'combined_data.csv'.")
