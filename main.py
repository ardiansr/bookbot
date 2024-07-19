import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    chars_list = dict_to_sorted_desc_list(chars_dict)
    for char in chars_list:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End report ---")


def dict_to_sorted_desc_list(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"char": key, "num": dict[key]})
    dict_list.sort(reverse=True, key=lambda dict: dict["num"])
    return dict_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
