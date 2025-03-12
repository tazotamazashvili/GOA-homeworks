#cw 1

user_input = input("chawere sityva: ")
reversed_string = ""

for i in user_input(len(user_input) - 1, -1, -1):

    reversed_string += user_input[i]

print("shemotrialebuli sityva:", reversed_string)

#cw 2

sum = 0
for i in range(0, 101):
    sum += i

print("jami:", sum)

#cw 3

user_input = input("sheiyvanet sam asoiani sityva: ")

for i in range(3):
    if len(user_input) != 3:
        print("unda chawerot 3 asoiani sityva.")
        user_input = input("sheiyvanet 3 asoiani sityva: ")

        print("Palindrome:", user_input[0] == user_input[2])
    else:
        break

#cw 4

for i in range(100, 301):
    print(i ** 2)

#cw 5

for i in range(1000):
    print(i % 2 == 1)

#cw 6

user_input = int(input("chawere ricxvi: "))

fesvi = user_input ** 0.5

print(fesvi)