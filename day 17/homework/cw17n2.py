list = [1, 2, 3, 4, 5, 6, 7, 8]

def manual_index(lst):
    index = 0
    result = []
    while index < len(lst):
        result.append((index, lst[index]))
        index += 1
    return result

print(manual_index(list))