list = [1, 2, 3, 4, 5, 6]

def manual_len(l):
    res = 0
    if type(l) == list:
        for i in list:
            res += 1
    elif type(l) == str or type(l) == int:
        for i in str(l):
            res += 1
            
    return res
    
print(manual_len(list))