class BMW:
    def start_engine(self):
        print("BMW engine is designed to run smoothly!")

    def drive(self):
        print("Driving the BMW... smooth performance.")

class Ferrari:
    def start_engine(self):
        print("Ferrari engine designed for rough drives!")

    def drive(self):
        print("Driving the Ferrari... aggressive ride.")

def test_drive(car):
    car.start_engine()
    car.drive()

bmw_car = BMW()
ferrari_car = Ferrari()

cars = [bmw_car, ferrari_car]
for car in cars:
    test_drive(car)
