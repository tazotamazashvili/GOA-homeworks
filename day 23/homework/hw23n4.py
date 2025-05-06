def check_type(value, type_name):
    if type_name.lower() == "str":
        return type(value) == str
    elif type_name.lower() == "int":
        return type(value) == int
    elif type_name.lower() == "float":
        return type(value) == float
    elif type_name.lower() == "bool":
        return type(value) == bool
    else:
        return False
