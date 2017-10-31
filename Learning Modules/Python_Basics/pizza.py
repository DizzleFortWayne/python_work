##the asterisk* tells python to make an empty tuple	
def make_pizza(size,*toppings):
	"""Print the list of toppings that have been requessted"""
	#Now we loop through the passed parameters
	## We have a positional parameter which is the first passed in
	## all others get packed into the tuple
	print("\nMaking a "+ str(size) + "inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)
	
	
	##The function reponds whether it receives one value or three values
make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')
