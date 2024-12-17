# Lamar Logan
# INST126
# Prof. Jackson
# 10/10/2024
  
# Import all of the modules into the code
import os

# Print the current working directory and list all of its contents that are inside of it
print("current directory", os.getcwd())
print("Contents of the directory:", os.listdir())

# This step will ask the user to specfiy the file path
file_path = input("Please enter the file path: ")

# This step is for when there is an error when inputing or typing the wrong file
while True:
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            break
    except FileNotFoundError:
        print("File not found. Please try again.")
        File_path = input("Please enter the file path: ")

# This step is for when the code will ask the user for a word or phrase to count, which is like the first word count assignment
word_or_phrase = input("Please enter the word or two-word phrase you want to count: ").strip()
if len(word_or_phrase.split()) > 2:
    print("Error: Only single words or two-word phrases are allowed.")
    exit()

# Ask the user if they want case sensitivity or not
while True:
    case_sensitive = input("Do you want the search to be case-sensitive? (yes/no): ").lower()
    if case_sensitive not in ["yes","no"]:
        break
    else:
        print("Invalid input. Please enter 'yes or 'no'.") 

if case_sensitive == 'no':
    word_or_phrase == word_or_phrase.lower()
    text = text.lower()

# This step is to perform the word/Phrase count in the specified or selected file
count = text.count(word_or_phrase)

# This last step is used to show the results
result_message = f'The word/phrase "{word_or_phrase}" was found {count} times in the file "{file_path}".'
print(result_message)

with open('wordcount_results.txt', 'w') as result_file:
    result_file.write(result_message)

