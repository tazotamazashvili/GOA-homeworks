#cw 1


text = int(input("chawere texti: "))
res = 2

print(text * res)

#cw 2 
for i in range(100, 0, -1):
    print(i)

#cw 4

for i in range(250, 500):
    if i % 10 == 0:
        print(i)

#cw 5

texti = input("chawere texti: ")

if texti.startswith('_'):
    print(True)
else:
    print(False)

#cw 6

num = int(input("chawere ricxvi"))
i = 10

if num %2 == 0:
    print("yes" * i)
else:
    print("no")