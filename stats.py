def word_counter(text):
    words = text.split()
    count = len(words)
    return count

def character_counter(text):
    character_counter = {}
    text = text.lower()
    characters = list(text)
    #print(characters)
    for character in characters:
        if character not in character_counter:
            character_counter[character] = 1
        else:
            character_counter[character] += 1
    return character_counter

def get_count(item):
    return item["num"]

def dictionary_sorter(dictionary):
    char_list =[]
    for c, n in dictionary.items():
        char_list.append({"char": c, "num": n})
    char_list.sort(key= get_count, reverse = True)
    return char_list