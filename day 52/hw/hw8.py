import random
num = random.randint(1, 100)

while True:
    try:
        guess = int(input("chawere ricxvi: "))
        
        if guess < 1 or guess > 100:
            print("ricxvi unda iyos 1 dan 100 mde")
            continue

        if guess < num:
            print("metia")
        elif guess > num:
            print("naklebia")
        else:
            print("sworia")
            break
    except ValueError:
        print("sheiyvane MXOLOD RICXVI.")