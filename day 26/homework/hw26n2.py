# შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს ლისტს და გამოიტანეთ ის data type რომელიც ყველაზე ხშირად გვხვდება ამ ლისტსში.




def most_common_type(lst):
    types = []

    for item in lst:
        types.append(type(item))

    most_common = None
    max_count = 0

    for t in types:
        count = types.count(t)
        if count > max_count:
            max_count = count
            most_common = t

    print("Most common type is:", most_common.__name__)
