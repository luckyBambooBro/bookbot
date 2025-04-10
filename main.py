import sys
from stats import get_num_words, character_count, sort_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

directory_path = sys.argv[1]

def get_book_text(filepath):
    #print no of words in book then store it in a total_words
    with open(filepath, "r") as f:
        file_contents = f.read()
    total_words = get_num_words(file_contents)


    #print the character count
    characters_to_print = character_count(file_contents) #characters_to_print is a dictionary
    for k, v in characters_to_print.items():
        print(f"'{k}': {v}")
    sorted_list = sort_list(characters_to_print)
    
    print(f'''============ BOOKBOT ============
Analyzing book found at books/{filepath}
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------''')
    for item in sorted_list: #sorted_list example: {"character": t, "count": 5813}
        if item["character"].isalpha():
            print(f"{item["character"]}: {item["count"]}")
    print("============= END ===============")

def main(directory_path):
    return get_book_text(directory_path)

main(directory_path)