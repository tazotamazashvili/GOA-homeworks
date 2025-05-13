def result_type():
    expr = input("Put in the equation")
    parts = expr.split()

    if len(parts) != 3:
        print("Incorrect format")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        print("Unknown Format")
        return

    print(type(result).__name__)
