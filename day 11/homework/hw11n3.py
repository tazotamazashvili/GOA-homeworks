#code wars

def add_length(str_):
    words = str_.split()
    return [f"{word} {len(word)}" for word in words]