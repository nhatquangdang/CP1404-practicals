# Question 1
out_file = open('name.txt', 'w')
name = input("Enter a name: ")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# Question 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# Question 4
in_file = open("numbers.txt", "r")
total = 0
for i in in_file:
    numbers = int(i)
    total += numbers
in_file.close()
print(total)
