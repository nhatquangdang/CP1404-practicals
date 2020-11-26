Min = 6


def main():
    password = get_password(Min)
    print('*' * len(password))


def get_password(Min):
    password = input("Enter password with {} or more charaters".format(Min))
    while len(password) < Min:
        print("Enter again")
        password = input("Enter password with {} or more charaters".format(Min))
    return password


main()
