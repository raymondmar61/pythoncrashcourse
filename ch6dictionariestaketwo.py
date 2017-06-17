#Python Crash Course Chapter 6 Dictionaries
#Dictionary is a collect of key-value pairs.  A value can be a number, string, list, or another dictionary . . . any object.
#if else, for loop, sorted, set, nesting are included

alien0 = {"color": "green","points": 5}
print(alien0) #print {'points': 5, 'color': 'green'}
print(alien0["color"]) #print green
print(alien0["points"]) #print 5
alien0["xposition"] = 0
alien0["yposition"] = 25
print(alien0) #print {'color': 'green', 'xposition': 0, 'points': 5, 'yposition': 25}
aliena = {}
aliena["color"] = "greena"
aliena["points"] = 5
print(aliena) #print {'points': 5, 'color': 'greena'}
aliena["color"] = "yellowa"
print(aliena) #print {'points': 5, 'color': 'yellowa'}

alien_0 = {'x_position': 4, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position'])) #print Original x-position: 4
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position'])) #print New x-position: 6
print("\n")

alien0 = {"color": "green","points": 5}
print(alien0) #print {'points': 5, 'color': 'green'}
del alien0["points"]
print(alien0) #print {'color': 'green'}

favoritelanguages = {"jen": "python","sarah": "c","edward": "ruby","phil": "python"}
print(favoritelanguages) #print {'jen': 'python', 'edward': 'ruby', 'phil': 'python', 'sarah': 'c'}
print("Sarah's favorite language is " +favoritelanguages["sarah"]+ ".") #print Sarah's favorite language is c.

person = {"firstname": "Joe", "lastname": "Smith", "age": 45, "city":"San Francisco"}
print(person["firstname"]) #print Joe
print(person["lastname"]) #print Smith
print(person["age"]) #print 45
print(person["city"]) #print San Francisco

user0 = {"username": "efermi", "first": "enrico", "last": "fermi"}
for key, value in user0.items(): #key and value temporary varables pair can be any temporary variables pair
	print("Key: " +key+ " Value: " +value) #print Key: last Value: fermi\n Key: username Value: efermi\n Key: first Value: enrico

favoritelanguages = {"jen": "python","sarah": "c","edward": "ruby","phil": "python"}
for name, language in favoritelanguages.items():
	print(name.title()+ ": " +language) #print Jen: python\n Phil: python\n Edward: ruby\n Sarah: c
#loop all keys only
#The .keys() method returns a list of all the keys
print(favoritelanguages.keys()) #print dict_keys(['jen', 'phil', 'edward', 'sarah'])
for name in favoritelanguages.keys():
	print(name) #print phil\n jen\n sarah\n edward
pythonfriends = ["jen","phil"]
for name in favoritelanguages.keys():
	if name in pythonfriends:
		print(name+" likes to program in " +favoritelanguages[name]+".") #print phil likes to program in python.\n jen likes to program in python.
if "erin" not in favoritelanguages.keys():
	print("Erin, please tell us your favorite language") #print Erin, please tell us your favorite language
for name in sorted(favoritelanguages.keys()): #sorted() function returns keys in order
	print(name.title()+ ", thank you for taking the poll.") #print Edward, thank you for taking the poll.\n Jen, thank you for taking the poll.\n Phil, thank you for taking the poll.\n Sarah, thank you for taking the poll.
#use the values() method to return a list of values without any keys
print("The following languages have been mentioned:")
for language in favoritelanguages.values():
	print(language) #print python\n python\n c\n ruby
print("The following languages have been mentioned no duplicates:")
for language in set(favoritelanguages.values()):
	print(language) #print python\n c\n ruby
print("\n")

pythonglossary = {"ifelifelse": "if then elseif", "variables":"store data", "for loop":"repeat actions","functions":"call code at anytime","list":"store information"}
for key, value in pythonglossary.items():
	print("concept "+key+ " means " +value)
rivers = {"mississippi": "usa", "amazon":"brazil", "zen":"china"}
for river, country in rivers.items():
	print(river+ " runs through " +country)
for river in rivers.keys():
	print(river)
for country in rivers.values():
	print(country)
print("\n")

#print who didn't take the favoritelanguages dictionary poll from list of names
favoritelanguages = {"jen": "python","sarah": "c","edward": "ruby","phil": "python"}
takepoll = ["winnie","sarah","candy","wayne","lisa","spike","phil"]
for eachtakepoll in takepoll:
	if eachtakepoll not in favoritelanguages.keys():
		print(eachtakepoll+ " take the poll.")
	else:
		print(eachtakepoll+ " thank you for taking the poll.")
print("\n")

#nesting
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien) #print {'color': 'green', 'points': 5}\n {'color': 'yellow', 'points': 10}\n {'color': 'red', 'points': 15}
print("\n")
# Make an empty list for storing aliens
aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
#upgrade aliens 0, 1, and 2 to yellow medium 10 points
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
for alien in aliens:
	print(alien)
