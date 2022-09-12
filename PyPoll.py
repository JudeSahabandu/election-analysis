# The data we need to retrieve

    #Adding dependencies

import os
import csv

    # Assigning variable to load a csv file from a path

file_to_load = os.path.join('Resources','election_results.csv')

    # Assigning variable to save a txt file to a path

file_to_save = os.path.join('Analysis','election_analysis.txt')

    #Open election results to read the file

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Read and print the header row

    headers=next(file_reader)
    print(headers)

#Creating a text file to save and add text

    # Open a txt file to write to (edit using 'w')

open(file_to_save, "w")

with open(file_to_save, "w") as txt_file:
    
    #inputting required txt data

    txt_file.write("Counties In The Election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

