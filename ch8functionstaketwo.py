#Python Crash Course Chapter 8 Functions
#function with dictionary, function with while loop, function with for loop, function with lists, modules are included

def greetuser(passvaluename):
	print("Hello, " +passvaluename)
greetuser("Passing name Jesse") #return Hello, Passing name Jesse
greetuser("Passing name Sarah") #return Hello, Passing name Sarah
def describepet(animaltype, petname):
	print("I have a " +animaltype)
	print("My " +animaltype+ "'s name is " +petname.title()+ ".")
describepet("hamster","harry") #return I have a hamster\n My hamster's name is Harry.
describepet("dog","willie") #return I have a dog\n My dog's name is Willie.
describepet(petname="harry",animaltype="hamster") #return I have a hamster\n My hamster's name is Harry.
def describepetdefault(petname, animaltype="cat"): #default value must be last
	print("I have a " +animaltype)
	print("My " +animaltype+ "'s name is " +petname.title()+ ".")
describepetdefault("kat") #return I have a cat\n My cat's name is Kat.
describepetdefault("Billy","bird") #return I have a bird\n My bird's name is Billy.
#default argument must be last because Python interprets default argument as a positional argument.  If the function is called with petname, then petname argument matches up with the first parameter petname in describedefault function's definition
describepetdefault(animaltype="fish", petname="nemo") #return I have a fish\n My fish's name is Nemo.
print("\n")

def makeshirt(text, size="L"):
	print("Your shirt is size " +size+ " saying \"" +text+"\"")
makeshirt(size="L",text="Today is heaven") #return Your shirt is size L saying "Today is heaven"
makeshirt("Keep Cool", "M") #return Your shirt is size M saying "Keep Cool"
makeshirt(text="Keep Cool", size="M") #return Your shirt is size M saying "Keep Cool"
makeshirt("Physical fitness equals happy") #return Your shirt is size L saying "Physical fitness equals happy"
print("\n")

#middle_name argument is optional with an empty default value
def getformattedname(firstname, lastname, middlename=""):
	if middlename: #Python interprets non-empty strings as True
		fullname = firstname+ " " +middlename+ " " +lastname
	else:
		fullname = firstname+ " " +lastname
	return fullname.title()
musician = getformattedname("jimi","hendrix")
print(musician) #print Jimi Hendrix
print(getformattedname("jimi","hendrix")) #print Jimi Hendrix
musician = getformattedname("jimi","hendrix","lee")
print(musician) #print Jimi Lee Hendrix
print(getformattedname("jimi","hendrix","lee")) #print Jimi Lee Hendrix

#return a dictionary
def buildperson(firstname, lastname, age=""):
	person = {"first": firstname, "last": lastname}
	if age: #Python interprets non-empty strings as True
		person["age"] = age #add age to person dictionary
	return person
print(buildperson("jimi","hendrix", age=27)) #print {'first': 'jimi', 'last': 'hendrix', 'age': 27}

#Function with while loop
while True:
	firstname = input("First name (type q to quit) ")
	if firstname == "q":
		break
	lastname = input("Last name (type q to quit) ")
	if lastname == "q":
		break
	print("Hello " +getformattedname(firstname, lastname)+ "!")

def citycountry(city, country):
	return country+ ", " +city
print(citycountry("San Francisco","USA")) #print USA, San Francisco
print(citycountry("London","UK")) #print UK, London
print(citycountry("Tokyo","Japan")) #print Japan, Tokyo
def makealbum(name, title, tracks=""):
	album = {"name": name, "title": title}
	if tracks:
		album["tracks"] = tracks
	return album
print(makealbum("The Beatles","Let It Be", 12)) #print {'tracks': 12, 'name': 'The Beatles', 'title': 'Let It Be'}
print(makealbum("Michael Jackson","Beat It")) #print {'title': 'Beat It', 'name': 'Michael Jackson'}
print(makealbum(title="Jagged Little Pill",tracks=16,name="Alanis Morrisette")) #print {'tracks': 16, 'name': 'Alanis Morrisette', 'title': 'Jagged Little Pill'}
while True:
	name = input("Artist name (type q to quit) ")
	if name == "q":
		break
	title = input("Title ")
	print(makealbum(name, title))
print("\n")

