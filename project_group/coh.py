from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd()/"project_group"/"csv_reports"/"Cash on Hand.csv"
# Define new coh function
def coh():
    """
    -The function computes the
    difference in Cash-on-Hand if the current day is
    lower than the previous day.
    """
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            # Skip first line of csv
            next(reader)
            # Create variable to store previous cash on hand
            output = ""
            previous_coh = 0
            current_coh = 0
            # Make a for loop
            for row in reader:
                # Define what is current cash on hand
                current_coh = float(row[1])
                # Use if and else and check if previous cash on hand is more than current cash on hand
                if current_coh < previous_coh:
                    # Find the cash on hand loss if previous cash on hand is higher than current cash on hand
                    coh_loss = previous_coh - current_coh
                    # Print [CASH DEFICIT] DAY:{row[0]}, AMOUNT:USD{coh_loss} using f string
                    output += (f"[CASH DEFICIT] DAY:{row[0]}, AMOUNT:USD{coh_loss}\n")
                # Update the previous_coh for next iteration
                previous_coh = current_coh
    # Call the coh function
    return output

print(coh())