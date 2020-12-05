def main():
    # Number stuff

    numbers = []

    for i in range(5):
        Num = int(input('Input number {} :'.format(i)))

        numbers.append(Num)

    print('The first number is {}'.format(numbers[0]))

    print('The last number is {}'.format(numbers[-1]))

    print('The smallest number is {}'.format(min(numbers)))

    print('The largest number is {}'.format(max(numbers)))

    print('The average of the numbers is {}'.format(sum(numbers) / len(numbers)))

    # part 2:

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',

                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',

                 'bob']

    name = input('Enter username: ')

    if name in usernames:

        print('Access granted')

    else:

        print('Access denied')


if __name__ == '__main__':
    main()
