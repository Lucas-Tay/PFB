from pathlib import Path
import csv

# create a file to csv file.
file_path = Path.cwd() / "csv_reports" / "Profit and Loss.csv"

# def profit and loss function
def profitloss():
    """
    -This function helps compute the
    difference in the net profit column if net profit on
    the current day is lower than the previous day.

    """
    with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # Skip first line of csv
        next(reader)
        # Create variable to store previous net profit
        previous_net_profit = 0
        # Make a for loop
        for row in reader:
            # Define what is current net profit
            current_net_profit = float(row[4])
            # Use if and else and check if previous net profit is more than current net profit
            if previous_net_profit > current_net_profit:
                # Find the profit loss if previous net profit is higher than current net profit
                profit_loss = previous_net_profit - current_net_profit
                # Print [PROFIT DEFICIT] DAY:{row[0]}, AMOUNT:USD{profit_loss} using f string
                return(f"[PROFIT DEFICIT] DAY:{row[0]}, AMOUNT:USD{profit_loss}")
            # Store current net profit as previous net profit
            previous_net_profit = current_net_profit
        # Return [NET PROFIT SURPLUS] if for loop ends without profit deficit
        return(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

# Call profitloss function
print(profitloss())