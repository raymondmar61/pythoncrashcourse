#Python Crash Course Chapter 4 Working With Lists
#for loop, range(), list(), numbers, tuples are included

magicians = ["alice","david","carolina"]
for eachmagicians in magicians: #eachmagicians is the temporary variable which holds the value in the list magicians
	print(eachmagicians, end=" ") 
	print(eachmagicians.title()+ ", that was a great trick!") #print alice Alice, that was a great trick! 
print("Thank you, everyone.  That was a great magic show!")
print("\n")

pizzas = ["Combo","Pepperoni","Pepperoni & Sausage"]
for eachpizzas in pizzas:
	print("I like " +eachpizzas)
print(pizzas[0]+ " is my all time favorite.")
print(pizzas[1]+ " as long as it's not too oily.")
print("A great combo " +pizzas[2]+ " as long as it's not too oily.")
print("I like to eat pizza!")
print("\n")

for eachvalue in range(1,5):
	print(eachvalue)
numberslist = list(range(1,6))
print(numberslist) #print [1, 2, 3, 4, 5]
evennumberslist = list(range(2, 11, 2))
print(evennumberslist) #print [2, 4, 6, 8, 10]
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares) #print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) #print 0
print(max(digits)) #print 9
print(sum(digits)) #print 45
print("\n")

#A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
squares = [value**2 for value in range(1,11)]
print(squares) #print [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("\n")

players = ["charles", "martina", "michael", "florence", "eli"]
print(players) #print ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #print ['charles', 'martina', 'michael']
print(players[1:4]) #print ['martina', 'michael', 'florence']
print(players[:4]) #print ['charles', 'martina', 'michael', 'florence']
print(players[2:]) #print ['michael', 'florence', 'eli']
print(players[-3:]) #print ['michael', 'florence', 'eli'] #a negative index returns an element a certain distance from the end of a list
print("Here are the first three players on my team:")
for eachplayer in players[0:3]:
	print(eachplayer.title())
print("\n")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #friend_foods = my_foods <-- illegal to copy a list
print("My favorite foods are:")
print(my_foods) #print ['pizza', 'falafel', 'carrot cake']
print("My friend's favorite foods are:")
print(friend_foods) #print ['pizza', 'falafel', 'carrot cake']
print("\n")

slices = ["car","boat","ice cream","dice","book","fan","light"]
print("The first three items in the list are:")
print(slices[0:3]) #print ['car', 'boat', 'ice cream']
print("The middle three items in the list are:")
print(slices[2:5]) #print ['ice cream', 'dice', 'book']
print("The first three items in the list are:")
print(slices[-3:]) #print ['book', 'fan', 'light']
pizzas = ["Combo","Pepperoni","Pepperoni & Sausage"]
friends_pizzas = pizzas[:]
print(pizzas) #print ["Combo","Pepperoni","Pepperoni & Sausage"]
print(friends_pizzas) #print ["Combo","Pepperoni","Pepperoni & Sausage"]
pizzas.append("Bellpepper & Meat")
friends_pizzas.append("Salami & Onion & Sausage")
print(pizzas) #print ['Combo', 'Pepperoni', 'Pepperoni & Sausage', 'Bellpepper & Meat']
print(friends_pizzas) #print ['Combo', 'Pepperoni', 'Pepperoni & Sausage', 'Salami & Onion & Sausage']
print("\n")

#Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
dimensions = (200, 50)
print(dimensions[0]) #print 200
print(dimensions[1]) #print 50
for eachdimensions in dimensions:
	print(eachdimensions)
#You can assign a new value to a variable that holds a tuple.  We redefine the entire tuple:
dimensions = (200, 50)
for eachdimensions in dimensions:
	print(eachdimensions) #print 200\n 50
dimensions = (400, 100)
for eachdimensions in dimensions:
	print("new dimensions" ,eachdimensions) #print new dimensions 400\n new dimensions 100
buffet = ("fried chicken","mixed vegetables","mashed potatoes","bread","ice cream")
for eachbuffet in buffet:
	print(eachbuffet, end=" ")
print(" ")
buffet = ("roast beef","mixed vegetables","mashed potatoes","bread rolls","ice cream")
for eachbuffet in buffet:
	print(eachbuffet, end=" ")