from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
def overheads():
    """
    -This function finds the highest overhead category.
    """
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # Skip first line of csv
        next(reader)
        # Store highest overhead and highest category in new variables
        highest_overhead = 0
        highest_category = ""
        # Make for loop
        for row in reader:
            # Define category and overhead
            category = row[0]
            overhead = float(row[1])
            # Use if to check if current overhead is higher than highest overhead
            if overhead > highest_overhead:
                # If current overhead is higer make it the new highest overhead and category
                highest_overhead = overhead
                highest_category = category
        # Print [HIGHEST OVERHEADS] {highest_category}:{highest_overhead}% using f string
        return(f"[HIGHEST OVERHEADS] {highest_category}:{highest_overhead}%")
# Call the overhead function
print(overheads())