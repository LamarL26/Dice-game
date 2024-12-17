# Lamar Logan
# INST126
# Prof. Jackson
# 10/17/2024

# The first thing to do in this code is to make sure we import the files that we need
import os
import csv

# This is the second step. Here, you print the working directory and any of the contents inside of the presenty directory
print("Present Directory:", os.getcwd())
print("Content inside of the working directory:", os.listdir())

# You will be asked here to specify the file path of your desire. And if any errors were to occur, a meesage will appear
while True:
    file_path = input("Type the CSV file path you desire: ")
    if os.path.isfile(file_path) and file_path.endswith('.csv'):
        with open(file_path, 'r') as file:
            # Read the CSV file content as a single string for word counting purposes
            reader = csv.reader(file)
            text = ' '.join([row for rows in reader for row in rows])  # Flatten the CSV content into a single string
        break
    else:
        print("This file was not found or is not a CSV file. Make sure what you typed is correct and try again.")

# For the fourth step, you will ask for either a two-word phrase or a word. You can only go up to two words
word_or_phrase = input("Please enter the word or two-word phrase you want to count: ").strip()
if len(word_or_phrase.split()) > 2:
    print("Error: Only single words or two-word phrases are allowed.")
    exit()

# Going back to Word Count 2.0, you will be asked if you would like the search to be case-sensitive or not
while True:
    case_sensitive = input("Do you wish for your desired search to be case-sensitive?  (yes/no): ").lower()
    if case_sensitive in ["yes", "no"]:
        break
    else:
        print("Error, wrong answer was inputted. Try again and either enter 'yes' or 'no'.")

# For here, if the case-sensitive option is not selected, it will convert to a lowercase
if case_sensitive == 'no':
    word_or_phrase = word_or_phrase.lower()
    text = text.lower()

# For this step, the code will perform count for the word or phrase
count = text.count(word_or_phrase)

# For the last result, the code will show the result and it will also save the result to a file.
result_message = f'The desired word/phrase "{word_or_phrase}" was found {count} times in the file "{file_path}".'
print(result_message)

with open('wordcount_results.txt', 'w') as result_file:
    result_file.write(result_message)
