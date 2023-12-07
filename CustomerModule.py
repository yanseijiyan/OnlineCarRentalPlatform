class Customer:
    def __init__(self, name):
        self.name = name

    def rent_car(self, car_rental, rental_mode, num_cars):
        rental_info = None
        if rental_mode == "hourly":
            rental_info = car_rental.rent_hourly(num_cars)
        elif rental_mode == "daily":
            rental_info = car_rental.rent_daily(num_cars)
        elif rental_mode == "weekly":
            rental_info = car_rental.rent_weekly(num_cars)
        return rental_info

    def return_car(self, car_rental, rental_info):
        car_rental.return_car(rental_info)