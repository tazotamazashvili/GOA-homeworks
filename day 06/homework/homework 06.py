#task 1

num1 = int(input("chawere ricxvi: "))

sum = 0

for num in range (1, num1 + 1):
    if num % 2 != 0:
        sum += num

print("kenti ricxvebis jami aris: ", sum)

# task 2

num2 = int(input("chawere ricxvi 1-dan 100-mde: "))

for num in range(1, 101):
    if num % num2 == 0:
        print(num)

# task 3

swori_pass = "random"
user_pass = input("chawere sheni paroli: ")

cda = 0

while user_pass != swori_pass and cda < 3:
    cda += 1
    print("paroli ar aris swori, scade tavidan.")
    user_pass = input("chawere sheni paroli: ")

if user_pass == swori_pass:
    print("paroli sworia")
else:
    print("paroli arasworia")

#task 4

user_input = input("Enter a string: ")

print(user_input[::-1])