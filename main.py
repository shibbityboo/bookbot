from stats import word_count, char_count, sorted_char_dicts
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    char_count(f"{sys.argv[1]}")
    sorted_list = sorted_char_dicts()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    word_count(f"{sys.argv[1]}")
    print("--------- Character Count -------")
    for dictionary in sorted_list:
        dict_char = dictionary["char"]
        if dict_char.isalpha():
            count = dictionary["num"]
            print(f"{dict_char}: {count}")
    print("============= END ===============")
main()