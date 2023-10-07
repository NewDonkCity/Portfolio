import csv

# Open the CSV file for reading
with open('DATA475_lab_rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    
    # Skip the first row
    next(reader)
    
    # Initialize variables
    total_area = 0
    count = 0
    areas = []
    
    # Loop through the rows in the CSV file
    for row in reader:
        # Calculate the area of the rectangle
        area = float(row[1]) * float(row[2])
        
        # Add the area to the list of areas
        areas.append(area)
        
        # Add the area to the total area
        total_area += area
        
        # Increment the count of rectangles
        count += 1
    
    # Calculate the average, maximum and minimum area
    average_area = total_area / count
    max_area = max(areas)
    min_area = min(areas)
    
    # Print out the results
    print(f'Total count of rectangles: {count}')
    print(f'Total area of rectangles: {total_area}')
    print(f'Average area of rectangles: {average_area}')
    print(f'Maximum area of rectangles: {max_area}')
    print(f'Minimum area of rectangles: {min_area}')
    
    # Open the summary CSV file for writing
    with open('summary.csv', 'w', newline="") as summary_file:
        writer = csv.writer(summary_file)
        
        # Write the results to the summary CSV file
        headers = [
            'Total count of rectangles',
            'Total area of rectangles',
            'Average area of rectangles',
            'Maximum area of rectangles',
            'Minimum area of rectangles',
        ]
        values = [
            count,
            total_area,
            average_area,
            max_area,
            min_area,
        ]
        writer.writerow(headers)
        writer.writerow(values)
