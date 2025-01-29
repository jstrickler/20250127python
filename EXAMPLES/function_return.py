def get_hello():
    return "Hello, world"

h = get_hello()   # h = "Hello, world" 
print(f"{h = }")

def hello():
    print("Hello, world")
    # return None

h = hello()
print(f"{h = }")

def double(x):
    return x * 2

d = double(10)
print(f"{d = }")

def greet(whom):
    print(f"Hello, {whom}")

greet('world')
greet('\U0001FDFE')
greet('Python programmers')
