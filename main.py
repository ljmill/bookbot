def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    char_list = dict_to_char_list(chars_dict)
    sorted_char_list = sort_list_by_total(char_list)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_char_list:
        print(f"The '{item["char"]}' character was found {item["total"]} times")
        
    print("--- End report ---")

def sort_on_total(dict):
    return dict["total"]

def sort_list_by_total(list):
    list.sort(reverse=True, key=sort_on_total)
    return list

def dict_to_char_list(dict):
    char_counts = []
    for item in dict:
        if item.isalpha():
            char_counts.append({"char": item, "total": dict[item]})
    return char_counts

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()