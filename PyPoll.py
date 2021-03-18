# The data we need to retrieve.
# 1) The total number of votes cast
# 2) A complete list of candidates who received votes
# 3) The percentgae of votes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote

#import modules
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize total vote counter
total_votes = 0

# Initialize candidate list
candidate_options = []

# Initalize dictionary for candidate votes
candidate_votes = {}

# Winning candidate tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)    

    # Print the header row
    headers = next(file_reader)
    
    # Print each row in csv file
    for row in file_reader:
        # add to total vote count
        total_votes += 1
        # find candidate name for each row
        candidate_name = row[2]
        # add candidate name to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # begin tracking votes for candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Open file as text file
with open(file_to_save, 'w') as txt_file:
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes: ,}\n"
    f"-------------------------\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    # Calculate percentage of votes for candidates
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = votes / total_votes * 100
        candidate_results = (f'{candidate}: {vote_percentage: .1f}% ({votes:,})\n')
        print(candidate_results)
        # save candidate results to file
        txt_file.write(candidate_results)
    
        # Find winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    
    # Print winning information
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )
    print(winning_candidate_summary)
    # Save winning summary
    txt_file.write(winning_candidate_summary)

