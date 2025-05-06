def divide_larger_by_smaller(a, b):
    try:
        a = float(a)
        b = float(b)

        larger = max(a, b)
        smaller = min(a, b)

        if smaller == 0:
            return "cant divide by 0"

        return larger / smaller

    except ValueError:
        return "number must have a meaning"
