# Initial Set Up
import os
import csv

csvpath = os.path.join('budget_data.csv')

# Setting Variables
tmonth = 0
tnet = 0
aver = 0
gincrease = 0
gincreasemonth = 0
gdecrease = 0
gdecreasemonth = 0

# Setting reading function
with open(csvpath, newline="") as csvfile:

    # Setting reading function with delimiters
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip over the first line --> Headers
    csvheader = next(csvreader)
    row = next(csvreader)
    
