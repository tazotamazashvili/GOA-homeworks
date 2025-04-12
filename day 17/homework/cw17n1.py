list = [1, 2, 3, 4, 5]
def manual_remove(list):
    for int in list:
        if int == 5:
            list.remove(int)
    return list

print(manual_remove(list))