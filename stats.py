def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def char_count(char_list, book_text):
    char_info = {}
    for l in char_list:
        char_info[l] = book_text.count(l)
    return char_info
