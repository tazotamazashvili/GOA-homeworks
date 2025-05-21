num1 = int(input("first: "))
num2 = int(input("second: "))
num3 = int(input("third: "))
num4 = int(input("fourth: "))
num5 = int(input("fifth: "))

lst = []

lst.append(num1)
lst.append(num2)
lst.append(num3)
lst.append(num4)
lst.append(num5)

total = sum(lst)
print("the sum:", total)