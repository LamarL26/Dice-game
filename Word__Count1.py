# Word Count 1.0 Assignment 
# Lamar Logan
# 10/2/2024
# INST126
# Prof. Jackson

# To start, I will import the libraries
import os

# For this part, I will print out the directory that is currently working
print("current working directory:", os.getcwd())

# Here, I will list the files that are inside of the directory
print("Files in the directory:", os.listdir)

# In this step, I will make the code so I can get the filename directly from the user, which would include the "txt" files
filename = input("Enter the filename (including .txt): ")


word_to_count = input("Enter the word to count: ")

# In this step, I will try to open up the file, as well as count occurrences of the word
try: 
    with open(filename, 'r') as file:
        text = file.read()
        # For right here, it will count occureneces of the word
        word_count = text.lower().split().count(word_to_count.lower())
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
    exit()

# For here, it will print the result
result_message = f"The word '{word_to_count}' was found {word_count} times in the file: {filename}"
print(result_message)

# Lastly, I will write the result of the file here to finish off my code
with open("wordcount_results.txt", 'w') as result_file:
    result_file.write(result_message)