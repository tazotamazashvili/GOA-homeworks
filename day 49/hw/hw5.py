people = [
    {"name": "Ana", "age": 17},
    {"name": "Nika", "age": 20},
    {"name": "Giorgi", "age": 25},
    {"name": "Luka", "age": 16}
]

for person in people:
    if person["age"] > 18:
        print(person)
