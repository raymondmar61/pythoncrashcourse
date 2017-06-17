#Python Crash Course Chapter 5 If Statements
#for loop, in, not in, are included

cars = ["audi","bmw","subaru","toyota"]
for eachcar in cars:
	if eachcar == "bmw":
		print(eachcar.upper())
	else:
		print(eachcar.title())
requested_toppings = ["mushrooms","onions","pineapple"]
print("mushrooms" in requested_toppings) #print True
print("pepperoni" in requested_toppings) #print False
banned_users = ["andrew","carolina","david"]
user = "marie"
if user not in banned_users:
	print(user.title()+ ", you can post a response if you wish.") #print Marie, you can post a response if you wish.
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
#concise
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" +str(price)+ ".")

#Sometimes it’s important to check all of the conditions of interest. Use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.
requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
	print("Adding mushrooms")
if "pepperoni" in requested_toppings:
	print("Adding pepperoni")
if "extra cheese" in requested_toppings:
	print("Adding extra cheese")
print("Finished making your pizza!")
print("\n")
#RM:  for loop better?!?
istoppings = ["mushrooms","extra cheese","pepperoni"]
for eachrequested_toppings in requested_toppings:
	for eachistoppings in istoppings:
		if eachrequested_toppings in eachistoppings:
			print("Adding " +eachistoppings)
print("Finished making your pizza!")
print("\n")
#RM:  a better for loop
for requested_toppings in requested_toppings:
	if requested_toppings in istoppings:
		print("Adding yummy " +requested_toppings)
print("Finished making your yummy pizza!")
print("\n")


alien_color = "green"
if alien_color == "green":
	points = 5
else:
	points = 10
print("Player earned " +str(points)+ " points.")
alien_color = "red"
if alien_color == "green":
	points = 5
if alien_color == "yellow":
	points = 10
if alien_color == "red":
	points = 10
print("Player earned " +str(points)+ " points.")
alien_color = "yellow"
if alien_color == "green":
	points = 5
elif alien_color == "yellow":
	points = 10
elif alien_color == "red":
	points = 15
print("Player earned " +str(points)+ " points.")

age = 40
if age < 2:
	print("Baby")
elif age < 4:
	print("Toddler")
elif age < 13:
	print("Kid")
elif age < 20:
	print("Teenager")
elif (age >= 20) and (age < 65):
	print("Adult")
elif (age >= 65):
	print("Elder")

favoritefruits = ["kiwi","apple","orange","grapes","melon","blueberries"]
if "apple" in favoritefruits:
	print("I like apple")
if "grapes" in favoritefruits:
	print("I like grapes")
if "banana" in favoritefruits:
	print("I like banana")
if "kiwi" in favoritefruits:
	print("I like kiwi")
if "eggplant" in favoritefruits:
	print("I like eggplant")
print("\n")

requested_toppings = ["mushrooms","green peppers","extra cheese"]
for eachrequested_toppings in requested_toppings:
	if eachrequested_toppings == "green peppers":
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " +eachrequested_toppings+ ".")
print("Finished making your pizza!")
#It’s useful to check whether a list is empty before running a for loop.
#When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.
requested_toppings = ["mushrooms","green peppers","extra cheese"]
if requested_toppings:
	for eachrequested_toppings in requested_toppings:
		if eachrequested_toppings == "green peppers":
			print("Sorry, we are out of green peppers right now.")
		else:
			print("Adding " +eachrequested_toppings+ ".")
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
requested_toppings = []
if requested_toppings:
	for eachrequested_toppings in requested_toppings:
		if eachrequested_toppings == "green peppers":
			print("Sorry, we are out of green peppers right now.")
		else:
			print("Adding " +eachrequested_toppings+ ".")
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza?") #print Are you sure you want a plain pizza?

available_toppings = ["mushrooms", "olives", "green peppers",
"pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_toppings in requested_toppings:
	if requested_toppings in available_toppings:
		print("Adding " +requested_toppings+ ".")
	else:
		print("Sorry, we don't have " +requested_toppings+ ".")
print("Finished making your pizza!")
print("\n")

#usernames = ["admin","Eric","Sammy","George","Buster","Kate"]
usernames = []
if usernames:
	for eachusernames in usernames:
		if eachusernames == "admin":
			print("Hello admin, would you like to see a status report")
		else:
			print("Hello " +eachusernames+ ", thank you for logging in again.")
else:
	print("System is offline")

currentusers = ["ED","Al","Roy","Riza","Eric"]
newusers = ["Becky","AL","Ronny","Ed","Beth","Lewis"]
currentusers = [eachcurrentusers.lower() for eachcurrentusers in currentusers]
print(currentusers)
newusers = [eachnewusers.lower() for eachnewusers in newusers]
print(newusers)
for newusers in newusers:	
	if newusers in currentusers:
		print(newusers+ " is already taken")
	else:
		print(newusers+ " is available")
#I can't figure out how to display initial currentusers and initial newusers lowercase and uppercase in for loop to inform new users username already taken

ordinalnumbers = []
for x in range(1,10):
	ordinalnumbers.append(x)
print(ordinalnumbers)
for eachordinalnumbers in ordinalnumbers:
	if eachordinalnumbers == 1: #in (1) error message
		print(str(eachordinalnumbers)+"st")
	elif eachordinalnumbers in (2, 3):
		print(str(eachordinalnumbers)+"nd")
	else:
		print(str(eachordinalnumbers)+"th")
