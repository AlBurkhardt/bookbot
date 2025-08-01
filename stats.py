def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_characters(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        dictionary: characters and number of appearances.
    """
    character_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if not char.isspace():
            character_count[char] = character_count.get(char, 0) + 1
    
    return character_count

def get_character_count_list(character_count):
    """
    Converts the character count dictionary to a list of dictionaries.
    
    Args:
        character_count (dict): A dictionary with characters and their counts.
        
    Returns:
        list: A list of dictionaries with character and count.
    """
    return [{"char": char, "count": count} for char, count in character_count.items()]

def print_report(path, word_count, character_count_list):
    """
    Prints a report of the word and character counts.
    
    Args:
        path (str): The path to the book file.
        word_count (int): The number of words in the text.
        character_count (dict): A dictionary with characters and their counts.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -----------")
    for dict in character_count_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")