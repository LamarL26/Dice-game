# Word Count 1.0

# Step 1: Import necessary libraries
# Step 2: Print the current working directory and the list files
# Step 3: Get user input for the file and the word to count
# Step 4: Read the file and count occurrences of the word
# Step 5: Print the result to the terminal
# Step 6: Write the result to a text file

import os

# Print current working directory
print("current working directory:", os.getcwd())

# List files in the directory
print("Files in the directory:", os.getchwd())
print(os.listdir())

# Get the filename from the user
filename = input("Enter the filename (including .txt): ")

# Get the word to count
word_to_count = input("Enter the word to count: ")

try: 
    with open(filename, 'r') as file:
        text = file.read()
        # count occureneces of the word
        word_count = text.lower().split().count(word_to_count.lower())
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
    exit()

# Print the result
result_message = f"The word '{word_to_count}' was found {word_count} times in the file: {filename}"
print(result_message)

# Write the result to a file
with open("wordcount_results.txt", 'w') as result_file:
    result_file.write(result_message)