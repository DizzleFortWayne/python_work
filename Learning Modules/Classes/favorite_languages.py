
from collections import OrderedDict
##orderedDict(() prints back and stores in the order added
favorite_languages=OrderedDict()

favorite_languages['justin']='python'
favorite_languages['heidi']='c'
favorite_languages['phoenix']='ruby'
favorite_languages['morgan']='python'
favorite_languages['Karter']='C#'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	    language.title() + ".")
