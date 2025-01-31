# obj = CLASS()
CITIES = list()
CITIES.append("Denver")
CITIES.append("Topeka")

COLORS = list()   # same as colors = []
COLORS.append("blue")

print(f"{type(CITIES) = }")
print(f"{type(COLORS) = }")
print(f"{CITIES = }")

#  KitBuilder   EmployeeInfo   CarParts    ConfigOptions
class Dog:
    def bark(self):
        print("woof! woof!")
    
    def fetch(self):
        print("fetching the stick...")

d1 = Dog()
d2 = Dog()

d1.bark()
d2.fetch()
