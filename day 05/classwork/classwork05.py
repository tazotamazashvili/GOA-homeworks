#task 1

for number in range(2, 25):
    if number % 2 != 0:
        print(number)

#task 2

saxeli = input("chawere sheni saxeli: ")

for aso in saxeli:
    print(aso)

# task 3

swori_pass = "random"
user_pass = input("chawere sheni paroli: ")

while user_pass != swori_pass:
    print("paroli ar aris swori, scade tavidan.")
    user_pass = input("chawere sheni paroli: ")

print("paroli sworia")