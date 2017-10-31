
##Flag or a switch to turn off loop
active=True
while active:
	message=input("Tell me something and I'll repeat it, until you say'quit'")	
	if message=='quit':
		active=False
	else:
		print(message)
