def main():
    path = "books/frankenstein.txt"
    text = book_text(path)
    words = word_count(text)
    characters = char_count(text)
    sorted_char = better_dict(characters)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in this document")
    for item in sorted_char:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def word_count(text):
    w = text.split()
    return len(w)

def book_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    letter_count = {}
    lower_case = text.lower()
    for l in lower_case:
        if l in letter_count:
            letter_count[l] += 1
        else:
            letter_count[l] = 1
    return letter_count
    
def sort_on(dict):
    return dict["num"]

def better_dict(characters):
    char_list = [{"char" : k, "num" : v} for k, v in characters.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()