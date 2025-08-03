from stats import get_num_words, get_num_chars, get_sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_content = get_book_text(sys.argv[1])
    words_count = get_num_words(file_content)
    chars_count = get_num_chars(file_content)
    sorted_chars_count = get_sorted_dict(chars_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")

    for item in sorted_chars_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()