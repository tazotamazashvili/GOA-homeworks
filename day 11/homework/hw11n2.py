#code wars

def string_clean(s):
    """
    Function will return the cleaned string
    """
    return ''.join(i for i in s if i not in '0123456789')