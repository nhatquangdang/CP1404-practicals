def main():
    input_file = open("temps_input.txt", "r")
    output_file = open("temps_output.txt", "w")
    for i in input_file:
        exchange = F_to_C(float(i))
        print(exchange, file=output_file)
    input_file.close()
    output_file.close()


def F_to_C(fahrenheit):
    # Convert fahrenheit to celsius
    return 5 / 9 * (fahrenheit - 32)


main()
