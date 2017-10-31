
#accept string input>Write dictionary to file
#Loops thorugh until 'exit is typed

name_0={}

active=True
while active:
	name_0['first']=input("Please enter your first name: ")
	name_0['last']=input("Please enter your last name: ")	
	if name_0['first']=='quit' or name_0['last']=='quit':
		active=False
	else:
		print(name_0)
		filename= 'write_file.txt'
		#appends name to new line
		with open(filename,'a') as file_object:
			file_object.write(str(name_0)+",\n")
