# გაიარეთ Python introduction "Memory & Variables"-ის ჩათვლით

#hw 4

num = int(input("chawere ricxi 50-is chatvlit: "))

while num < 1 or num > 50:
    print("tavidan sheiyvane ricxi 50-is chatvlit")
    num = int(input("chawere ricxi 50-is chatvlit: "))

for i in range(num, 101, num):
    print(i)

#hw 5

print("gamoicani ricxvebis tanmimdevroba")

while True:
    user = int(input("sheiyvane ricxvi: "))
    
    if user == 6788:
        print("gamoicani!")
        break
    else:
        print("ar gamoicani")