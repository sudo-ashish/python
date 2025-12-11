class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_car(self):
        return f"{self.model}"

    def get_brand(self):
        return self.__brand

class ElectriceCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def get_ele(self):
        return f"{self.model} {self.battery_size}"



my_car = Car("konigsegg", "sadiar's spear")

# print(my_car.brand)
print(my_car.model)
print(my_car.get_car())

my_EleCar = ElectriceCar("tesla", "y", "4200KW")

print(my_EleCar.get_ele())
print(my_EleCar.get_brand())
