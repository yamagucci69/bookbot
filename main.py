import sys 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path= sys.argv[1]
    file_content = get_book_text(file_path)
    num_words = get_num_words(file_content)
    dict_of_characters = character_frequency(file_content)
    list_of_dictionaries = dictionary_list(dict_of_characters)
    report = print_list_of_dictionaries(list_of_dictionaries, num_words, file_path)


def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def print_list_of_dictionaries(list_of_dictionaries, num_words, file_path):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {file_path}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += "--------- Character Count -------\n"

    for char_dict in list_of_dictionaries:
        char = char_dict["character"]
        count = char_dict["count"]

        if char.isalpha():
            report += f"{char}: {count}\n"
    report += "============= END ==============="
    print(report)
    return report


from stats import get_num_words
from stats import character_frequency
from stats import dictionary_list
main()