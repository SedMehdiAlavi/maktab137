from logging import exception


class Car :

    def __init__(self , car_id : str , model: str , year: int ,
                 is_available: bool = True):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.is_available = is_available


    def rent_car(self):
        if self.is_available:
            self.is_available = False


    def return_car(self):
        if not self.is_available :
            self.is_available = True

    def display_info (self) :
        print(f"{self.car_id}: {self.model}, {self.year}, {self.is_available}")

bmw = Car("1" , "bmw x4" , 2016 , True)
benz = Car("2" , "benz g3" , 2017 , True)

class RentalAgency:

    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def find_car(self, id):
        for car in self.cars:
            if car.car_id == id:
                car.display_info()


    def rent_car(self, car):
        if car.is_available:
            car.is_available = False
        else:
            raise ValueError(f"{car} not found")

    def display_available_cars(self):
        sorted_cars = sorted(self.cars, key=lambda car: car.car_id)
        for car in sorted_cars:
            if car.is_available:
                car.display_info()

ferdos = RentalAgency()
ferdos.add_car(bmw)
ferdos.add_car(benz)
ferdos.find_car("1")
ferdos.rent_car(bmw)
