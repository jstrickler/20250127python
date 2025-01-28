airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',
            'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles'}

print(airports['LAX'])

airports['SLC'] = 'Salt Lake City'
airports['LAX'] = 'Lost Angels'
print(airports['SLC'])  # print value where key is 'SLC'
print(f"{airports['LAX'] = }")

code = 'PSP'

if code in airports:   # is key in dictionary?
    print(airports[code])  # print key if key is in dictionary
else:
    print(f"{code} not in airports")

print(airports.get(code))  # get value if key in dict, otherwise get None
print(airports.get(code, 'NO SUCH AIRPORT'))  # get value if key in dict, otherwise get 'NO SUCH AIRPORT'

print(airports.setdefault(code, 'Palm Springs'))  # get value if key in dict, otherwise get 'Palm Springs' AND set key
print(code in airports)  # check for key in dict
print(f"{airports = }")

# x = DICT[key]  raises error if key not present
# x = DICT.get(key)   returns None if key not present
# x = DICT.get(key, default_value)  returns default value if key not present

