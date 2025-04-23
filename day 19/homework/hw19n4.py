def sami(numbers):
    result = [num for num in numbers if num % 3 != 0]
    return result

my_list = [1, 3, 4, 6, 7, 9, 10, 12]
lst = sami(my_list)
print(lst)