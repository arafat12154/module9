class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):

        self.current_speed += change


        self.current_speed = max(0, min(self.current_speed, self.maximum_speed))


def main():

    new_car = Car(registration_number="ABC-123", maximum_speed=142)
    new_car.accelerate(30)
    print("Current Speed after +30 km/h:", new_car.current_speed, "km/h")

    new_car.accelerate(70)
    print("Current Speed after +70 km/h:", new_car.current_speed, "km/h")

    new_car.accelerate(50)
    print("Current Speed after +50 km/h:", new_car.current_speed, "km/h")

    new_car.accelerate(-200)
    print("Final Speed after emergency brake:", new_car.current_speed, "km/h")
if __name__ == "__main__":
    main()