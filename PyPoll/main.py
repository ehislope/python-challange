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
   
    # assign value to variables
    votes = 0
    candidate = ["Khan","Correy","Li", "O'Tooley"]
    kahn_votes = 0
    kahn_percent = 0
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
    khan_votes= candidate.count(candidate[0])
    khan_percent = kahn_votes/votes
    correy_votes= candidate.count(candidate[1])
    correy_percent = correy_votes/votes
    li_votes= candidate.count(candidate[2])
    li_percent = li_votes/votes
    otooley_votes= candidate.count(candidate[3])
    otooley_percent = otooley_votes/votes

        # A complete list of candidates who received votes
            # candidate_names = ["Khan", "Correy", "Li", "O'Tooley"]
            # vote_count_khan= candidate_names.count("Khan") + 1

    
    
# The winner of the election based on popular vote
# output in terminal
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {votes}")
print("-------------------------------------")
print(f'{candidate[0]}: {kahn_percent:.3f}, ({kahn_votes})')
print(f'{candidate[1]}: {correy_percent:.3f}, ({correy_votes})')
print(f'{candidate[2]}: {li_percent:.3f}, ({li_votes})')
print(f'{candidate[3]}: {otooley_percent:.3f}, ({otooley_votes})')