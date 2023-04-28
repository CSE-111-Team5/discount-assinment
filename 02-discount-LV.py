"""You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%."""

from datetime import datetime

#VARIABLES
today = datetime.now()
day = today.weekday()

subtotal = float(input("Please enter the subtotal: "))

if day == 1 or day == 2:
    if subtotal >= 50:
        discount = subtotal * 0.1
        print(f"Discount amount: {discount:.2f}")
        new_subtotal = subtotal - discount
        tax = new_subtotal * 0.06
        total = new_subtotal +  tax
    else:
        tax = subtotal * 0.06
        total = subtotal +  tax
else:
    tax = subtotal * 0.06
    total = subtotal +  tax

print(f"Sales tax amount:{tax:.2f}")
print(f"Total: {total:.2f}")