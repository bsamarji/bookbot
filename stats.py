def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def char_count(char_list, book_text):
    char_info = {}
    for l in char_list:
        char_info[l] = book_text.count(l)
    return char_info

def sort_on(items):
    return items["num"]

def sort_chars(char_dict):
    char_list = []

    for key in char_dict:
        chars = {
            "char": key,
            "num": char_dict[key]
        }
        char_list.append(chars)

    char_list.sort(reverse=True, key=sort_on)
    return char_list
