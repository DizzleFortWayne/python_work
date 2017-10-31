def describe_pet(pet_name, animal_type='dog'):
	#naming the dog is an act of setting the default paramater animal_type
	# now if no value is named, the function will use the default
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("\nMy " + animal_type + "'s names is " + pet_name.title() + ".")
	
describe_pet(pet_name='willie') 
