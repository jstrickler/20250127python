from datetime import datetime

# Bill Gates's birthday
gates_bd = datetime(1955, 10, 28, 20, 58, 0)  # Create a datetime object

print(gates_bd)  # Print using default format
print()

print(gates_bd.strftime('Bill was born on %B %d, %Y at %I:%M %p'))  # Format using strftime()
print()

print(gates_bd.strftime('BG: %m/%d/%y'))  # Format using strftime()
print()

print(gates_bd.strftime('Mr. Gates was born %d-%b-%Y'))  # Format using strftime()
print()

print(gates_bd.strftime('log entry: %Y-%m-%d'))  # Format using strftime()
print()
