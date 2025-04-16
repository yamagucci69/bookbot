def get_num_words(file_content):
    words = file_content.split()
    num_words = len(words)
    return num_words

def character_frequency(file_content):
    characters = file_content.lower()
    dict_of_characters= {}
    for character in characters:
        if character in dict_of_characters:
            dict_of_characters[character] += 1
        else:
            dict_of_characters[character] = 1
    return dict_of_characters

def dictionary_list(dict_of_characters):
    list_of_dictionaries =[]
    for char, count in dict_of_characters.items():
        list_of_dictionaries.append({"character": char, "count": count})
        list_of_dictionaries.sort(reverse=True, key=lambda dict: dict["count"])
    return list_of_dictionaries



