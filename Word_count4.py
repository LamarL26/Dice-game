# Lamar Logan
# INST126
# Prof. Jackson
# 10/30/2024

import os
import sys
import csv
from word_counter import count_occurrences

def count_word_occurrences(text, word_or_phrase, case_sensitive):
    """
    Counts how often a specific word or phrase appears in the provided text.
    Adjusts for case sensitivity based on user preference.
    """
    # Make both the text and search term lowercase if case-sensitive search is disabled
    if not case_sensitive:
        text = text.lower()
        word_or_phrase = word_or_phrase.lower()
    return text.count(word_or_phrase)  # Return the count of the word/phrase in the text

def main():
    # Show the present directory and its files to help the user locate the file they want
    print("Present Directory:", os.getcwd())
    print("Contents inside of the directory:", os.listdir())

    # Check if the program was given command-line arguments for file path, word, and case sensitivity
    if len(sys.argv) > 1:
        file_path = sys.argv[1]  # First argument: path to the file

        # Make sure a word or phrase to search for is provided
        if len(sys.argv) > 2:
            word_or_phrase = sys.argv[2].strip()
        else:
            print("Error: Please provide a word or two-word phrase.")
            exit()

        # Get case sensitivity preference from arguments or prompt the user
        case_sensitive = (sys.argv[3].lower() == 'yes') if len(sys.argv) > 3 else input("Case-sensitive? (yes/no): ").strip().lower() == 'yes'
    else:
        # If no command-line arguments, ask the user for inputs interactively
        file_path = input("Type the file path you desire: ")
        word_or_phrase = input("Enter the word or two-word phrase you want to count: ").strip()
        case_sensitive = input("Do you wish for your desired search to be case-sensitive? (yes/no): ").lower() == 'yes'

    # Limit the search term to a single word or a two-word phrase to keep the results specific and manageable
    if len(word_or_phrase.split()) > 2:
        print("Error: Only single words or two-word phrases are allowed.")
        exit()

    # Allow both .csv and .txt files to be used
    while True:
        if os.path.isfile(file_path) and (file_path.endswith('.csv') or file_path.endswith('.txt')):
            with open(file_path, 'r') as file:
                # If it's a .csv, read it row by row and combine all cells into a single string
                if file_path.endswith('.csv'):
                    reader = csv.reader(file)
                    text = ' '.join([cell for row in reader for cell in row])
                else:
                    # If it's a .txt, read the whole file at once
                    text = file.read()
            break
        else:
            print("File not found or is not a CSV or TXT file.")
            file_path = input("Please enter a valid CSV or TXT file path: ")

    # Count how many times the specified word or phrase appears in the file
    count = count_word_occurrences(text, word_or_phrase, case_sensitive)

    # Display and save the result
    result_message = f'The word/phrase "{word_or_phrase}" was found {count} times in the file "{file_path}".'
    print(result_message)

    # Write the results to a file so the user has a record of the search results
    with open('wordcount_results.txt', 'w') as result_file:
        result_file.write(result_message)

if __name__ == "__main__":
    # Check if enough command-line arguments are provided, otherwise run the program normally
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        print("Error: Not enough command-line arguments. You need to provide the file path, a word or phrase, and (optionally) case sensitivity (yes/no).")
    else:
        main()  # Run the main function when done
