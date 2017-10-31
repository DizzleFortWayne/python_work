## positional parameters/arguments rely on where they are located 
## otherwise they could be backwards or out of place
def describe_pet(animal_type,pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My "+ animal_type + "'s name is "+pet_name.title() +".")

describe_pet('hamster','harry')
describe_pet('Dog','Mojo')