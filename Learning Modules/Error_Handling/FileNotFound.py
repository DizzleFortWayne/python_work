filename='alice.txt'

try:
	with open(filename) as f_obj:
		contents=f_object.read()
except FileNotFoundError:
	msg="Sorry, the file, " +filename+ " does not exist."
	print(msg)
