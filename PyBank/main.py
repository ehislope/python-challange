# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# import CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

# read budget_data
with open (csvpath, newline='') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# print(csvreader)
    count = 0
    net = 0
    profit_losses = []
    sum_changes = 0
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for Row in csvreader:
        # count number of months
        count = count + 1
        # total net profit/losses
        net = net + int(Row[1])
        profit_losses.append(int(Row[1]))
        # figure out the month over month profit/loss and avererage
    for i in range(0, len(profit_losses)):
        # profit_losses[i+1] - profit_losses[i]
        sum_changes = sum_changes + profit_losses[i+1] - profit_losses[i]
        Average = sum_changes/count
        break
        # find greatest monthly profit over time

        # find greasted decrease in losses over time
# output analysis to .txt
output_path = os.path.join("Analysis", "Analysis.txt")
f = open(output_path, 'w')
print("Financial Analysis", file=f)
print("-------------------------------------", file=f)
print(f"Total Months: {count}", file=f)
print(f"Total:{net}", file=f)
print (f"Average Change: {Average:.2f}", file=f)


