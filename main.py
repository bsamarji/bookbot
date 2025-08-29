from stats import word_count, char_count, sort_chars

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read().lower()
    return file_contents

def get_unique_chars(book_text):
    return set(book_text.lower())

def main():
    file = "books/frankenstein.txt"
    book = get_book_text(file)
    num_words = word_count(book)
    char_set = get_unique_chars(book)
    char_dict = char_count(char_set, book)
    sorted_chars = sort_chars(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()
