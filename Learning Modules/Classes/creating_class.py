class Dog():
	"""A simple attempt to model a dog"""
	
	##The __intit__() method runs automatically every time we
	##create a bew instance of the class
	 
	## "self" is required in method definition
	##and must come first before other parameters
	## this is a reference to the instance
	
	##Defining three separate methods within a class
	
	def __init__(self,name,age):
		"""Initialize name and attributes"""
		self.name=name
		self.age=age
		#since these don't need additional information, we just have 
		#one parameter, self
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(self.name.title() + " rolled over!")

##Very important that you capitalize class names and 
#-instances of class names like Dog instead of dog

#my_dog is an instance of dog
my_dog=Dog('mojo',12)
##The .name and .age are attributes of the instance
#This is how python finds the attribute
print("My dog's name is " +my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

##after creating an instance of dog, "my_dog" now we can call any method
#-in the dog class(below)

my_dog.sit()
my_dog.roll_over()
## here we use another instance
your_dog=Dog('sticker',12)
##Now she obeys the same methods
your_dog.sit()
your_dog.roll_over()
