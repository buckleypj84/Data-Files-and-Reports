import os
import csv
csvpath = os.path.join('c:/csvfile/netflix_rating.csv')

title = input("What show or movie are you looking for? ")
with open(csvpath, newline '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=', ')
found = false
csv_header = next(csvreader)
print(f"CSV Header: {csv_header})

for row in csvreader:
    if(row[0] == title):
        print("f ")
        found= true
        break

if not found
        print("I don't know that title")



