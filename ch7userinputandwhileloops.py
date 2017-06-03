#The input() function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it stores it in a variable to make it convenient for you to work with.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#You can store your prompt in a variable and pass that variable to the input() function. This allows you to build your prompt over several lines, then write a clean input() statement.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

#Use the input as a number, use the int() function, which tells Python to treat the input as a numerical value. The int() function converts a string representation of a number to a numerical representation.
age = int(input("What's youre age? "))
print("You're age is" ,age)
#or use the int() function in another line
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

#The modulo operator (%), which divides one number by another number and returns the remainder
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")

#FYI If you’re using Python 2.7, you should use the raw_input() function when prompting for user input. This function interprets all input as a string, just as input() does in Python 3.

#7-1(121)
rentalcar = input("What kind of rental car do you want? ")
print("Let me see if I can find a " +rentalcar+".")

#7-2(121)
partyof = int(input("How many are in the dinner group? "))
if partyof > 8:
	print("You need to wait for a table.")
else:
	print("Table is ready.")

#7-3(121)
divisblebyten = int(input("A number "))
if divisblebyten % 10 == 0:
	print(divisblebyten, "is divisible by 10.")
else:
	print(divisblebyten, "is not divisible by 10.")

#The for loop takes a collection of items and executes a block of code once for each item in the collection.
#In contrast, the while loop runs as long as, or while, a certain condition is true.
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1
#We’ll define a quit value and then keep the program running as long as the user has not entered the quit value
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt) #prompt is from the prompt variable defined above
	#This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:
	if message != "quit":
		print(message)

#What about more complicated programs in which many different events could cause the program to stop running? For example, in a game, several different events can end the game. When the player runs out of ships, their time runs out, or the cities they were supposed to protect are all destroyed, the game should end.
#For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True #active variable is the flag
while active:
	message = input(prompt)
	if message == 'quit': #if user enters quit, set active to False, while loop stops
		active = False
	else:
		print(message)
#now that we have a flag to indicate whether the overall program is in an active state, it would be easy to add more tests (such as elif statements) for events that should cause active to become False.

#To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement. The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only executes code that you want it to, when you want it to.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
#A loop that starts with while True runs forever unless it reaches a break statement.
while True:
	city = input(prompt)
	if city == 'quit': #When they enter 'quit', the break statement runs, causing Python to exit the loop
		break
	else:
		print("I'd love to go to " + city.title() + "!")
#FYI You can use the break statement in any of Python’s loops. For example, you could use break to quit a for loop that’s working through a list or a dictionary.

#Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue #If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the rest of the loop and return to the beginning.
	print(current_number) #If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.

#7-4(127)
while True:
	pizzatoppings = input("Enter a pizza topping.  Type quit when finished. ")	
	if pizzatoppings == "quit":
		break
	else:
		print("I add " +pizzatoppings+ " to your pizza.")

#7-5(127)
age = ""
while age != 100:
	age = int(input("How old is the movie goer? Enter when finished. "))
	if age < 3:
		print("$0.00")
	elif age >= 3 and age <=12:
		print("$10.00")
	else:
		print("$15.00")
#7-6(128)		
#7-7(128)

#To keep track of many users and pieces of information inputted from the user, we’ll need to use lists and dictionaries with our while loops.  Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

#moving items from one list to another
# Start with users that need to be verified, and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users: #The while loop runs as long as the list unconfirmed_users is not empty.
	current_user = unconfirmed_users.pop() #pop() function removes unverified users one at a time from the end of unconfirmed_users.
	#Here, because Candace is last in the unconfirmed_users list, her name will be the first to be removed, stored in current_user, and added to the confirmed_users list. Next is Brian, then Alice.
		print("Verifying user: " + current_user.title())
		confirmed_users.append(current_user)
#When the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#The remove() function removes an item in a list only once. What if you want to remove all instances of a value from a list?  To remove all instances of that value, you can run a while loop until 'cat' is no longer in the list.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: #Python enters the while loop because it finds the value 'cat' in the list.  It removes each instance of 'cat' until the value is no longer in the list, at which point Python exits the loop.
	pets.remove('cat')
print(pets)

#Filling a Dictionary with User Input
#Let’s make a polling program in which each pass through the loop prompts for the participant’s name and response. We’ll store the data we gather in a dictionary.
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ") #This is the key.
	response = input("Which mountain would you like to climb someday? ")
	# Store the response in the dictionary.  This is the value.:
	responses[name] = response
	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

#7-8(131)
sandwich_orders = ["turkey","blt","ham","roast beef"]
finished_sandwiches = []
while sandwich_orders:
	making_sandwiches = sandwich_orders.pop()
	print("I'm making your " +making_sandwiches+ " sandwich.")
	finished_sandwiches.append(making_sandwiches)
print("\nThe following sandwiches are made:")	
for eachfinished_sandwiches in finished_sandwiches:
	print(eachfinished_sandwiches)

#7-9(131)
sandwich_orders = ["turkey","pastrami","blt","pastrami","ham","roast beef","pastrami",]
print(sandwich_orders)
while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")
print(sandwich_orders)

#7-10(131)
responses = {}
polling_active = True
while polling_active:
	name = input("What's your name? ")
	place = input("If you could visit one place in the world, where would you go?")
	responses[name] = place
	repeat = input("Do you want another person to response? (yes/no) ")
	if repeat == "no":
		polling_active = False
print("\nThe one place results are below")
for key, value in responses.items():
	print(key+ " wants to visit " +value+".")