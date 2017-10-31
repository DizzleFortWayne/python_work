##First you need to open the file to access it

with open('pi_digits.txt') as file_object:
## ----Or to use a relative path---(below)
   #with open("directory/filename.txt') as file_object:
##-----Or absolute path---------
	# filepath='/home/jmcclain/other_files/text_files/filename.txt'
	#with open(filepath) as file_object:

	contents=file_object.read()
	## rstrip() takes the extra line out of the string that python makes
	print(contents.rstrip())

##Optionally you can close a program with close()
###But don't do this until you know what you're doing
