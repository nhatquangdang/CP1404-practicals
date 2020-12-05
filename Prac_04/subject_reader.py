"""

CP1404/CP5632 Practical

Data file -> lists program

"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()

    print(data)

    display_the_mission(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""

    data = []

    input_file = open(FILENAME)

    for line in input_file:
        line = line.strip()  # Remove the \n

        parts = line.split(',')  # Separate the data into its parts

        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)

        data.append(parts)

    input_file.close()

    return data


def display_the_mission(data):
    for line in data:
        print('{} is taught by {} and has {} student'.format(line[0], line[1], line[2]))


main()
