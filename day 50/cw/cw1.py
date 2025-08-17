def square_digits(num):
    num_str = str(num)          
    squares = []

    for digit in num_str:
        number = int(digit)
        square = number ** 2
        squares.append(str(square))

    result_str = ''.join(squares)
    return int(result_str)