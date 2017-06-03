alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. You can use any object that you can create in Python as a value in a dictionary.
#In Python, a dictionary is wrapped in braces, {}, with a series of keyvalue pairs inside the braces.  A key-value pair is a set of values associated with each other. When you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
#To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) #returns green
#If a player shoots down this alien, you can look up how many points they should earn using code like this:
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
#Notice that the order of the key-value pairs does not match the order in which we added them. Python doesn’t care about the order in which you store each key-value pair; it cares only about the connection between each key and its value.

#To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line.
#Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generates a large number of key-value pairs automatically.
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

#To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key. For example, consider an alien that changes from green to yellow as a game progresses.
print("The alien is " + alien_0['color'] + ".") #appears no need to assign alien_0['color'] a variable; althought it's easier and convenient
alien_0["color"] = "yellow"
print("The alien's new color is " + alien_0['color'] + ".")

#Use the del statement to completely remove a key-value pair.  All del needs is the name of the dictionary and the key that you want to remove.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0["points"]
print(alien_0)

#You can also use a dictionary to store one kind of information about many objects.
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',} #It’s good practice to include a comma after the last key-value pair as well, so you’re ready to add a new key-value pair on the next line.
name = "sarah"
print(name.title()+ "'s favorite language is " +favorite_languages[name]+ ".")

#6-1(102)
person = {"first_name": "edward", "last_name": "smith", "age": 40, "city": "San Jose",}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

#6-2(102)
favoritenumbers = {"Buster": 28, "Steph": 30, "Chris": 8, "Joe": 8, "Montana": 16,}
print("Buster's favorite number is" ,favoritenumbers["Buster"])
print("Steph's favorite number is" ,favoritenumbers["Steph"])
print("Chris's favorite number is" ,favoritenumbers["Chris"])
print("Joe's favorite number is" ,favoritenumbers["Joe"])
print("Montana's favorite number is" ,favoritenumbers["Montana"])

#6-3(102)
glossary = {"variable": "store a value", "print": "statemente to return a value", "ifthenelse": "a loop", "string": "words", "lists":"store values in one container",}
print("variable: " +glossary["variable"])
print("print: " +glossary["print"])
print("ifthenelse: " +glossary["ifthenelse"])
print("string: " +glossary["string"])
print("lists: " +glossary["lists"])

#You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.
#the glossary dictionary and for loop below is off the top of Raymond's head
glossary = {"variable": "store a value", "print": "statemente to return a value", "ifthenelse": "a loop", "string": "words", "lists":"store values in one container",}
for eachglossary in glossary:
	print(eachglossary+": " +glossary[eachglossary])

#The method items() returns a list of key-value pairs.
#the key-value pairs are not returned in the order in which they were stored, even when looping through a dictionary. Python doesn’t care about the order in which key-value pairs are stored; it tracks only the connections between individual keys and their values.
user_0 = {'username': 'efermi','first': 'enrico','last': 'fermi',}
for key, value in user_0.items(): #This code would work just as well if you had used abbreviations for the variable names: for k, v in user_0.items()
	print("\nKey: " +key)
	print("Value: " +value)
#If you loop through the favorite_languages dictionary, you get the name of each person in the dictionary and their favorite programming language. Because the keys always refer to a person’s name and the value is always a language, we’ll use the variables name and language in the loop instead of key and value.
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
for name, language in favorite_languages.items():
	print(name.title()+ "'s favorite language is " +language+ ".")

#The keys() method is useful when you don’t need to work with all of the values in a dictionary.  In other words, I want the keys only.
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
for name in favorite_languages.keys():
	print(name.title())
#looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote
for name in favorite_languages:
	print(name.title())
#We loop through the names in the dictionary. When the name matches one of our friends, we  display a message about their favorite language.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends: #name == friends doesn't work
		print("   A match " +name.title()+ " and " +favorite_languages[name].title())
#let’s find out if Erin took the poll
#The keys() method isn’t just for looping: It actually returns a list of all the keys.  Code checks if 'erin' is in this list.
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#One way to return items in a certain order is to sort the keys as they’re returned in the for loop. You can use the sorted() function to get a copy of the keys in order
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

