# task 1

num = int(input("put in a number: "))

print("here's every divider for this number:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)