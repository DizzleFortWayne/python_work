
def Write_Text(filename):
    print("Please follow the prompts, type 'q'to quit")
    dictionary_0={}
    active=True
    with open(filename,'a') as f_obj:
	    while active:
		    dictionary_0['first_name']=input("What's your first name")
		    if dictionary_0['first_name']=='q':
			    active=False
			    break
		    dictionary_0['last_name']=input("what's your last name?")
		    if dictionary_0['last_name']=='q':
			    active=False
			    break
		    dictionary_0['age']=input("How old are you")
		    if dictionary_0['age']=='q':
			    active=False
			    break
		    f_obj.write(str(dictionary_0)+"\n")


filename="txt_edit_test.txt"
Write_Text(filename)
