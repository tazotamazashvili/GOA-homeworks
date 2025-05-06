def combine_strings_and_numbers(*args):
    result = ""
    numbers = ""

    for arg in args:
        if type(arg) == int:
            numbers += str(arg) + " "
        else:
            result += str(arg) + " "

    return result + numbers