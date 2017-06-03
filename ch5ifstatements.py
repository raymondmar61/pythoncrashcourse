#The loop first checks if the current value of car is 'bmw'.  If it is, the value is printed in uppercase. If the value of car is anything other than 'bmw', it’s printed in title case.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for eachcar in cars:
	if eachcar == "bmw":
		print(eachcar.upper())
	else:
		print(eachcar.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

#You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action. Other times you might be satisfied with just one condition being True. The keywords and and or can help you in these situations.
age0 = 22
age1 = 18
if (age0 >= 21) and (age1 >=21):
	print("Accepted")
else:
	print("Underage")
age1 = 22
if (age0 >= 21) and (age1 >=21):
	print("Accepted")	
else:
	print("Underage")
age0 = 22
age1 = 18
if (age0 >= 21) or (age1 >=21):
	print("An adult is present")
else:
	print("Everyone is under 21")
age0 = 18
if (age0 >= 21) or (age1 >=21):
	print("An adult is present")	
else:
	print("Everyone is under 21")

#Sometimes it’s important to check whether a list contains a certain value before taking an action.  To find out whether a particular value is already in a list, use the keyword in.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings:
	print("Yes, we have mushrooms")
else:
	print("No, we don't have mushrooms")
if "pepperoni" in requested_toppings:
	print("Yes, we have pepperoni")
else:
	print("No we don't have pepperoni")
topping = "pineapple"
if topping in requested_toppings:
	print("Yes, we have " +topping)
else:
	print("No we don't have " +topping)

#Other times, it’s important to know if a value does not appear in a list. You can use the keyword not in this situation.
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title()+ ", you can post a response if you wish.")

#A Boolean expression is just another name for a conditional test. A Boolean value is either True or False.  Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:
game_active = True
can_edit = False
print(game_active) #prints True
print(can_edit) #prints False

#The simplest kind of if statement has one test and one action:
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

#Often, you’ll want to take one action when a conditional test passes and a different action in all other cases. An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

#Often, you’ll need to test more than two possible situations, and to evaluate these you can use Python’s if-elif-else syntax. Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
#Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the if-elif-else chain and then have a simple print statement that runs after the chain has been evaluated:
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" +str(price)+ " today.")
#You can use as many elif blocks in your code as you like.
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10	
else:
	price = 5
print("Your admission cost is $" +str(price)+ " today.")
#The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data. If you have a specific final condition you are testing for, consider using a final elif block and omit the else block.

#However, sometimes it’s important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.  These three independent tests are executed every time this program is run.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.") #pepperoni isn't printed
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")
#In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.

#5-3, 5-4 (88)
#5-5 (89)
alien_color = "green"
if alien_color == "green":
	print("Five points")
else:
	print("Ten points")
alien_color = "yellow"
if alien_color == "green":
	print("Five points")
else:
	print("Ten points")
alien_color = "red"
if alien_color == "green":
	points = 5
elif alien_color == "yellow":
	points = 10
elif alien_color == "red":
	points = 15
print(str(points)+ " points")

#5-6 (89)
age = 17
if age < 2:
	print("Baby")
elif (age >= 2) and (age < 4):
	print("Toddler")
elif (age >= 4) and (age < 13):
	print("Kid")
elif (age >= 13) and (age < 20):
	print("Teenager")
elif (age >= 20) and (age < 65):
	print("Adult")
elif (age >= 65):
	print("Elder")

#5-7 (89)
favoritefruits = ["apples","grapes","oranges","kiwi","honey dew","mango"]
if "apples" in favoritefruits:
	print("You like apples")
if "bananas" in favoritefruits:
	print("You like bananas")
if "plums" in favoritefruits:
	print("You like plums")
if "oranges" in favoritefruits:
	print("You like oranges")
if "grapes" in favoritefruits:
	print("You like grapes")
for eachfavoritefruits in favoritefruits:
	if eachfavoritefruits == ("apples"):
		print("I like " +eachfavoritefruits)						
	if eachfavoritefruits == ("grapes"):
		print("I like " +eachfavoritefruits)
	if eachfavoritefruits == ("oranges"):
		print("I like " +eachfavoritefruits)
	if eachfavoritefruits == ("peaches"):
		print("I like " +eachfavoritefruits)
	if eachfavoritefruits == ("plums"):
		print("I like " +eachfavoritefruits)
	if eachfavoritefruits == ("mango"):
		print("I like " +eachfavoritefruits)
	else:
		print("I don't like (which doesn't work)" +eachfavoritefruits)

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#it’s useful to check whether a list is empty before running a for loop.
#When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.
requested_toppings = []
if requested_toppings  == "True": #personal preference added "True"
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

#The following example defines two lists. The first is a list of available toppings at the pizzeria, and the second is the list of toppings that the user has requested. This time, each item in requested_toppings is checked against the list of available toppings before it’s added to the pizza:
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for eachrequested_topping in requested_toppings:
	if eachrequested_topping in available_toppings:
		print("Adding " + eachrequested_topping + ".")
	else:
		print("Sorry, we don't have " + eachrequested_topping + ".")
print("\nFinished making your pizza!")
#similarily:
favoritefruits = ["apples","grapes","oranges","mango"]
fruits = ["apples","grapes","oranges","kiwi","honey dew","mango","peaches","plums"]
for eachfruit in fruits:
	if eachfruit in favoritefruits:
		print("I like " +eachfruit)						
	else:
		print("I don't like (which work)" +eachfruit)

#5-8 5-9 (93)
#usernames = []
usernames = ["admin","Eric","George","Heather","Rocky"]
if usernames:	
	for eachname in usernames:
		if eachname == "admin":
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " +eachname+ " thank you for logging in again.")
else:
	print("We need to find some users.")

#5-10 (93)
current_users = ["John","eick","wi03","903xe","wxopie","eopq1"]
new_users = ["eick","eixopw","xkoe;x","wkdioel","JOHN","eoplwl"]
[x.lower() for x in current_users]
[y.lower() for y in new_users]
print(current_users)
print(new_users)
for eachnew_users in new_users:	
	if eachnew_users in current_users:
		print(eachnew_users+ " is taken.")
	else:
		print(eachnew_users+ " is available.")		
#doesn't work converting all to lower case.  skipped.  Go back later.

#5-11 (93)
numbers = [1,2,3,4,5,6,7,8,9]
for eachnumber in numbers:
	if eachnumber == 1:
		print("1st")
	elif eachnumber == 2:
		print("2nd")
	elif eachnumber == 3:
		print("3rd")
	else:
		print(str(eachnumber)+"th")