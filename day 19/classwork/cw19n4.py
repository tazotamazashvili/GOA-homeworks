def join_numbers(numbers):
    result = ''
    for n in numbers:
        result += str(n)
    return result

nums = [1, 2, 4, 18]
print(join_numbers(nums))