#If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a list of values without any keys.
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
#In a poll with a large number of respondents, this can result in a very repetitive list. To see each language chosen without repetition, we can use a set () function.  When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items.
print("The following unique languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

#6-4(108)
glossary = {"variable": "store a value", "print": "statemente to return a value", "ifthenelse": "a loop", "string": "words", "lists":"store values in one container", "dictionary": "lists and values", "set()": "function returns unique values",}
for term, definition in glossary.items():
	print(term+": " +definition)

#6-5(108)
rivers = {"nile": "egypt", "mississippi": "united states","amazon": "brazil",}
for eachriver, country in rivers.items():
	print("The " +eachriver.title()+ " runs through " +country.title()+".")
for rivername in rivers.keys():
	print(rivername)
for countryname in rivers.values():
	print(countryname)

#6-6(108)
favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
peoplelist = ["erica","jake","sarah","winnie","uno","phil"]
for eachpeoplelist in peoplelist:
	print(eachpeoplelist)
	if eachpeoplelist in favorite_languages.keys():
		print("   Thank you " +eachpeoplelist+ " for taking the poll.")
	else:
		print("   "+eachpeoplelist+ " please take the poll.")

#Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. This is called nesting. You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.
#The alien_0 dictionary contains a variety of information about one alien, but it has no room to store information about a second alien.  One way is to make a list of aliens in which each alien is a dictionary of information about that alien.
##We first create three dictionaries, each representing a different alien.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
#We pack each of these dictionaries into a list called aliens.
aliens = [alien_0, alien_1, alien_2]
#We loop through the list and print out each alien.
for eachalien in aliens:
	print(eachalien)

#Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary.  For example, consider how you might describe a pizza that someone is ordering. If you were to use only a list, all you could really store is a list of the pizza’s toppings. With a dictionary, a list of toppings can be just one aspect of the pizza you’re describing.
#In the following example, two kinds of information are stored for each pizza: a type of crust and a list of toppings. The list of toppings is a value associated with the key 'toppings'. To use the items in the list, we give the name of the dictionary and the key 'toppings', as we would any value in the dictionary. Instead of returning a single value, we get a list of toppings:
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'],}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping) #\t is tab
#You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary. In the earlier example of favorite programming languages, if we were to store each person’s responses in a list, people could choose more than one favorite language.
#We use the variable name languages to hold each value from the dictionary, because we know that each value will be a list.  Inside the main dictionary loop, we use another for loop to run through each person’s list of favorite languages.
favorite_languages = {'jen': ['python', 'ruby'],'sarah': ['c'],'edward': ['ruby','go'],'phil': ['python', 'haskell'],}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
#To refine this program even further, you could include an if statement at the beginning of the dictionary’s for loop to see whether each person has more than one favorite language by examining the value of len(languages). If a person has more than one favorite, the output would stay the same. If the person has only one favorite language, you could change the wording to reflect that. For example, you could say Sarah's favorite language is C.

#You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.  For example, if you have several users for a website, each with a unique username, you can use the usernames as the keys in a dictionary. You can then store information about each user by using a dictionary as the value associated with their username.
users = {'aeinstein': {'first': 'albert','last': 'einstein','location': 'princeton',},'mcurie': {'first': 'marie','last': 'curie','location': 'paris',},}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())

#6-7(114)
person1 = {"first_name": "edward", "last_name": "smith", "age": 40, "city": "San Jose",}
person2 = {"first_name": "serena", "last_name": "moon", "age": 16, "city": "tokyo",}
person3 = {"first_name": "brian", "last_name": "jay", "age": 35, "city": "houston",}
people = [person1, person2, person3]
for eachpeople in people:
	print(eachpeople)

#6-8 (115)
snowman = {"animal": "snowman", "owner": "raymond"}
pinky = {"animal": "bear", "owner": "michelle"}
sara = {"animal": "squirrel", "owner": "ian"}
pets = [snowman, pinky, sara]
for eachpets in pets:
	print(eachpets)

#6-9(115)
favorite_places = {"spike": ["las vegas","santa barbara","anaheim"], "jet": ["san francisco","monterey","santa cruz"], "faye": ["new york","britian","washington DC"]}
for name, places in favorite_places.items():
	print("\n"+name+"'s favorite places are the following:")
	for eachplaces in places:
		print("\t" +eachplaces)

#6-10(115)
favoritenumbers = {"Buster": [28, 40], "Steph": [30, 11, 23, 8], "Chris": [8, 10, 12], "Joe": [8, 80, 800], "Montana": [16, 6, 8, 80],}
for eachname, eachnumbers in favoritenumbers.items():
	#print(eachname+ "'s favorite numbers are " ,eachnumbers[eachname]) doesn't work
	print(eachname+ "'s favorite numbers are the following:")
	for eachnumber in eachnumbers:
		print(eachnumber)

#6-11(115)
cities = {"san francisco": {"country":"USA", "population": 1000000,"fact": "golden gate bridge",}, "las vegas": {"country":"USA", "population": 800000,"fact": "casinos",},}
for eachcity, eachcityinfo in cities.items():
	print("\nCity: " +eachcity)
	print("\tCountry: " +eachcityinfo["country"])
	print("\tPopulation:" ,eachcityinfo["population"])
	print("\tFact: " +eachcityinfo["fact"])

#6-12(115)
