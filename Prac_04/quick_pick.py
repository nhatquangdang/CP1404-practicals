import random
in_line = 6
minimum = 1
maximum = 45

def main():
    quickpicks = int(input("Enter numbers to roll: "))
    while quickpicks < 0:
        print("Invalid number")
        quickpicks = int(input("Enter numbers to roll: "))
    for i in range(quickpicks):
        picks = []
        for j in range(in_line):
            numbers = random.randint(minimum,maximum)
            while numbers in picks:
                #This While loop works when same number appear in same line
                numbers = random.randint(minimum,maximum)
            picks.append(numbers)
        picks.sort()
        print(picks)
main()


