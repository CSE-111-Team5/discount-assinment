'''
Emily Cordero
Brother Eisinger
discount.py 
Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input and gets the current day of the week from your computer’s operating system.
'''
# importing a library on time
from datetime import date
from datetime import datetime

dates = datetime.now()
day = dates.weekday()

print(day)