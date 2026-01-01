char_dict = {}

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_path):
    num_words = 0
    text_content = get_book_text(file_path).split()
    for i in text_content:
        num_words += 1
    print(f"Found {num_words} total words")

def char_count(file_path):
    text_content = get_book_text(file_path).split()
    for word in text_content:
        word = word.lower()
        word_chars = list(word)
        for char in word_chars:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    #for unique_char in char_dict:
        #quantity = char_dict[unique_char]
        #print(f"'{unique_char}': {quantity}")

def sort_on(items):
    return items["num"]

def sorted_char_dicts():
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list