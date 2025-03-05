# task 1

number = int(input("put in ur number: "))
prime = True

for i in range(2, number):
    if number % i == 0:
        prime = False

if number > 1 and prime:
    
    print("your number is a prime!")

else:

    print("your number is not a prime!")