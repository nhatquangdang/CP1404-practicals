from car import Car
import random
class UnreliableCar(Car):
    price_per_km = 1.23
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0
    def __str__(self):
        """Return a string ofa Car with the fare of distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def total_fare(self):
        """Return the price of the trip."""
        return self.price_per_km * self.current_fare_distance

    def new_fare(self):
        """Start a new fare for driver."""
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        if random.randint(1, 100) < self.reliability:
            self.current_fare_distance += distance_driven
        else:
            pass
        return distance_driven