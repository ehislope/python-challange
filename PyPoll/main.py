# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# import CSV
csvpath = os.path.join('Resources', 'election_data.csv')

# read election_data
with open (csvpath, newline='') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
# set variables for total votes, list of canditates, % votes by candidate, total votes by candidate
    count = 0
    candidates = []
    percent = 0

    for Row in csvreader:
    # The total number of votes cast
        count = count + 1
    # A complete list of candidates who received votes
    

    # The percentage of votes each candidate won

   
    # The total number of votes each candidate won


# The winner of the election based on popular vote