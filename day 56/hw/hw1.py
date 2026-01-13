def xshiri(a):
    max_letter = ''
    max_count = 0

    for i in set(a):
        count = a.count(i)
        if count > max_count:
            max_count = count
            max_letter = i

    return max_letter