items = int(input("Number of items: "))
total = 0
while items <= 0:
    items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total = total * (90 / 100)
print("Total price for " + str(items) + " items is ${:.2f}".format(total))
