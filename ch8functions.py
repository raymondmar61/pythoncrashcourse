def greet_user():
	print("Hello!")
#greet_user() function has one job: print("Hello!")
greet_user()

#Passing Information to a Function
#jesse is the argument. username is the parameter. Note People sometimes speak of arguments and parameters interchangeably
def greet_user(username):
	print("Hello, " +username+ "!")
	print("Hello, " +username.title()+ "!")
greet_user("jesse")

#8-1 (135)
def display_message():
	print("I'm learning functions.")
display_message()

#8-2 (135)
def favorite_book(title):
	print("One of my favorite books is " +title.title()+ ".")
favorite_book("Steve Jobs")

#a function call may need multiple arguments.  You can use positional arguments, which need to be in the same order the parameters were written; keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.

#Positional Arguments
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
#Multiple Function Calls
#You can call a function as many times as needed. Describing a second, different pet requires just one more call to describe_pet():
describe_pet('dog', 'willie')

#Keyword Arguments
#A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument.  Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
describe_pet(animal_type='cat', pet_name='dawn')
describe_pet(pet_name='dawn', animal_type='cat')

#Default Values
#You can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.
#non-default argument must be first or default argument must not be first
def describe_pet(pet_name, animal_type='dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='doug default animal_type dog')
describe_pet("ronnie","fish")

#8-3 (141)
def make_shirt(size, message):
	print("Size: " +size+ " Message: " +message)
make_shirt("large","abc123")
make_shirt(message="123abc",size="medium")

#8-4 (141)
def make_largeshirt(message, size="large"):
	print("Size: " +size+ " Message: " +message)
make_largeshirt("I love Python.")
make_largeshirt("I love Python.", "medium") #prints size medium
make_largeshirt("chocolate.", "small") #prints size small message chocolate

#8-5 (141)
def describe_city(city, country="USA"):
	print(city+ " is in " +country)
describe_city("San Francisco")	
describe_city("London", "England")	
describe_city(country="Canada",city="Vancouver")

#Return Values
#A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print(get_formatted_name('janis', 'joplin'))
#To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value.
def get_formatted_name(first_name, last_name, middle_name=''):
	#Python interprets non-empty strings as True, so if middle_name evaluates to True if a middle name argument is in the function call
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#If we’re using a middle name, we have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
print("\n")

#Returning a Dictionary
#the following function takes in parts of a name and returns a dictionary representing a person
def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)
#You can easily extend this function to accept optional values like an age
def build_person(first_name, last_name, age=""):
	person = {'first': first_name, 'last': last_name}
	if age:
		person["age"] = age
	return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

#8-6 (146)
def city_country(city, country):
	print(city+ ", " +country)
city_country("Paris","France")
city_country("Budapest","Romania")
city_country("Tokyo","Japan")

#8-7 (146)
def make_album(artist, title, tracks=""):
	album = {"Artist": artist, "Title": title}
	#if tracks is non-empty, it's true, it's true when there's a value
	#add tracks to the dictionary
	if tracks:
		album["tracks"] = tracks
	return album
#both ways to print the dictionary album work
print(make_album("The Beatles","Let It Be"))
print("\n")
music = make_album("The Beatles","Let It Be", 12)
print(music)

#8-8 (146)
while True:
	print("\nPlease enter an album.  Enter q to quit")
	artist = input("Artist: ")
	if artist == "q":
		break
	title = input("Title: ")
	if title == "q":
		break
	print(make_album(artist, title))

#Passing a List
#When you pass a list to a function, the function gets direct access to the contents of the list.
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print("\n")

#Modifying a List in a Function
#When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are permanent, allowing you to work efficiently even when you’re dealing with large amounts of data.
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Simulate creating a 3D print from the design.
	print("Printing model: " + current_design)
	completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)
print("\n")	
#We can reorganize this code by writing two functions, each of which does one specific job. Most of the code won’t change; we’re just making it more efficient. The first function will handle printing the designs, and the second will summarize the prints that have been made:
#print_models() function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)
#show_completed_models() function displays the name of each model that was printed		
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
#We set up a list of unprinted designs and an empty list that will hold the completed models. Then, because we’ve already defined our two functions, all we have to do is call them and pass them the right arguments. We call print_models() and pass it the two lists it needs; as expected, print_models() simulates printing the designs. Then we call show_completed_models() and pass it the list of completed models so it can report the models that have been printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#This example also demonstrates the idea that every function should have one specific job. The first function prints each design, and the second displays the completed models. This is more beneficial than using one function to do both jobs.
#Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.

#you can pass a function to copy a list to another list. Any changes the function makes to the list will affect only the copy, leaving the original list intact. You can send a copy of a list to a function like this: function_name(list_name[:])  The slice notation [:] makes a copy of the list to send to the function.  e.g. print_models(unprinted_designs[:], completed_models)

#8-9 (150)
magicians = ["alpha","bravo","charlie","delta"]
def show_magicians(names):
	for eachname in names:
		print("Welcome magician " +eachname.title())
show_magicians(magicians)		

