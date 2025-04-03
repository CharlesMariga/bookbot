from stats import get_num_words, get_num_characters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(f"./{sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    num_chars_dict = get_num_characters(book_text)
    char_count = sort_dictionary(num_chars_dict)
    for char in char_count:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()