#Create a Python application that reads the data on Udemy Web Development offerings. 
#Then store the contents of the Title, Price, Subscriber Count, Number of Reviews, and Course Length into Python Lists.
#Then zip these lists together into a single tuple.
#Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your csv.

#Notes:
#Windows user may get an UnicodeDecodeError, to avoid this file pass in encoding="utf8" as an additional parameter when reading in the file.
#As, with many datasets, the file does not include the header line. Use the below as a guide on the columns: "id,title,url,isPaid,price,numSubscribers,numReviews,numPublishedLectures,instructionalLevel,contentInfo,publishedTime"

#Bonus
#Find the percent of subscribers that have also left a review on the course. Include this in your final output.
#Parse the string associated with course length, such that we store it as an integer instead of a string. (i.e. "4 hours" should be converted to 4).

import os
import csv

#udemy_csv = os.path.join("..", "Resources", "web_starter.csv")
udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
#with open(udemy_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])

        # Add amount of reviews
        reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

# Zip lists together
cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
