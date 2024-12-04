import threading
from random import randint
from time import sleep


class Parking:
    def __init__(self, amount_of_spaces):
        self.amount_of_spaces = amount_of_spaces
        self.amount_of_available_spaces = amount_of_spaces
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def park_car(self, car_number):
        with self.condition:
            if self.amount_of_available_spaces == 0:
                print(f"Машина {car_number} пытается припарковаться, но мест на парковке недостаточно.")
                self.condition.wait()

            if self.amount_of_available_spaces > 0:
                self.amount_of_available_spaces -= 1
                print(f"Машина {car_number} успешно припарковалась.")

    def leave_parking(self, car_number):
        with self.condition:
            self.amount_of_available_spaces += 1
            print(f"Машина {car_number} покинула парковку.")
            self.condition.notify()

def car_run(parking, car_number):
    time_arrive = randint(1, 47)
    time_parking = randint(1, 48 - time_arrive)
    sleep(time_arrive / 2)
    parking.park_car(car_number)
    sleep(time_parking / 2)
    parking.leave_parking(car_number)


threads = []
total_spaces = 10
parking = Parking(total_spaces)
for i in range(20):
    thread = threading.Thread(target=car_run, args=(parking, i + 1, ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

