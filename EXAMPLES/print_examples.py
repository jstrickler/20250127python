city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

print(city, temperature, hit_count, average)
print()

print(city, end=' ')  # Print space instead of newline at the end
# conditional code here...
print(temperature)
print()

# Item separator is comma + space
print(city, temperature, hit_count, average, sep=", ")
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="")
print()

print(city, temperature, "\n", hit_count, end="\n\n\n", sep=" ")
print("next line")

print(f"{city} {temperature}\n{hit_count}\n\n\n")

#  f"....{value}.....{value}....{value}....""

country = "Spain"
city = "Barcelona"
print(f"{city}, {country}")

x = f"{city}, {country}"

pi = 22 / 7
print("pi is", pi)
print(f"pi is {pi:.3f}")

