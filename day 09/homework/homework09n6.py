name = str(input("chawere sheni saxeli"))
last_name = str(input("chawere sheni gvari"))

def say_name(name, lastname):
    return f"{name[0]}. {lastname}"

res = say_name(name, last_name)
print(res)