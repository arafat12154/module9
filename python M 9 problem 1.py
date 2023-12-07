class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
def main():
    new_car = Car(registration_number="ABC-123", maximum_speed=142)
    print("Registration Number:", new_car.registration_number)
    print("Maximum Speed:", new_car.maximum_speed, "km/h")
    print("Current Speed:", new_car.current_speed, "km/h")
    print("Travelled Distance:", new_car.travelled_distance, "km")
if __name__ == "__main__":
    main()