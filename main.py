def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file = "books/frankenstein.txt"

    book = get_book_text(file)
    print(book)

main()
