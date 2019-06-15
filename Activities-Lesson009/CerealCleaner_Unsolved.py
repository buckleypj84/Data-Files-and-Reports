import os
import csv

#get the current working directory
currentDir = os.getcwd()
csvpath = os.path.join("Resources", "cereal_cleaner.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    #csv_header = next(csvfile)
    #print(f'"Header: {csv_header}")

    # Loop through list -- row is 0 based but represents col for this file
    for row in csvreader:
       #convert string to float and compare to grams of fiber
        if float(row[7])>=5:
            print(row)

