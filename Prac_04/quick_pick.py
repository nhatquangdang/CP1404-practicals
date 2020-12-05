import random


def Check(array):
    flag = True
    while flag:
        flag = False

        for i in range(len(array) - 1):
            try:
                num = array[i + 1]
            except IndexError:
                break

            if array[i] == num:
                array.pop(i + 1)
                flag = True

    return len(array)


def main():
    Number = int(input('How many "quick picks" you want: '))
    Raw = []
    CONSTANTS = []
    for i in range(Number):

        for j in range(6):
            Raw.append(random.randint(1, 45))
            Raw.sort()
        while Check(Raw) < 6:
            Raw.append(random.randint(1, 45))
            Raw.sort()

        CONSTANTS.append(Raw)
        Raw = []

    for lines in CONSTANTS:
        for col in range(6):
            print('{}'.format(lines[col]), end=' ')
        print()


if __name__ == '__main__':
    main()


