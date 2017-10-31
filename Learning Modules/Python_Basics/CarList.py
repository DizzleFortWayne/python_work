##More with lists
##cars=['tesla', 'ford', 'chevy', 'porsche', 'bmw'] ## Creates list of cars

##cars[0]='subaru' ## this replaces tesla  in the first position

##cars.append('subaru') appends subaru to the end of the list

##cars.insert(0,'nissan') ##.insert() lets you select insertion position

##del cars[0] ##deletes the value in the first position

#print(cars[0].title()) ## Prints first position [0] with title for caps

##Using pop() method in a list
#pop method removes the last item in the list but lets you keep using its value
## This could be good for printing the last car bought if it were in chronological order
##You can also remove an item from ANY position with pop() method
## If you want to remove an item without using it, use del
## If you want to remove an item and temporarily use it, use .pop()

#print(cars)
#popped_car=cars.pop() ##removes last car on list
#first_car=cars.pop(0) ## Removes first car
#second_car=cars.pop(1)## removes second car
#print(cars)

##If you do not know the position, but know the value, you can use the remove() method

##cars.remove('chevy') removes value regardless of position

##you can also remove values assigned to a variable (below) then print the differences
#print(cars)
#too_expensive='porsche'
#cars.remove(too_expensive)
#print(cars)
#print("\nA "+ too_expensive.title() +" is too expensive for me.")

#SORTING LISTS
##.sort() sorts permanently (case sensitive) and cannot be reverted(below)
#cars=['tesla', 'ford', 'chevy', 'porsche', 'bmw'] ## Creates list of cars
#print(cars)
#cars.sort()
#print(cars)

##sorting a list temporarily with the sort() function
cars=['tesla', 'ford', 'chevy', 'porsche', 'bmw'] ## Creates list of cars
len(cars)