#pass a list to a function
def greetusers(names):
	for eachnames in names:
		print("Hello " +eachnames.title()+ "!")
usernames = ["hannah","ty","margot"]
greetusers(usernames) #return Hello Hannah!\n . . . 

def printmodels(unprinteddesigns, completedmodels):
	while unprinteddesigns:
		currentdesign = unprinteddesigns.pop()
		print("Printing model: " +currentdesign)
		completedmodels.append(currentdesign)
def showcompletedmodels(completedmodels):
	print("The following models have been printed:")
	for eachcompletedmodels in completedmodels:
		print(eachcompletedmodels)
unprinteddesigns = ["iphone case","robot pendant","dodecahedron"]
completedmodels = []
printmodels(unprinteddesigns,completedmodels) #return Printing model: dodecahedron\n Printing model: robot pendant\n Printing model: iphone case
#notice printmodels() sending the two lists unprinteddesigns and completedmodels
print(completedmodels) #print ['dodecahedron', 'robot pendant', 'iphone case']
showcompletedmodels(completedmodels) #return The following models have been printed:\n dodecahedron\n robot pendant\n iphone case
#notice showcompletedmodels() sending the filled list completedmodels which is shown on the print(completedmodels)
print("\n")

#passing the function a copy of the list, not the original. Any changes the function makes to the list will affect only the copy, leaving the original list intact-->functionname(listname[:])
def printmodelscopylist(unprinteddesigns, completedmodels):
	while unprinteddesigns:
		currentdesign = unprinteddesigns.pop()
		print("Printing model: " +currentdesign)
		completedmodels.append(currentdesign)
unprinteddesigns = ["iphone case","robot pendant","dodecahedron"]
completedmodels = []
print(unprinteddesigns) #print ["iphone case","robot pendant","dodecahedron"]
print(completedmodels) #print []
printmodelscopylist(unprinteddesigns[:],completedmodels) #return Printing model: dodecahedron\n Printing model: robot pendant\n Printing model: iphone case\n
print(unprinteddesigns) #print ["iphone case","robot pendant","dodecahedron"]
print(completedmodels) #print ['dodecahedron', 'robot pendant', 'iphone case']

def showmagicians(name):	
	for eachname in name:
		print(eachname)
def makegreat(name):	
	for eachname in name:		
		great = "the Great " +eachname
		greatmagiciannames.append(great)
magiciannames = ["Houdini","Jerry","Secret"]
greatmagiciannames = []
showmagicians(magiciannames)
makegreat(magiciannames)
showmagicians(greatmagiciannames)
print("\n")

def makepizza(size, *toppings): #arbitrary number arguments placed last
	print("Making a " +size+ " pizza with the following toppings:")
	for eachtopping in toppings:
		print("- " +eachtopping) #side note, if no for loop, makepizza() prints results in a tuple
makepizza("small","pepperoni") #return Making a "small" pizza with the following toppings:\n - pepperoni
makepizza("medium","mushrooms","green peppers","extra cheese") #return Making a "medium" pizza with the following toppings:\n - mushrooms\n - green peppers\n - extra cheese
makepizza("large","salami","sausage","pepperoni","bell peppers") #return Making a large pizza with the following toppings:\n- salami\n - sausage\n - pepperoni\n - bell peppers
#functions that accept as many key-value pairs as the calling statement provides
#double asterisks before the parameter **userinfo cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.  Function works no matter how many additional key-value pairs are provided in the function call.
def buildprofile(first, last, **userinfo):
	profile = {}
	profile["firstname"] = first
	profile["lastname"] = last
	for key, value in userinfo.items():
		profile[key] = value
	return profile
print(buildprofile("albert","einstein",location="princeton",field="physics")) #print {'location': 'princeton', 'field': 'physics', 'lastname': 'einstein', 'firstname': 'albert'}
print(buildprofile("Jackie","Chan",hobbies="books, karate, chow mein",favorite_color="red",car="audi")) #print {'lastname': 'Chan', 'firstname': 'Jackie', 'hobbies': 'books, karate, chow mein', 'car': 'audi', 'favorite_color': 'red'}

#storing your functions in a separate file called a module and then importing that module into your main program. An import statement tells Python to make the code in a module available in the currently running program file.

