def unique_sum(lst):
    if not lst:
        return None
    
    list = []
    total = 0
    
    for num in lst:
        if num not in list:
            list.append(num)
            total += num
            
    return total