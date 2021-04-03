# -*- coding: UTF-8 -*-

# Import required packages
import csv
import os

# Files to read, and file to output
budget_data = os.path.join("Resources", "budget_data.csv")
financial_analysis = os.path.join("Analysis", "financial_analysis.csv")

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas, grab the header
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Variables for data
    net_total = 0
    months_number = 0
    profit_list = []
    average_change = 0
    current_profit = 0
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""

    # Loop through the data
    for row in csvreader:
        current_profit = int(row[1])
        net_total += current_profit
        months_number += 1
        # Add monthly profits/losses to a list
        profit_list.append(row[1])
        # Find greatest increase/decrease in profits, and their dates
        if current_profit > greatest_increase:
            greatest_increase = current_profit
            greatest_increase_date = row[0]
        if current_profit < greatest_decrease:
            greatest_decrease = current_profit
            greatest_decrease_date = row[0]
    
    # Loop through the list of profits, calculating difference per month
    i = 1
    while i < len(profit_list):
        average_change += int(profit_list[i]) - int(profit_list[i-1])
        i += 1

    # Calculate average change by diving the monthly change by number of months
    average_change = "{:.2f}".format(average_change / (months_number))

    # Summary table
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {months_number}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results as a text file
with open("Analysis\\budget_analysis.txt", "w") as output_file:
    print("Financial Analysis", file=output_file)
    print("---------------------------------", file=output_file)
    print(f"Total Months: {months_number}", file=output_file)
    print(f"Total: ${net_total}", file=output_file)
    print(f"Average Change: ${average_change}", file=output_file)
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=output_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=output_file)
