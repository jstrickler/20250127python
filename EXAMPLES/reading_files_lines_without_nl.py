FILE_PATH = '../DATA/mary.txt'

with open(FILE_PATH) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # splitlines() splits string on '\n' into lines
    print(lines_without_nl)

with open('../DATA/breakfast.txt') as breakfast_in:
    all_data = breakfast_in.read().splitlines() # without newlines
    # all_data = breakfast_in.readlines() with newlines
    print(f"{all_data = }")

bacon_count = all_data.count('waffles')
print(f"{bacon_count = }")
