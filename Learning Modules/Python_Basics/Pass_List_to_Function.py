def greet_users(names):
	"""Print a somple greeting to each user in the list"""
	for name in names:
		msg="Hello, " +name.title() +"!"
		print(msg)
###This line defines the list		
usernames=['hannah','ty','margot']
###This line calls the greet users finction and passes the parameters
greet_users(usernames)
