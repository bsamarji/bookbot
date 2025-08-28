def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words


def main():
    file = "books/frankenstein.txt"
    book = get_book_text(file)
    num_words = word_count(book)
    print(f"{num_words} words found in the document")


main()
