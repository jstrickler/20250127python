fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon",
         "Kiwi", "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG",
         "pear", "banana", "Tamarind", "persimmon", "elderberry", "peach",
         "BLUEberry", "lychee", "grape"]

def ignore_case(single_fruit):
    comparison_value = single_fruit.lower()
    print(f"Comparing '{single_fruit}' as '{comparison_value}'")
    return comparison_value

sorted_fruits = sorted(fruits, key=ignore_case)
print(f"{sorted_fruits = }\n")
