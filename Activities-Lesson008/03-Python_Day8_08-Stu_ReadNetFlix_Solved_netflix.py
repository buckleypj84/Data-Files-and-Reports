#Prompt the user for what video they are looking for.
#Search through the netflix_ratings.csv to find the user's video.

#If the CSV contains the user's video then print out the title, 
#   what it is rated and the current user ratings.
#For example "Pup Star is rated G with a rating of 82"

#If the CSV does not contain the user's video then print out a message 
# telling them that their video could not be found.

# Modules
import os
import csv
#get the current working directory
currentDir = os.getcwd()

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

#class video (6/11/19 at 2:12:07) explains details about path/join
# Set path for file
#csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")


#csvpath = os.path.join('c:/TempDir/NetFlix_ratings.csv')
#csvpath = os.path.join('Resources','web_end.csv') --- this is the prefered method
csvpath = "c:/TempDir/testing.csv"
#csvpath = "c:/TempDir/NetFlix_ratings.csv" -- file created error on open function
#                                           -- copied data to Notepad ++ from GitLab 
#                                           -- into Excel, saved as csv  
#                                           -- imported  

# Bonus
# ------------------------------------------
# Set variable to check if we found the video
found = False

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video -- row is 0 based but represents col for this file
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

            # BONUS: Set variable to confirm we have found the video
            found = True

            # BONUS: Stop at first results to avoid duplicates
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
