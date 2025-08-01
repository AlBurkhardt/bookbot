from stats import count_words 
from stats import count_characters 
from stats import get_character_count_list
from stats import print_report
import sys
def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_content = get_book_text(filepath)
    
    if book_content:     
        count = count_words(book_content)
        """print(f"{count} words found in the document")"""
        char_count = count_characters(book_content)
        character_count_list = get_character_count_list(char_count)
        character_count_list.sort(key=lambda x: x["count"], reverse=True)
        print_report(filepath, count, character_count_list)
        """print(char_count)"""

main()