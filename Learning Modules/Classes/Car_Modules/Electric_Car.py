class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles"""
	def __init__(self,make,model,year):
		"""initialize attributes of the parent class.
		then initialize electric car attributes"""
		
		super().__init__(make,model,year)
		self.battery_size=90
	def describe_battery(self):
		"""Print a statement that describes battery size"""
		print("This car has a " +str(self.battery_size) + " KWH battery.")
		
	    
my_new_car=Car('BMW', '535xi', 2011)
print(my_new_car.get_descriptive_name())
##Child class passing attributes
my_tesla=ElectricCar('Tesla','model s',2016)

##This passes the new miles into my_new_car instance
my_new_car.update_odometer(2600)
my_new_car.read_odometer()
my_new_car.increment_odometer(5000)
my_new_car.read_odometer()

#the calling the child class
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

