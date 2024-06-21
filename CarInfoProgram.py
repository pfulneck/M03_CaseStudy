'''
M03 Lab - Case Study: Lists, Functions, and Classes
'''

# defining parent Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# defining Automobile class that inherits attributes from Vehicle class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type) # call superclass constructor to call in vehicle_type

        # initializing attributes for Autombile Class
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    # displaying auto info
    def display_info(self):
        print('Vehicle Type: ', self.vehicle_type)
        print('Year: ', self.year)
        print('Make: ', self.make)
        print('Model: ', self.model)
        print('Number of doors: ', self.doors)
        print('Type of roof: ', self.roof)

# function for collecting the car data from the user
def collect_car_data():
    vehicle_type = 'car'
    year = input('Enter the year of the car: ')
    make = input('Enter the make of the car: ')
    model = input('Enter the model of the car: ')
    doors = input('Enter the number of doors (2 or 4): ')
    roof = input('Enter the type of roof (solid, sun roof, convertable): ')

    # created an Automobile object with user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    return car

# main function to run the program
def main():
    print('Welcome the Car info App')
    car = collect_car_data()
    if car:
        print('\nHere is the information you entered:')
        car.display_info()
    else:
        print('Failed to collect car data.')

# entry point of the program
if __name__ == '__main__':
    main()