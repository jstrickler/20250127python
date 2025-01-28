print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if not raw_quantity:
        print("please enter quantity from 1 to 8")
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop
    quantity = int(raw_quantity)  # could validate via try/except
    if (quantity < 1) or (quantity > 8):
        print("please enter quantity from 1 to 8")
        continue
    print(f"sending {raw_quantity} ticket(s)")
