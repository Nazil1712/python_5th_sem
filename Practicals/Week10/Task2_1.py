def log_function_call(func):
    def wrapper(*args,):
        result = func(*args,)
        print(f"Calling {func.__name__} with arguments: {args}")
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

result1 = add(2, 3)
result2 = multiply(4, 5)
