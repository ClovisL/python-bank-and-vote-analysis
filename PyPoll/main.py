# -*- coding: UTF-8 -*-

# Import required packages
import csv
import os

# Files to read
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")    #Delete PyPoll part when done testing

# Read in the CSV file
with open(election_data, 'r') as csvfile:
    # Split the data on commas, grab the header
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Variables for data
    total_votes = 0
    candidates = []
    candidate_votes = 0
    candidate_percentage = 0

    # Loop through the file
    for row in csvreader:
        # Counts each row as a vote
        total_votes += 1
        # Adds each candidate name into a long list
        candidates.append(row[2])

    # Begins printing out the results
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")

    # Gets each unique candidate name into a set
    unique_names = set(candidates)
    # Loops through and counts how many votes each candidate received
    for candidate in unique_names:
        candidate_votes = candidates.count(candidate)
        candidate_percentage = "{:.2f}".format(candidate_votes / total_votes * 100)
        print(f"{candidate}: {candidate_percentage}% ({candidate_votes})")

    print("------------------------")
    print(f"Winner: ")
    print("------------------------")