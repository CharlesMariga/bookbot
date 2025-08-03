def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1
    return chars

def get_sorted_dict(dict):
    chars = []
    for item in dict:
            chars.append({ "char": item, "num": dict[item] })
    
    def sort_on(items):
        return items["num"]

    chars.sort(reverse=True, key=sort_on)
    return chars