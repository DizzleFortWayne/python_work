def print_models(unprinted_designs,completed_models):
	"""
	#simulated printing each design, until none are left
	# move each design to completed_models after printing"""
	while unprinted_designs:
		current_design=unprinted_designs.pop()
		#simulate creating a 3d print from design
		print("Printing Model: " +current_design)
		completed_models.append(current_design)
		
def show_completed_models(completed_models):
	"""Show all the models that were printed"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		##this could be condfusing
		##saying print EACH model
		print(completed_model)
		
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)



