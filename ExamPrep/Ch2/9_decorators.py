def my_decorator(func):
    def wrapper():
        print("somthing before")
        func()
        print("something after")
    

    return wrapper


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    
    return wrapper_do_twice




# @my_decorator
@do_twice
def say_whee():
    print("whee!!")        

say_whee()
