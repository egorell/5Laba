def cast(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return type(int(result))
            except ValueError:
                return (str(result) + " Not int")
        return wrapper
    return decorator

@cast(int)
def add(a, b):
    return a + b

result = add("8", "9")
print(result)