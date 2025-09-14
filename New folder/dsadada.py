person = {
    "name": "Tazo",
    "age": 16,
    "favorite_animal": "cat"
}



def check_number(num):
    if num > 0:
        return "დადებითი"
    elif num < 0:
        return "უარყოფითი"
    else:
        return "ნული"
    


name = input("ur name:")
age = int(input("ur age"))
favorite_color = input("ur fav color")

user_info = {
    "name": name,
    "age": age,
    "favorite_color": favorite_color
}


def sum_values(data):
    total = 0
    for value in data.values():
        total += value
    return total

fruits = {"apples": 5, "bananas": 3, "oranges": 10}
print(sum_values(fruits))
