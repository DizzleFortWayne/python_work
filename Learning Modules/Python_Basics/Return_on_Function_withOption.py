def get_formatted_name(first_name,last_name,middle_name):
	"""return full name, neatly formatted"""
#if there is no middle name don't use it
    if middle_name:
	full_name=first_name +' '+ middle_name + ' ' +last_name
    else:
	full_name=first_name +' ' +last_name
	
	
	return full_name.title()
	
musician=get_formatted_name('david','Roth','lee')
print(musician)

musician=get_formatted_name('Jimi','Hendrix')
print(musician)
