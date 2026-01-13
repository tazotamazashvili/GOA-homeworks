sia = []
sia1 = []

for _ in range(5):
    fruit = input("chawere sheni sayvareli xili: ")
    sia.append(fruit)

for _ in range(2):
    fruit = input("kidev: ")
    sia1.append(fruit)

if len(sia1) > 1:
    item1 = sia1.pop(1)
else:
    item1 = None

siebi = sia + sia1

sorted_siebi = sorted(siebi)

print(siebi)
print(sorted_siebi)