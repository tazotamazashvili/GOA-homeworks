def flt(list, divider):
    result = [num for num in list if num % divider == 0]
    return result

numbers = [1, 23, 165, 2, 3, 92, 10, 34, 911]
divider = 3
res = flt(numbers, divider)

print(res)