print("Total number of aliens: " + str(len(aliens)))
print("\n")
#put a list inside a dictionary
pizza = {"crust": "thick","toppings": ["mushrooms", "extra cheese"]}
print("You ordered a " +pizza["crust"]+ "-crust pizza with the following toppings:") #print You ordered a thick-crust pizza with the following toppings:
for eachtoppings in pizza["toppings"]:
	print(eachtoppings, end = " ") #print mushrooms extra cheese
print("\n")
favoritelanguages = {"jen": ["python","ruby"],"sarah": "c","edward": ["ruby","c"],"phil": ["python","haskell","javascript"]}
for name, languages in favoritelanguages.items():
	print(name+"'s favorite languages:")
	print(languages) #prints each name's favorite language in list [] format
	for eachlanguages in languages:
		print("\t" +eachlanguages) #print each name's favorite language not in list [] format
#You should not nest lists and dictionaries too deeply. If you’re nesting items much deeper than what you see in the preceding examples or you’re working with someone else’s code with significant levels of nesting, most likely a simpler way to solve the problem exists.
print("\n")
#a dictionary in a dictionary
users = {"aeinstein": {"first": "albert","last": "einstein","location": "princeton",},
"mcurie": {"first": "marie","last": "curie","location": "paris"}}
for username, userinfo in users.items():
	print("Username: " +username)
	print("Fullname: " +userinfo["first"]+ " " +userinfo["last"]) #It's like working inward to outward or first value of userinfo key
	print("Location: " +userinfo["location"])
print("\n")

person1 = {"firstname": "Joe", "lastname": "Smith", "age": 45, "city":"San Francisco"}
person2 = {"firstname": "Jane", "lastname": "Symth", "age": 54, "city":"San Jose"}
person3 = {"firstname": "Jack", "lastname": "Smithe", "age": 99, "city":"San Mateo"}
personlist = [person1, person2, person3]
print(personlist) #print [{'firstname': 'Joe', 'age': 45, 'city': 'San Francisco', 'lastname': 'Smith'}, {'firstname': 'Jane', 'age': 54, 'city': 'San Jose', 'lastname': 'Symth'}, {'firstname': 'Jack', 'age': 99, 'city': 'San Mateo', 'lastname': 'Smithe'}]
for eachpersonlist in personlist:
	print(eachpersonlist["firstname"]) #print Joe\n Jack\n Jane\n
	print(eachpersonlist["age"]) #print 45\n 99\n 65\n
print("\n")

favoriteplaces = {"bob":"las vegas", "george":"atlanta","rebecca":"hawaii"}
for name, location in favoriteplaces.items():
	print(name+"'s favorite vacation spot is " +location) #bob's favorite vacation spot is las vegas\n rebecca's favorite vacation spot is hawaii\n george's favorite vacation spot is atlanta
print("\n")

favoritenumbers = {"atlee": [5, 7], "mookie": [90, 54, 129], "gene": [74, 75, 97, 1009], "solo": [1]}
for name, favoritenumbers in favoritenumbers.items():
	print(name+"'s favorite numbers:")
	print(favoritenumbers) #print each name's favorite numbers in list [] format
	for eachfavoritenumbers in favoritenumbers:
		print(eachfavoritenumbers) #print each name's favorite numbers not in list [] format
print("\n")

cities = {"springdale": {"country": "usa","population": 3000,"fact": "zion national park",},
"anaheim": {"country": "usa","population": 50000,"fact": "disneyland"},
"london": {"country": "great britian","population": 500000, "fact": "london bridge"}}
for city, information in cities.items():
	print("City: " +city)
	print("Country: " +information["country"]+ " population: " ,information["population"]) #It's like working inward to outward or first value of information key
	print("fact: " +information["fact"])