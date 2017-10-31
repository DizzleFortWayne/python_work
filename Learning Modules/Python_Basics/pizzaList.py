
available_toppings=['mushrooms', 'pepperoni','olives',
					'green_peppers','pineapple','extra_cheese']

requested_toppings=['mushrooms','french_fries','extra_cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+ requested_topping+ ".")
	else:
		print("Sorry we don't have "+requested_topping+".")
	
print("\nFinished making your pizza!")
