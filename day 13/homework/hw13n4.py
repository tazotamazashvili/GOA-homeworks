#ver 1 

def info(name, surname, age, country):
    text = f"""full name: {name} {surname}. age: {age}, from: {country}."""
    return text

name = str(input("sheiyvane saxeli: "))
surname = str(input("sheiyvane gvari: "))
age = int(input("sheiyvane asaki: "))
country = str(input("sheiyvane sheni qveyana: "))

print(info(name, surname, age, country))