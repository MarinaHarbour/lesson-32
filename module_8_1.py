def add_everything_up(a, b):
    try:
        c = a + b
        if isinstance(c, (int, float)):
            return c
    except TypeError as exc:
        if isinstance(a, str):
            return a + str(b)
        else:
            if isinstance(b, str):
                return str(a) + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
