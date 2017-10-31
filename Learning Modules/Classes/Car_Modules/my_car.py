from car import Car

my_new_car=Car('BMW','535xi',2011)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading=54000
my_new_car.read_odometer()
