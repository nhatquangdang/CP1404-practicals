import random

max_increase = 0.1
max_decrease = 0.05
MAX = 1000
MIN = 0.01
price = 10
OUTPUT_FILE = "capitalist_conrad.txt"
out_file = open(OUTPUT_FILE, 'w')
# Please change to 'a' if you already have a file

day = 0
print("Starting price: ${:,.2f}".format(price), file=out_file)
while price >= MIN and price <= MAX:
    change = 0
    day += 1
    # Random 1, 2 for 50% chance of increase or decrease
    if random.randint(1, 2) == 1:
        change = random.uniform(0, max_increase)
    else:
        # - max_decrease to decrease 5% to 0%
        change = random.uniform(-max_decrease, 0)
    price *= (1 + change)
    print("On day {} price is: ${:,.2f}".format(day, price), file=out_file)
out_file.close()
