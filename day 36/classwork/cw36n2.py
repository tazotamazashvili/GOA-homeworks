def check_vowel(strng, position):
    vowels = 'AaEeIiOoUu'
    if position < 0 or position >= len(strng):
        return False
    return strng[position] in vowels