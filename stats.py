def get_word_count(text):
    return len(text.split())

def get_word_dct(text):
    word_count_dict = {}
    fixed_text = text.lower()
    for word in fixed_text:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

def sort_key(d):
    return d["num"]

def word_dict_list(worddict):
    word_listed = []
    for key in worddict:
        values = worddict[key]
        word_listed.append({"char" : key, "num": values})
    word_listed.sort(reverse=True, key=sort_key)
    return word_listed

