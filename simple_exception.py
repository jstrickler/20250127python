import logging

logging.basicConfig(
    filename="LOGS/wombats.log",
    level=logging.DEBUG,
)
raw_value = input("Enter a number: ")
logging.debug("User entered %s", raw_value)

try:  # run some code that might raise an error
    number = float(raw_value)
except Exception as err:  # check for exception
    logging.exception(err)
else: # if no exceptions were caught
    print(f"You entered the value {number * 10}")
finally: # cleanup
    print("FINALLY!")

print("program continues...")
