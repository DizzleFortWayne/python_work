#start with users that need to be verified and empty list
unconfirmed_users=['alice', 'brian', 'candace']
confirmed_users=[]

#verify each user until there is no unconfirmed users
#move each verified user into confirmed users

while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	
	print("The floowing users were unconfirmed...Verifying user: " +current_user.title())
	confirmed_users.append(current_user)
	##The method pop() removes and returns last object or obj from the list.
	
#DISPLAY all confirmed users
print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

