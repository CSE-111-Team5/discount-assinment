from datetime import datetime

subtotal = float(input('what is the subtotal? '))
dates = datetime.now()
date = dates.weekday()
date = 1 # this is a temp value.

if (date == 1 or date == 2) and (subtotal < 50.00):
    amountmore = 50-subtotal
    print(f'if you spend ${amountmore}. You will be elegable for a 10% discount.')

if subtotal >= 50.00 and (date ==1 or date == 2):
    discount =round(subtotal*.10 ,2)
    print(f'Discounted is ${discount:.2f}')
    subtotal = subtotal - discount

salestax = round(.06 * subtotal, 2)
total = salestax + subtotal

print(f'sales tax: ${salestax:.2f}')
print (f'Your Total is ${total:.2f}')
