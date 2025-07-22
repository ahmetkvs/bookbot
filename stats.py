def get_word_count(text):
    text_list = text.split()
    return len(text_list)

def get_char_counts(text):
    char_counts = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char not in char_counts:
            char_counts[lowered_char] = 1
        else:
            char_counts[lowered_char] += 1
    return char_counts

def get_sorted_char_counts(char_counts_dict):   
    char_count_dicts_list = []
    for char, count in char_counts_dict.items():
        each_dict = {"char": char, "num": count}
        char_count_dicts_list.append(each_dict)
    #print(char_count_dicts_list)
    char_count_dicts_list.sort(reverse=True, key=sort_on)
    return char_count_dicts_list

def sort_on(each_dict):
        return each_dict["num"]