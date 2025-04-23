def sort(list1, list2):
    combined = list1 + list2
    lst = sorted(combined)
    return lst

l1 = [5, 2, 9]
l2 = [1, 8, 3]

result = sort(l1, l2)
print(result)