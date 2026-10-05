#main func > fuction add without changing the main func code
def my_decorator(func):
    def wrapper():
        print("hi soniya")
        func()
        print("hi sarthak")
    return wrapper
@my_decorator
def say_hello():
    print("hello everyone")

say_hello()    
    
