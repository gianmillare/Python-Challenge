# Initial Set-Up
import os
import csv

# Create the path to file
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip over the first line --> Headers
    csvheader = next(csvreader)
    row = next(csvreader)

    # Setting Variables
    tmonth = 0
    tnet = 0
    gincrease = 0
    gincreasemonth = 0
    gdecrease = 0
    gdecreasemonth = 0
    
    previousrow = int(row[1])
    tmonth = tmonth + 1
    tnet = tnet + int(row[1])
    gincrease = int(row[1])
    gincreasemonth = row[0]
    gdecrease = int(row[1])
    gdecreasemonth = row[0]

    nextmonth = []
    monthcount = []

    # Begin the For Loop
    for row in csvreader:
        tmonth = tmonth + 1
        tnet = tnet + int(row[1])

        revenuechange = int(row[1]) - previousrow
        nextmonth.append(revenuechange)
        previousrow = int(row[1])
        monthcount.append(row[0])

       # Finding the greatest increase and decrease
        if int(row[1]) > gincrease:
            gincrease = int(row[1])
            gincreasemonth = row[0]
        if int(row[1]) < gdecrease:
            gdecrease = int(row[1])
            gdecreasemonth = row[0]

        # Finding the Average, Max, and Min
        average = sum(nextmonth)/len(nextmonth)
        roundedaverage = round(average, 2)
        revenuemax = max(nextmonth)
        revenuemin = min(nextmonth)

    # Print the Analysis
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total Months = {tmonth}")
    print(f"Total = ${tnet}.00")
    print(f"Average Change = ${roundedaverage}")
    print(f"Greatest Increase in Profits = {gincreasemonth} (${revenuemax}.00)")
    print(f"Greatest Decrease in Profits = {gdecreasemonth} (${revenuemin}.00)")

    # Write New Text File
    output_file = os.path.join('Analysis.csv')

    with open(output_file, 'w') as txtfile:
    
        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"------------------\n")
        txtfile.write(f"Total Months ,{tmonth}\n")
        txtfile.write(f"Total ,${tnet}\n")
        txtfile.write(f"Average Change ,${average}\n")
        txtfile.write(f"Greatest Increase in Profits , {gincreasemonth} (${revenuemax})\n")
        txtfile.write(f"Greatest Decrease in Profits , {gdecreasemonth} (${revenuemin})\n")    
