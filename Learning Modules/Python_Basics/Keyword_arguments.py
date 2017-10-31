##Keyword arguments are named value pair that you pass to a function
##This frees you from having to correct the ordering
def describe_pet(animal_type, pet_name):
	"""Display Information aabout pet"""
	print("\nI have a "+ animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+ ".")
	
describe_pet(animal_type='hamster', pet_name='harry')


	
