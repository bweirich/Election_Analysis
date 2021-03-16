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

# Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)    

    # Print the header row
    headers = next(file_reader)
    print(headers)
    
# Open file as text file
with open(file_to_save, 'w') as txt_file:
    txt_file.write('Counties in the Election\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\nArapahoe\nDenver\nJefferson')