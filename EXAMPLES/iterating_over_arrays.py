fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon']

# ITERABLE can be str, bytes, list, tuple, set, dict, 
#    *iterator*
# for VAR in ITERABLE: 
#    ...
for fruit in fruits:
    # fruit = fruits[0]; fruit = fruits[1]; ...
    print(fruit)
print(f"{fruit = }")

print()

for char in fruits[1]:
    print(char)
print()