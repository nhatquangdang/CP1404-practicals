def user_name(email):
    split1 = email.split('@')[0]
    split2 = split1.split('.')
    name = " ".join(split2).title()
    return name


def main():
    user_email = {}
    email = input("Enter your email: ")
    while email != "":
        name = user_name(email)
        ask = input("Is your name {} ? (Y/N)".format(name)).upper()
        if ask != "Y" and ask != "":
            name = input("Input your name: ")
        user_email[email] = name
        email = input("Enter your email: ")
    for email, name in user_email.items():
        print("{} ({})".format(name, email))
main()
