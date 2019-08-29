# Initial Set Up
import os
import csv

csvpath = os.path.join('budget_data.csv')

# Setting Variables
tmonth = 0
tnet = 0
average = 0
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

    # Calculating initial variables
    previousrow = int(row[1])
    tmonth = tmonth + 1
    tnet = tnet + int(row[1])
    gincrease = int(row[1])
    gincreasemonth = str(row[0])

    for row in csvreader:
    
        # Begin reading each row
        revenuechange = int(row[1]) - previousrow
        nextmonth = []
        nextmonth.append(revenuechange)
        previousrow = int(row[1])
        monthcount = []
        monthcount.append(row[0])

       # Calculate total number of months
        tmonth = tmonth + 1
       # Calculate the net of Profit/Losses
        tnet = tnet + int(row[1])
       
       #Set the greatest increase and decrease
    if int(row[1]) > gincrease:
        gincrease = int(row[1])
        gincreasemonth = int(row[0])

    if int(row[1]) < gdecrease:
        gdecrease = int(row[1])
        gdecreasemonth = int(row[0])
            
    # Find the average of monthly revenue changes
    average = sum(nextmonth)/len(nextmonth)

    revenuemax = max(nextmonth)
    revenuemin = min(nextmonth)

# Analysis
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months = tmonth")
print(f"Average Change = average")
print(f"Greatest Increase in Profits = gincreasemonth revenuemax")
print(f"Greates Decrease in Profits = gdecreasemonth revenuemin")

    
                         
    
    

    
