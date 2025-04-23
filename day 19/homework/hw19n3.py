def pos_neg(list1, list2):
    combined = list1 + list2
    pos = 0
    neg = 0

    for num in combined:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += num

    return pos, neg


a = [1, -3, 5, -2]
b = [-7, 4, 0, 6]

result = pos_neg(a, b)
print("pos:", result[0])
print("neg:", result[1])