# import the os module
# This will allow us to create file paths across operating systems
import os

# import Module for reading CSV files
import csv

# import CSV
csvpath = os.path.join('Resources', 'election_data.csv')

# read election_data
with open (csvpath, newline='') as csvfile:

 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    # assign value to variables
    votes = 0
    candidate = ["Khan","Correy","Li", "O'Tooley"]
    khan_votes = 0
    khan_percent = 0
    correy_votes = 0
    correy_percent = 0
    li_votes = 0
    li_percent = 0
    otooley_votes = 0
    otooley_percent = 0
    
    for Row in csvreader:
        # The total number of votes cast
            votes = votes + 1
            # count votes per candidate
            candidate.append(str(Row[2]))
    # count votes and calculate % for each candidate, .count found on \
    # https://www.programiz.com/python-programming/methods/list/count
    khan_votes= candidate.count(candidate[0])
    khan_percent = (khan_votes/votes)*100
    correy_votes= candidate.count(candidate[1])
    correy_percent = (correy_votes/votes)*100
    li_votes= candidate.count(candidate[2])
    li_percent = (li_votes/votes)*100
    otooley_votes= candidate.count(candidate[3])
    otooley_percent = (otooley_votes/votes)*100

      
# The winner of the election based on popular vote

# output analysis to text file
output_path = os.path.join("Analysis", "Analysis.txt")
f = open(output_path, 'w')
print("Election Results", file=f)
print("-------------------------------------", file=f)
print(f"Total Votes: {votes}", file=f)
print("-------------------------------------", file=f)
print(f'{candidate[0]}: {khan_percent:.3f}, ({khan_votes})', file=f)
print(f'{candidate[1]}: {correy_percent:.3f}, ({correy_votes})', file=f)
print(f'{candidate[2]}: {li_percent:.3f}, ({li_votes})', file=f)
print(f'{candidate[3]}: {otooley_percent:.3f}, ({otooley_votes})', file=f)
# output in terminal
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {votes}")
print("-------------------------------------")
print(f'{candidate[0]}: {khan_percent:.3f}, ({khan_votes})')
print(f'{candidate[1]}: {correy_percent:.3f}, ({correy_votes})')
print(f'{candidate[2]}: {li_percent:.3f}, ({li_votes})')
print(f'{candidate[3]}: {otooley_percent:.3f}, ({otooley_votes})')