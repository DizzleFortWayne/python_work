responses={} ##This is the empty dictionary


#Set a flag to inicate that it is active
polling_active=True

## instantiates loop
while polling_active:
	#prompt for name and response
	name=input("n\What is your name?  ")
	response=input("Which mountain would you like to climb someday?  ")
	
	## Store response in dictionary
	responses[name]=response
	
	#find out if anyone else is going to take the poll
	repeat=input("\nWould you like to let another person respond?  (yes/no) ")
	if repeat=="no":
		polling_active=False
		
#polling is complete show results
print("\n--Poll Results--")
for name, response in responses.items():
	print(name + " would like to climb " + response + "?")
