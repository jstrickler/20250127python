"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # sorted() returns a list

print(sorted_fruit)

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

sorted_nums = sorted(nums)
print(f"{sorted_nums = }")
