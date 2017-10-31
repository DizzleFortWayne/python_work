filename='write_file.txt'


#W is the "Write" mode
#a is the "append" mode
with open(filename, 'W') as file_object:
	file_object.write("I love programming.")
	
