import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        self.current_speed = max(0, min(self.current_speed, self.maximum_speed))

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled

def main():

    cars = [Car(registration_number=f"ABC-{i}", maximum_speed=random.randint(100, 200)) for i in range(1, 11)]

    while all(car.travelled_distance < 10000 for car in cars):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    print("Race Results:")
    for car in cars:
        print(f"Car {car.registration_number}:")
        print(f"Maximum Speed: {car.maximum_speed} km/h")
        print(f"Final Speed: {car.current_speed} km/h")
        print(f"Travelled Distance: {car.travelled_distance} km\n")
if __name__ == "__main__":
    main()
