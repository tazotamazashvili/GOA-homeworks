countries = []

for i in range(3):
    country = input("chawere qveyana: ")
    countries.append(country)
    
capitals = {
    countries[0]: "tbilisi",
    countries[1]: "madrid",
    countries[2]: "berlin"
}

for country, capital in capitals.items():
    print(capital)
    
search = input("enter a country to find its capital: ")

if search in capitals:
    print("capital is:", capitals[search])
else:
    print("country not found")