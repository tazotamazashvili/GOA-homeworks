def pop(word):
    word = word.lower()
    return word == word[::-1]

input_word = input("chawere sityva: ")

if pop(input_word):
    print("aris palindromi")
else:
    print("ar aris palindromi")