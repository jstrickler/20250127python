airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma', 'YCC': 'Calgary',
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

#   KEY, VALUE
for abbr, airport in airports.items():  # items() returns an iterable of key:value pairs
    print(abbr, airport)

print('-' * 60)

for abbr, airport in sorted(airports.items()):  # iterate, sorted by key
    print(abbr, airport)

# for KEY_VAR, VALUE_VAR in DICT.items():
    # ...

