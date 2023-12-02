import csv

data = [
    [0.5014, 0.6827, 0.7547, 0.6521, 0.8247, 0.6315, 0.7386, 0.8079, 0.6826, 0.8202],
    [0.2691, 0.6713, 0.7487, 0.6682, 0.8327, 0.6237, 0.7460, 0.8107, 0.6677, 0.8100],
    [0.4850, 0.6759, 0.7473, 0.6681, 0.8288, 0.6167, 0.7451, 0.8127, 0.6251, 0.7826],
    [0.5180, 0.6867, 0.7554, 0.6447, 0.8196, 0.5872, 0.7493, 0.8105, 0.7220, 0.8467]
]

# Specify the file path
csv_file_path = 'output.csv'

# Writing to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV file created: {csv_file_path}')
