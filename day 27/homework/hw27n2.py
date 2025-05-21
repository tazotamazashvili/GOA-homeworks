password = input("input ur password: ")

if len(password) < 8:
    print("password too short")
if len(password) > 8:
    print("password accepted")