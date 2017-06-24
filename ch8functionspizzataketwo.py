def makepizza(size, *toppings): #arbitrary number arguments placed last
	print("Making a " +size+ " pizza with the following toppings:")
	for eachtopping in toppings:
		print("- " +eachtopping) #side note, if no for loop, makepizza() prints results in a tuple