#imports
from stats import word_counter
from stats import character_counter
from stats import dictionary_sorter
import sys


#functions
def get_books_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_books_text(sys.argv[1])
        words = word_counter(text)
        print(f"Found {words} total words")
        characters = character_counter(text)
        #print(characters)
        sorted_dictionary = dictionary_sorter(characters)

        for entry in sorted_dictionary:
            c = entry['char']
            n = entry['num']
            if c.isalpha():
                print(f"{c}: {n}")
            else:
                pass 

main()