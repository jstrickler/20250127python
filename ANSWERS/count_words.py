import sys

if len(sys.argv) < 3:
    print("Syntax: count_words.py PATTERN FILE ...")
    sys.exit()

pattern = sys.argv[1]  # sys.argv[0] is script name

for file_name in sys.argv[2:]:
    count = 0
    with open(file_name) as file_in:
        for line in file_in:
            if pattern in line:
                count += 1

    print(f'''"{pattern}" occurred on  {count} lines in {file_name}''')
