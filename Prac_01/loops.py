for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()

number = int(input("Number of starts: "))
for i in range(0, number):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")