#8-10 (150)
def appendgreatmagicians(magicians, greatmagicians):
	while magicians:
		current_magicians = magicians.pop()
		print("Printing magician: " + current_magicians)
		greatmagicians.append("The Great " +current_magicians)
		#greatmagicians.append("The Great " +magicians) <-- error message.  Must have the three lines above with print() optional.
def make_great(greatmagicians):
	print("\nThe following magicians are great:")
	for eachgreatmagicians in greatmagicians:
		print(eachgreatmagicians)
magicians = ["alpha","bravo","charlie","delta"]
greatmagicians = []
appendgreatmagicians(magicians, greatmagicians)
make_great(greatmagicians)

#8-11 (150)

#Passing an Arbitrary Number of Arguments
#Python allows a function to collect an arbitrary number of arguments from the calling statement
#The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple.
#If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
def make_pizza(size, *toppings):
	print("\nMaking a " +str(size)+ "-inch pizza with the following toppings:")
	for eachtopping in toppings:
		print("-" +eachtopping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword Arguments
#Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides.
#The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.
def build_profile(first, last, **user_info):
	#In the body of build_profile(), we make an empty dictionary called profile to hold the user’s profile.
	profile = {}
	#add the first and last names to this dictionary because we’ll always receive these two pieces of information from the user.
	profile['first_name'] = first
	profile['last_name'] = last
	#we loop through the additional key-value pairs in the dictionary user_info and add each pair to the profile dictionary
	for key, value in user_info.items():
		profile[key] = value
	return profile
#call build_profile(), passing it the first name 'albert', the last name 'einstein', and the two key-value pairs location='princeton' and field='physics'. We store the returned profile in user_profile and print user_profile	
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

#8-12 (154)
def sandwiches(*items):
	print(items)
sandwiches("lettice","tomato","ham")	
sandwiches("lettice","tomato","turkey","bacon")	
sandwiches("lettice","tomato","onion","cheese","roast beef")	

#8-13 (154)
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('Raymond', 'Mar', location='San Jose', field='economics', hobbies = 'gym, music, books, cook')
print(user_profile)

#8-14 (154)
def make_car(manufacturer, modelname, **keywords):
	auto = {}
	auto["manufacturer"] = manufacturer
	auto["modelname"] = modelname
	for key, value in keywords.items():
		auto[key] = value
	return auto
car = make_car("subaru","outback", color="blue", tow_package=True)
print(car)

#Storing Your Functions in Modules
#You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. An import statement tells Python to make the code in a module available in the currently running program file.  There are several ways to import a module, and I’ll show you each of these briefly.

#Importing an Entire Module
#The line import ch8functionspizza tells Python to open the file ch8functionspizza.py and copy all the functions from it into this program. You don’t actually see code being copied between files because Python copies the code behind the scenes as the program runs. All you need to know is that any function defined in ch8functionspizza.py will now be available.
#Below imports the module we just created and then makes two calls to make_pizza():
import ch8functionspizza
#To call a function from an imported module, enter the name of the module you imported, ch8functionspizza, followed by the name of the function, make_pizza(), separated by a dot
ch8functionspizza.make_pizza(16, "pepperoni","sausage")
ch8functionspizza.make_pizza(12, "mushrooms","green peppers","salami")

#Importing Specific Functions
#You can also import a specific function from a module. Here’s the general syntax for this approach: from module_name import function_name.  You can import as many functions as you want from a module by separating each function’s name with a comma: from module_name import function_0, function_1, function_2
#With this syntax, you don’t need to use the dot notation when you call a function. Because we’ve explicitly imported the function make_pizza() in the import statement, we can call it by name when we use the function.
from ch8functionspizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Function an Alias
#If the name of a function you’re importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias.  You’ll give the function this special nickname when you import the function.  The general syntax for providing an alias is: from module_name import function_name as fn
#Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as keyword renames a function using the alias you provide:
from ch8functionspizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using as to Give a Module an Alias
#You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module’s functions more quickly.
#The general syntax for this approach is: import module_name as mn
#Calling p.ch8functionspizza() is more concise than calling ch8functionspizza.make_pizza():
import ch8functionspizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Importing All Functions in a Module
#You can tell Python to import every function in a module by using the asterisk (*) operator.
#The syntax is the following: from module_name import *
#The asterisk in the import statement tells Python to copy every function from the module ch8functionspizza into this program file. Because every function is imported, you can call each function by name without using the dot notation. However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get some unexpected results.
from ch8functionspizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#8-15 (159)

#8-16 (159)
import ch8functionsmagicians
magicians = ["alpha","bravo","charlie","delta"]
ch8functionsmagicians.show_magicians(magicians)
print("\nfrom module_name import function_name")
from ch8functionsmagicians import show_magicians
show_magicians(magicians)
print("\nfrom module_name import function_name as fn")
from ch8functionsmagicians import show_magicians as sm
sm(magicians)
print("\nimport module_name as mn")
import ch8functionsmagicians as ch8magic
ch8magic.show_magicians(magicians)
print("\nfrom module_name import *")
from ch8functionsmagicians import *
show_magicians(magicians)

#8-17 (159)