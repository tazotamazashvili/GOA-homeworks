num = input("chawere samnshina ricxvi")

if len(num) == 3:
    aseuli = int(num[0])
    ateuli = int(num[1])
    erteuli = int(num[2])
    sumnum = aseuli + ateuli + erteuli
    sum = int(num) % sumnum
    print(sum)
else:
    print("samnishna chawere")
