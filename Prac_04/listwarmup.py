def main():
    # TODO: Change the first element of numbers to "ten" (the string, not the number 10)
    # TODO: Change the last element of numbers to 1
    numbers = ["10", 1, 4, 1, 5, 9, 1]

    #default:
    print(numbers[0])                           #3
    print(numbers[-1])                          #2
    print(numbers[3])                           #1
    print(numbers[:-1])                         #[3, 1, 4, 1, 5, 9]
    print(numbers[3:4])                         #[1]
    print(5 in numbers)                         #True
    print(7 in numbers)                         #False
    print("3" in numbers)                       #False
    print(numbers + [6, 5, 3])                  #[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    # TODO: Get all the elements from numbers except the first two (slice)
    print(numbers[2:])                          #[4, 1, 5, 9, 1]
    print(9 in numbers)                         #True
if __name__ == '__main__':
    main()
