##the asterisk* tells python to make an empty tuple	
def make_pizza(*toppings):
	"""Print the list of toppings that have been requessted"""
	#Now we loop through the passed parameters
	print("\nMaking a pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)
	
	
	##The function reponds whether it receives one value or three values
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

