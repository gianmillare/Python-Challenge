# Initial Set Up
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# Setting Variables
nextmonth = []
monthcount = []
tmonth = 0
tnet = 0
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

    # Setting initial variables
    previousrow = int(row[1])
    tmonth = tmonth + 1
    tnet = tnet + int(row[1])
    gincrease = int(row[1])
    gincreasemonth = row[0]
    gdecrease = int(row[1])
    gdecreasemonth = row[0]

    for row in csvreader:

        # Calculate total number of months
        tmonth = tmonth + 1
        # Calculate the net of Profit/Losses
        tnet = tnet + int(row[1])
        
        # Begin reading each row
        revenuechange = int(row[1]) - previousrow
        nextmonth.append(revenuechange)
        previousrow = int(row[1])
        monthcount.append(row[0])
       
       #Set the greatest increase and decrease
        if int(row[1]) > gincrease:
            gincrease = int(row[1])
            gincreasemonth = row[0]

        if int(row[1]) < gdecrease:
            gdecrease = int(row[1])
            gdecreasemonth = row[0]
            
    # Find the average of monthly revenue changes
    average = sum(nextmonth)/len(nextmonth)

    revenuemax = max(nextmonth)
    revenuemin = min(nextmonth)

# Analysis
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months = {tmonth}")
print(f"Total = ${tnet}")
print(f"Average Change = ${average}")
print(f"Greatest Increase in Profits = {gincreasemonth} (${revenuemax})")
print(f"Greatest Decrease in Profits = {gdecreasemonth} (${revenuemin})")

    
                         
    
    

    
