import sys
from stats import (get_word_count, 
    get_word_dct, 
    word_dict_list,
)
    
def main():
    if len(sys.argv) != 2:
        return print("Usage: python3 main.py <path_to_book>"), sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    worddict = get_word_dct(text)
    word_listed = word_dict_list(worddict)
    print_report(book_path, word_count, word_listed)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def print_report(book_path, word_count, word_listed):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in word_listed:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

main()