def clean_list(lst):
    other = None

    for item in lst:
        if type(item) != int:
            other = item

    if other is not None:
        lst.remove(other)

    return lst
