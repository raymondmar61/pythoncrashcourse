# You’ll often want to run through all entries in a list, performing the same task with each item.  When you want to do the same action with every item in a list, you can use Python’s for loop.
#keep in mind that the set of steps is repeated once for each item in the list, no matter how many items are in the list. If you have a million items in your list, Python repeats these steps a million times—and usually very quickly.
#when writing your own for loops that you can choose any name you want for the temporary variable that holds each value in the list.

magicians = ['alice', 'david', 'carolina']
for eachmagician in magicians: #pull a name from the list magicians, and store it in the variable eachmagician.
	print(eachmagician) #“For every magician in the list of magicians, print the magician’s name.”
	print(eachmagician.title()+ ", that was a great trick!")
	print("I can't wait to see your next trick, " +eachmagician.title()+ ".\n")
print("The for loop is completed.  The last magician from the loop is " +eachmagician.title()+ ".  Thank you, everyone.  That was a great magic show!\n")

#4-1(60)
pizza = ["pepperoni","combo","sausage"]
for eachpizza in pizza:
	print("I like " +eachpizza+ " pizza!")
print("I really love pizza!\n")
#4-2(60)
animals = ["shark","tiger","bear"]
for eachanimals in animals:
	print("A " +eachanimals+ " can be a good animal.")
print("These animals are strong!\n")

#Python’s range() function makes it easy to generate a series of numbers.  The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.  range(x,y-1)
for value in range(1,6):
	print(value)
#If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.
numbers = list(range(1,6))
print(numbers)
#We can also use the range() function to tell Python to skip numbers in a given range.
evennumbers = list(range(2,11,2))
print(evennumbers)
#Here’s how you might put the first 10 square numbers into a list:
squares = []
for eachvalue in range(1, 11):
	square = eachvalue ** 2
	squares.append(square)
	#faster combine the two lines to one:  squares.append(eachvalue ** 2)
print(squares)
#min(), max(), sum()
digits = []
for eachdigit in range(0,10):
	digits.append(eachdigit)
print(min(digits))
print(max(digits))
print(sum(digits))

#A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
squares2 = [eachvalue**2 for eachvalue in range(1,11)]
print(squares2) #prints squares2 as one list
#To use the syntax above, begin with a descriptive name for the list, such as squares2. Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. The for loop in this example is for value in range(1,11), which feeds the values 1 through 10 into the expression value**2. Notice that no colon is used at the end of the for statement.

#4-3(64)
for eachnumber in range(1,21):
	print(eachnumber)

#4-4(64)
# million = []
# for eachnumber in range(1,1000001):
# 	million.append(eachnumber)
# print(million)
#4-5(64)
million2 = []
for eachnumber in range(1,1000001):
	million2.append(eachnumber)
print(min(million2))	
print(max(million2))	
print(sum(million2))
#4-6(64)
for eachoddnumber in range(1,20,2):
	print(eachoddnumber)
#4-7(64)
threes = []
for eachmultiplethird in range(3,31,3):
	threes.append(eachmultiplethird)
print(threes)
#4-8(64)
cubes = []
for eachcube in range(1,11):
	cubes.append(eachcube**3)
print(cubes)	
#4-9(64)
cubes2 = [eachvalue**3 for eachvalue in range(1,11)]
print(cubes2)

#You can also work with a specific group of items in a list, which Python calls a slice.  To make a slice, you specify the index of the first and last elements you want to work with.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #prints charles 0, martina 1, michale 2
print(players[1:4]) #prints martina 1, michael 2, florence 3
print(players[:4]) #prints charles 0, martina 1, michael 2, florence 3
print(players[2:]) #michael 2, florence 3, eli 4
#Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can output any slice from the end of a list.
print(players[-3:]) #eli, florence, michael
print("Here are the first three players on my team:")
for eachplayer in players[:3]:
	print(eachplayer.title())

#To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
print("My favorite foods are: ", my_foods)
print("My friend's favorite foods copying me are: ", friends_foods)
#To prove that we actually have two separate lists, we’ll add a new food to each list and show that each list keeps track of the appropriate person’s favorite foods:
my_foods.append("cannoli")
friends_foods.append("ice cream")
print(my_foods)
print(friends_foods)
#If we had simply set friend_foods equal to my_foods, we would not produce two separate lists.
#The equal  tells Python to connect the new variable friend_foods to the list that is already contained in my_foods, so now both variables point to the same list. As a result, when we add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods.

#4-10(69)
cubes = []
for eachcube in range(1,11):
	cubes.append(eachcube**3)
print(cubes)
print("The first three items are " ,cubes[0:3])
print("The middle items are " ,cubes[4:7])
print("The last three items are " ,cubes[-3:])
#4-11(69)
pizza = ["pepperoni","combo","sausage"]
friends_pizza = pizza[:]
pizza.append("artisan")
friends_pizza.append("bbq")
for eachpizza in pizza:
	print(eachpizza)
for eachpizza in friends_pizza:	
	print(eachpizza)
#4-12(69)
my_foods = ['pizza', 'falafel', 'carrot cake']
for eachfood in my_foods:
	print(eachfood)

#sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
#A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 #error message, can't change dimensions[0]
for eachdimension in dimensions:
	print(eachdimension)
#you can assign a new value to a variable that holds a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple.
dimensions = (200, 50)
for eachdimension in dimensions:
	print("Original dimension: " ,eachdimension)
dimensions = (400, 100)
for eachdimension in dimensions:
	print("New dimension: " ,eachdimension)

#4-13(71)
buffet = ("mashed potatoes","steamed vegetables","fried chicken","salad","corn bread")
for eachbuffet in buffet:
	print(eachbuffet)
buffet = ("mashed potatoes","steamed vegetables","ham","salad","chicken soup")
for eachbuffet in buffet:
	print(eachbuffet)