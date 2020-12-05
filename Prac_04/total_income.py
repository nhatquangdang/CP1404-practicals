"""

CP1404/CP5632 Practical

Starter code for cumulative total income program

"""


def Calculator(NumberofMonths, incomes):
    print("\nIncome Report\n-------------")

    total = 0

    for month in range(1, NumberofMonths + 1):
        income = incomes[month - 1]

        total += income

        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def main():
    """Display income report for incomes over a given number of Months."""

    incomes = []

    NumberofMonths = int(input("How many Months? "))

    for month in range(1, NumberofMonths + 1):
        # TODO: the string format() method instead of string concatenation (+).

        income = float(input("Enter income for month {} :".format(month)))

        incomes.append(income)

    Calculator(NumberofMonths, incomes)


if __name__ == '__main__':
    main()
