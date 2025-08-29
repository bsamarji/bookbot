from stats import word_count, char_count

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
    print(f"{num_words} words found in the document")
    char_set = get_unique_chars(book)
    char_dict = char_count(char_set, book)
    print(char_dict)

main()
