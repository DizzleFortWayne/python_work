## builds your function, provides variables
## when you call it you pass a parameter and it provides
## output from the return

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name=first_name+' '+last_name
	return full_name.title()

##musician variable takes the values retured from the function
## the input jimi and hendrix goes into finction
## gets concatenated and formated by title()
##then returned
musician=get_formatted_name('jimi','hendrix')
print(musician)
