def add_airports(**codes):
    for code, airport in codes.items():
        print(code, airport)

add_airports(RDU="Raleigh-Durham", LAX="Los Angeles", LGA="NY LaGuardia")