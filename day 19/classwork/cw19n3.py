def removeodd(nums):
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    return even

nums = [1, 3, 2, 6, 8, 9]
print(removeodd(nums))