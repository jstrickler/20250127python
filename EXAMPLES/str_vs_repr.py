from datetime import date

today = date.today()

print(today)   # uses str(today)
print()
print(repr(today))  # uses repr(today)
print()
print(f"OLD: today = {today}")
print(f"{today = }")  # also uses repr(today)

s = "abc"
print(f"s = {s}")
print(f"{repr(s) = }")

print(f"{today = }")


