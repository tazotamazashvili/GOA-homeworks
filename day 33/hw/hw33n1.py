def manual_split(s, delimiter=' '):
    result = []
    current = ''
    for char in s:
        if char == delimiter:
            if current:
                result.append(current)
                current = ''
        else:
            current += char
    if current:
        result.append(current)
    return result
