# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
# import CSV
csvpath = os.path.join('Resources', 'election_data.csv')
# define function and have it accept 'election_data' as parameter
def print_candidate_name(election_data):
    candidate_name = str(election_data[2])
    print(candidate_name)
# read election_data
with open (csvpath, newline='') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    # assign value to variables
    
    count = 0
    candidate_name=[]
    candidate_count = 0
    percent = 0
    for Row in csvreader:
    # The total number of votes cast
        count = count + 1

    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    for i in range(0, len(candidate_name)):
        candidate_count = candidate_count + (candidate_name[i] + candidate_name[i+1])
        percent = candidate_count/count
        break




# The winner of the election based on popular vote

# output in terminal
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {count}")
print("-------------------------------------")
print(f'[candidate_name]: {percent:.3f}, {(candidate_count)}')