from CarRentalModule import CarRental
from CustomerModule import Customer

def main():
    available_cars = 10
    car_rental = CarRental(available_cars)

    customer_name = input("Enter customer name: ")
    customer = Customer(customer_name)

    while True:
        print("\n1. Display available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            car_rental.display_available_cars()
        elif choice == '2':
            rental_mode = input("Enter rental mode (hourly/daily/weekly): ")
            num_cars = int(input("Enter the number of cars to rent: "))
            customer_rental_info = customer.rent_car(car_rental, rental_mode, num_cars)
        elif choice == '3':
            if 'customer_rental_info' in locals():
                customer.return_car(car_rental, customer_rental_info)
            else:
                print("Error: No rental information available.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()