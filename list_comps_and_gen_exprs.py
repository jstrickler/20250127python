fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print(f"{f0 = }\n")

f1 = [f.upper() for f in fruits]  # list comprehension
print(f"{f1 = }\n")

#  list comprehension
#  [EXPR for VAR in ITERABLE in condition]

#  generator expression
#   (EXPR for VAR in ITERABLE if CONDITION)


f_gen = (f.upper() for f in fruits)
print(f"{f_gen = }")
for fruit in f_gen:
    print(fruit)
print()

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f.title() for f in fruits if len(f) > 8]
print(f"{f3 = }\n")

#    [EXPR for VAR in ITERABLE ...]
f4 = [f for f in fruits if f[1] == 'a']
print(f"{f4 = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

n1 = [int(n * .5) for n in nums]
print(f"{n1 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [person[3] for person in people]
print(f"{dobs = }\n")

