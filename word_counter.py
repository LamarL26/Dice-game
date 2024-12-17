# word_counter.py

def count_occurrences(word, file_path, case_sensitive=True):
    """
    Count occurrences of a word in a given file.
    Args:
        word (str): The word to count.
        file_path (str): The path to the file.
        case_sensitive (bool): Whether the count should be case-sensitive.
    Returns:
        int: The number of occurrences.
    """
    with open(file_path, 'r') as f:
        text = f.read()
        if not case_sensitive:
            word = word.lower()
            text = text.lower()
        return text.count(word)
