Current_year = 2020
Vintage_age = 100

class Guitar:
    # self.name, self.year, self.cost are attributes
    def __init__(self, name="No name", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "My guitar: {}, first made in {}, its cost ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return Current_year - self.year

    def is_vintage(self):
        return self.get_age() >= Vintage_age

    def __lt__(self, other):
        return self.year < other.year
