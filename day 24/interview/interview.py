#Funqcia romelsac gadaecema stringi da abrunebs xmovnebis gareshe
def novowels(word):
    result = ''
    for i in word:
        if i.lower() not in 'aeiou':
            result += i
    return result