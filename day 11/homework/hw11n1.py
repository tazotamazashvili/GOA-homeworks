#code wars

def calculator(x, y, op):
    if type(x) not in (int, float) or type(y) not in (int, float):
        return "unknown value"
    
    if op == '+': return x + y
    if op == '-': return x - y
    if op == '*': return x * y
    if op == '/': return x / y if y != 0 else "unknown value"

    return "unknown value"