import csv
import math

input_file = '.\\Datasets\\metal\\Dataset_VisContest_Rapid_Alloy_development_v1.txt'
output_file = 'Rapid_Alloy.csv'

with open(input_file, 'r') as txt_file, open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    cnt = 0
    for line in txt_file:
        row = line.split()
        
        if cnt > 0:
            row = [f"{float(item):.8f}" if 'E' in item else item for item in row] # round scientific notations
            row = [0 if item == "nan" else item for item in row] # nan to 0
        
        writer.writerow(row)
        cnt += 1

print(f"File converted successfully! The CSV file is saved as '{output_file}'")
