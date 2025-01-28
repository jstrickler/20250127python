cities = []  # empty list
cities = list() # also empty list
cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print("after cities.append('Miami')")
print("after cities.append('Montgomery')")
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

# iterable: object that can be looped over with 'for'
# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3] # del any-object
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()  # removes LAST element
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3) # remove specific element
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)
print()

stuff = [5, 88.9, "foo", [1, 2, 3], "bar", b'abc', ('a', 'b', 'c')]
print(f"{stuff = }")
print(f"{len(stuff) = }")
