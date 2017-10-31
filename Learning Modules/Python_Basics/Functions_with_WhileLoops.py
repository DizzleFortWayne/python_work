

##defining your function

def get_formatted_name(first_name,last_name):
	"""return a full name, neatly formatted"""
	full_name=first_name+ ' ' +last_name
	return full_name.title()
	
#using a loop to call a function and 
#pass the first and last name arguments
while True:
	print ("\nPlease tell me your name")
	print("(enter 'quit' at any time to quit")
	
	f_name=input("First Name:  ")
	if f_name=='quit':
		break
	l_name=input("Last Name:  ")
	if f_name=='quit':
		break
	formatted_name=get_formatted_name(f_name,l_name)
	print("\nHello, "+formatted_name+ "!")
	
