def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
 
def sort_on(dict):
    return dict["num"]

def sort_dictionary(chars_dict):
    chars_count_list = []
    for key in chars_dict:
        chars_count_list.append({ 'char': key, 'num': chars_dict[key] })
    chars_count_list.sort(reverse=True, key=sort_on)
    return chars_count_list