
number=input("\nEnter a number, and I'll tell you even, or odd! \nPress 0 to quit")
number=int(number)
if number==0:
	print("Um, I said a number")
if number %2==0:
	print("\nThe Number " + str(number) +" is even")
else:
	print("\nThe Number " + str(number) +" is Odd")

	
