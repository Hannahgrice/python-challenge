import csv

# Path to your CSV file
csv_file_path = "budget_data.csv"

# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    # Read the CSV file
    csv_reader = csv.reader(csvfile)
    
    # Iterate through each row
    for row in csv_reader:
        # Process the row
        print(row)
# month variable
total_months = 0 
# in csv file
with open(csv_file_path, newline='') as csvfile:
    # read file 
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    # iterate through rows
    for row in csv_reader:
        total_months += 1

import csv

# Path to your CSV file
csv_file_path = "budget_data.csv"

# Initialize variables
total_months = 0
total_profit_losses = 0
total_changes = 0
previous_profit_loss = None
max_increase = 0
max_increase_date = None
max_decrease = 0
max_decrease_date = None

# Open the CSV file
with open(csv_file_path, newline='') as csvfile:
    # Read the CSV file
    csv_reader = csv.reader(csvfile)
    
    # Skip the header row
    next(csv_reader)
    
    # Read the first row to set initial values
    first_row = next(csv_reader)
    previous_profit_loss = int(first_row[1])
    total_months += 1
    total_profit_losses += previous_profit_loss

    # Iterate through each remaining row
    for row in csv_reader:
        # Increment total months
        total_months += 1
        
        # Extract profit/loss for the current row
        current_profit_loss = int(row[1])
        
        # Add profit/loss for the current row to the total
        total_profit_losses += current_profit_loss
        
        # Calculate change in profit/losses
        change = current_profit_loss - previous_profit_loss
        total_changes += change
        
        # Update maximum increase if applicable
        if change > max_increase:
            max_increase = change
            max_increase_date = row[0]
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = total_changes / (total_months - 1)  # Subtract 1 because there is 1 less change than total months
    
    # Update maximum increase if applicable
if change > max_increase:
        max_increase = change
        max_increase_date = row[0]
    
    # Update maximum decrease if applicable
if change < max_decrease:
        max_decrease = change
        max_decrease_date = row[0]
    
    # Update previous profit/loss for the next iteration
previous_profit_loss = current_profit_loss

# Print results
print("-----------------------")
print("Total number of months:", total_months)
print("Total profit/losses over the entire period:", total_profit_losses)
print("Average change of profit/losses:", average_change)
print("Greatest increase in profits (date and amount):", max_increase_date, "($", max_increase, ")")
print("Greatest decrease in profits (date and amount):", max_decrease_date, "($", max_decrease, ")")