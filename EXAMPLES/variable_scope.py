animal = "wombat"  # global variable

def spam():
    a = 100   # local variable
    print(f"{animal = }")
    print(f"{a = }")

def ham():
    a = "apple"  # local variable
    print(f"{animal = }")
    print(f"{a = }")

def eggs(color):
    # color is local variable
    print(f"{animal = }")
    print(f"{color = }")

spam()
print()  # blank line
ham()
print()
eggs("green")