# Initial functions
import os
import csv

# Set path for the file
csvpath = os.path.join('Resources','election_data.csv')

# Set Variables
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

# Open and read the csv file
with open(csvpath,newline='') as csvfile:

    # Separate using delimiters
    csvreader = csv.reader(csvfile,delimiter=',')

    # Skip over the headers
    csv_header = next(csvfile)

    # Create the For Loop
    for row in csvreader:

        # Count the total number of votes
        total_votes = total_votes + 1

        # Count total number of votes for each candidate
        if (row[2] == "Khan"):
            khan = khan + 1
        elif (row[2] == "Correy"):
            correy = correy + 1
        elif (row[2] == "Li"):
            li = li + 1
        else:
            otooley = otooley + 1

    # Calculate the percentage of votes for each candidate
    pkhan = khan/total_votes
    pcorrey = correy/total_votes
    pli = li/total_votes
    potooley = otooley/total_votes

    # Define the winner using Max function
    winner = max(khan, correy, li, otooley)

    if winner == khan:
        dictator = "Khan rules the World!"
    elif winner == correy:
        dictator = "Correy rules the World!"
    elif winner == li:
        dictator = "Li rules the World!"
    else:
        dictator = "O'Tooley rules the World!"

# Analysis
print(f"Election Results")
print(f"----------------")
print(f"Total Votes = {total_votes}")
print(f"----------------")
print(f"Khan = {pkhan} ({khan})")
print(f"Correy = {pcorrey} ({correy})")
print(f"Li = {pli} ({li})")
print(f"O'Tooley = {potooley} ({otooley})")
print(f"----------------")
print(f"{dictator}")
print(f"----------------")

# Create output file
output_file = os.path.join('election_data_revised.csv')

# Open the output file
with open(output_file, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"Total Votes , {total_votes}\n")
    txtfile.write(f"Khan , {pkhan} ,{khan}\n")
    txtfile.write(f"Correy , {pcorrey}, {correy}\n")
    txtfile.write(f"Li , {pli}, {li}\n")
    txtfile.write(f"O'Tooley , {potooley} ,{otooley}\n")
    txtfile.write(f"----------------\n")
    txtfile.write(f"{dictator}\n")

    
