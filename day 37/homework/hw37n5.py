def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        next_root = int(root) + 1
        return next_root ** 2
    return -1
