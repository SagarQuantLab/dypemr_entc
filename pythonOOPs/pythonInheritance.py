class vehicle:

    def __init__(self, year, manufacturer):
        self.year = year
        self.manufacturer = manufacturer

    def getCarDetails(self):
        return self.year, self.manufacturer

class SUV(vehicle):

    def __init__(self, vehicle_name, type_of_fuel, year, manufacturer):
        super().__init__(year, manufacturer)
        # vehicle.__init__(self, year. manufacturer)
        self.vehicle_name = vehicle_name
        self.type_of_fuel = type_of_fuel

class hatchback(SUV):

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
