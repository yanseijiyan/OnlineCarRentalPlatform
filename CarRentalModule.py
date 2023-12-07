from datetime import datetime, timedelta

class CarRental:
    def __init__(self, available_cars):
        self.available_cars = available_cars
        self.rentals = []

    def display_available_cars(self):
        print(f"Available cars: {self.available_cars}")

    def rent_hourly(self, num_cars):
        return self._rent("hourly", num_cars)

    def rent_daily(self, num_cars):
        return self._rent("daily", num_cars)

    def rent_weekly(self, num_cars):
        return self._rent("weekly", num_cars)

    def return_car(self, rental_info):
        if rental_info in self.rentals:
            self.rentals.remove(rental_info)
            rented_time = rental_info['rented_time']
            return_time = datetime.now()
            rental_period = return_time - rented_time
            bill = self.calculate_bill(rental_info['rental_mode'], rental_period, rental_info['num_cars'])
            print(f"Car returned successfully. Bill: ${bill}")
        else:
            print("Error: Rental information not found.")

    def _rent(self, rental_mode, num_cars):
        if num_cars > 0 and num_cars <= self.available_cars:
            rented_time = datetime.now()
            rental_info = {'rental_mode': rental_mode, 'num_cars': num_cars, 'rented_time': rented_time}
            self.rentals.append(rental_info)
            self.available_cars -= num_cars
            print(f"Car(s) rented successfully. Enjoy your {rental_mode} rental!")
            return rental_info
        else:
            print("Error: Invalid number of cars requested or insufficient available cars.")
            return None

    def calculate_bill(self, rental_mode, rental_period, num_cars):
        if rental_mode == "hourly":
            return 10 * rental_period.seconds // 3600 * num_cars
        elif rental_mode == "daily":
            return 50 * rental_period.days * num_cars
        elif rental_mode == "weekly":
            return 150 * rental_period.days // 7 * num_cars
        else:
            return 0