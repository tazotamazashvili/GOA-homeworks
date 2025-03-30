def even_last(numbers): 
    sum = 0
    for i in range(0, len(numbers), 2):
        sum += numbers[i] * numbers[-1]  
            
    return sum