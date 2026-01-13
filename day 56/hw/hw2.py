def num(lst):
    result = []
    for i in lst:
        if lst.count(i) == 1:
            result.append(i)
    return result