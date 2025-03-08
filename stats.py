from collections import Counter


def get_num_words(string):
    ## count number of words from a string
    return len(string.split())

def characters_count(string):
    result = {} 
    string = string.lower()
    for s in string: 
        count = result.get(s, None)
        if count:
            result[s] = count + 1
        else:
            result[s] = 1
        
    return result
    # return dict(Counter(string.lower()))


if __name__ == "__main__":
    a = characters_count("geeks for geeks")
    print(a)