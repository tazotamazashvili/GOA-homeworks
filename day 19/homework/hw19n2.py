def lst_sum(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    if sum1 > sum2:
        return list1
    elif sum2 > sum1:
        return list2
    else:
        return "siis jami aris tanabari"
    

a = [1, 5, 9]
b = [2, 4, 6]

result = lst_sum(a, b)
print(result)