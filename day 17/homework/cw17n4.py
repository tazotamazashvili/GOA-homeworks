list = [1, 2, 3, 4, 5, 6, 7, 8]

def manual_pop(list):
    element = list[-1]
    del list[-1]
    return element

print(manual_pop(list))