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

def greet(whom): # parameters
    print(f"Hello, {whom}")

greet('world')  # arguments
greet('\U0001FDFE')
greet('Python programmers')
greet(1234)
greet(greet)
greet('mom', 'dad')


def zero():
    return 0

print(f"{5 + zero() = }")

def rectangle_area(length, width):
    return length * width

print(f"{rectangle_area(5, 10) = }")
