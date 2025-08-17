def scramble(strng, array):
    result = [''] * len(strng)
    i = 0
    while i < len(strng):
        index = array[i]
        letter = strng[i]
        result[index] = letter
        i = i + 1
    return ''.join(result)

print(scramble("abcd", [0, 3, 1, 2]))