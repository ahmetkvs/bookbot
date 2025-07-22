from stats import get_word_count, get_char_counts, get_sorted_char_counts
import sys

def get_book_text(file_path):
    book_text_as_string = ""
    with open(file_path) as f:
        book_text_as_string = f.read()
    return book_text_as_string


def print_character_count(char_counts_dict_list):
    print("--------- Character Count -------")
    for char_count_dict in char_counts_dict_list:
        if char_count_dict["char"].isalpha():
            char = char_count_dict["char"]
            num = char_count_dict["num"]
            print(f"{char}: {num}")



def main():
    if len(sys.argv) == 2:
        book_location = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    book_string = get_book_text(book_location)
    num_of_words = get_word_count(book_string)
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    char_counts = get_char_counts(book_string)
    char_counts_dict_list = get_sorted_char_counts(char_counts)
    print_character_count(char_counts_dict_list)


main()