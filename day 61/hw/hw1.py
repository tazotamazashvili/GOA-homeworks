#1 import random

#2 list

#3 while loop

#4 input

#5 for loop

import random

def words():
    words = ["hello", "world", "how", "coffee", "tea"]

    word = random.choice(words)

    guessed_word = []

    right_words = set()

    for i in word:
        guessed_word.append("_")

    print(guessed_word)

    hearts = 6

    while hearts > 0:
        game = input("chawere aso: ").lower()
        if game in right_words:
            print("sworia")
            