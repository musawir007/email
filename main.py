import csv
while True:
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ]
    
    # Specify the filename
    filename = 'people.csv'
    
    # Write data to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
