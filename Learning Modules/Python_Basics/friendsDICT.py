## working with dictionaries 

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
   }
    
friends=['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("  Hi" +name.title() +
		    " , I see your favorite labguage is " +
		    favorite_languages[name].title() + "!")


##using the keys() method to sort through for a particular person
##favorite_languages={
 ##   'jen':'python',
 ##   'sarah':'c',
 ##   'edward':'ruby',
  ##  'phil':'python',
 ##  }
   
##if 'erin' not in favorite_languages.keys():
##	print("Erin, please take our poll!")
