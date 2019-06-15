# Read the resume file as text using the with statement.
# Create a list containing all words in the resume.

# Convert each word to lowercase to normalize the data.

# Use split to remove and trailing punctuation so only words remain.
# Create a set of unique words from the resume using set().

# Use set operations to filter out all remaining punctuation from the set of words.
# Create a set from string.punctuation to use in the difference operation.

# Use the cleaned set (no punctuation) to find all of the words from the resume that match the required skills.
# Use the cleaned set (no punctuation) to find all of the words that match the desired skills.

# Bonuses
# Count the number of occurrences for each word in the resume and print the top 10 occuring words in the resume.
# Use a dictionary data structure to hold the counts for each word.
# Make sure to remove punctuation and stop words

#Hints
#Carefully consider when to use a Dictionary data structure vs. a Set data structure 
#when operating on Unique and Non-unique elements.

# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import csv
import string

# Counter is used for the bonus solution
from collections import Counter

# Paths
resume_path = os.path.join("Resources", 'resume.md')
#csvpath = os.path.join("Resources", "cereal_cleaner.csv")
# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}


def load_file(resume_path):
    """Helper function to read a file and return the data."""
    with open(resume_path, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()


# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])
print(resume)

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)

# Calculate the Required Skills Match using Set Intersection
print(resume & REQUIRED_SKILLS)

# Calculate the Desired Skills Match using Set Intersection
print(resume & DESIRED_SKILLS)

# Bonus: Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(word_count)

# Bonus using collections.Counter
word_counter = Counter(word_list)
print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")

# Clean Punctuation
_word_count = [word for word in word_count if word not in string.punctuation]

# Clean Stop Words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]
_word_count = [word for word in _word_count if word not in stop_words]

# Sort words by count and print the top 10
sorted_words = []
for word in sorted(_word_count, key=word_count.get, reverse=True)[:10]:
    print(f"Token: {word:20} Count: {word_count[word]}")
