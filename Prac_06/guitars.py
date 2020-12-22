from Prac_06.guitar import Guitar

list = []


def main():
    print("My guitars!")
    print("To open list, enter nothing in the name")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        AddGuitars = Guitar(name, year, cost)
        list.append(AddGuitars)
        print(AddGuitars, "added.")
        name = input("Name: ")
    if list:
        list.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(list):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1} ({1}), worth ${1} {2}".format(i+1, guitar, vintage_string))
    else:
        print("No guitars")


main()
