#შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან არგუმენტს და მისი type-ის სესაბამისად გამოიტანეთ სიტყვები:
# Str - "Literature"
# Int/Float - "Math"
# Bool - "Science"

def identify_subject(value):
    if isinstance(value, str):
        print("Literature")
    elif isinstance(value, (int, float)):
        print("Math")
    elif isinstance(value, bool):
        print("Science")
    else:
        print("Unknown type")
