import os #changes path to / for windows environment
import csv
path = 'c:/TempDir/web_starter.csv'

title = []
price = []
subscribers = []
nbr_reviews = []
course_len = []

with open(path, newline='',encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])


#Zip all three lists together into tuples
newdata = zip(title, price, subscribers)

#save the output file path
path = "c:/TempDir/web_end.csv"
with open(path, 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(['Name','Price','Subscribers'])
    csvwriter.writerows(newdata)