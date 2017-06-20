#Python Crash Course Chapter 7 User Input and While Loops
#multi-line input prompt, while loop with lists and dictionaries are included

#message = input("Tell me something, and I will repeat it back to you: ")
message = "my message"
print("Here is your message: " +message+ ".")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " +name)

#height = int(input("How tall are you in inches? "))
height = 8
if height >= 36:
	print("You're tall enough to ride")
else:
	print("You'll be able to ride when you're a little older.")

#modulus
# number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
# if number % 2 == 0:
# 	print("\nThe number " + str(number) + " is even.")
# else:
# 	print("\nThe number " + str(number) + " is odd.")

#rentalcar = input("What kind of rental car do you like? ")
rentalcar = "Ford"
print("Let me see if I can find you a " +rentalcar+ ".")
#people = int(input("How many people are in your dinner group? "))
people = 10
if people > 8:
	print("You have to wait for a table.")
else:
	print("Table is ready.")

currentnumber = 1
while currentnumber <= 5:
	print(currentnumber)
	currentnumber += 1
prompt2 = "Tell me something, and I will repeat it back to you:"
prompt2 += "\nEnter 'quit' to end the program. "
message = "" #initialize while loop
while message != "quit":
	message = input(prompt2)
	print(message) #correction.  print(message) should be above the message = input(prompt2)
prompt3 = "Actively tell me something, and I will repeat it back to you:"
prompt3 += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt3)
	if message == 'quit':
		active = False
	else:
		print(message)
promptcities = "Please enter the name of a city you have visited:"
promptcities += "\n(Enter \"quit\" when you are finished.) "
while True:
	city = input(promptcities)
	if city == "quit":
		break
	else:
		print("Id love to go to " +city.title()+ "!")
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

while True:
	pizzatopping = input("Enter a pizza topping.  Type quit to exit. ")
	if pizzatopping == "quit":
		break
	else:
		print(pizzatopping+ " is added.")
while True:
	age = int(input("What is the moviegoer's age?  Type 0 to exit. "))
	if age == 0:
		break
	elif age > 0 and age < 3:
		print("Free")
	elif age >= 3 and age <= 12:
		print("$10")
	elif age > 12:
		print("$15")

#moving items from one list to another list
unconfirmedusers = ["Alice","Brian","Candace"]
confirmedusers = []
print(unconfirmedusers)
while unconfirmedusers: #while loop runs unconfirmedusers is not empty
	verifyinguser = unconfirmedusers.pop()
	print("Verifying user or moving unconfirmeduser to confirmeruser " +verifyinguser.title())
	confirmedusers.append(verifyinguser)
print(confirmedusers)
#remove all instances from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
	pets.remove("cat")
print(pets)
#Fill a dictionary with user input
responses = {}
pollingactive = True
while pollingactive:
	name = input("What is your name? ")
	mountain = input("Which mountain do you want to climb someday? ")
	responses[name] = mountain #store name and mountain in responses dictionary
	repeat = input("Do you want to enter another name? y or n ")
	if repeat == "n":
		pollingactive = False
print(responses)
for name, mountain in responses.items():
	print(name+ " wants to climb " +mountain)

sandwichorders = ["pastrami","turkey","roast beef","blt","bbq chicken","tuna"]
finishedsandwiches = []
while sandwichorders:
	makingsandwiches = sandwichorders.pop()
	print("I made your " +makingsandwiches+ " sandwich.")
	finishedsandwiches.append(makingsandwiches)
print(finishedsandwiches)
sandwichorders2 = ["pastrami","turkey","roast beef","blt","pastrami","pastrami","bbq chicken","pastrami","tuna"]
finishedsandwiches2 = []
while sandwichorders2:
	makingsandwiches = sandwichorders2.pop()
	if makingsandwiches == "pastrami":
		print("Out of pastrami")
		continue
	else:
		print("I made your " +makingsandwiches+ " sandwich.")
		finishedsandwiches2.append(makingsandwiches)
print(finishedsandwiches2)
responsesvacation = {}
pollingactive = True
while pollingactive:
	name = input("What is your name? ")
	dreamvacation = input("What dream vacation do you want to visit someday? ")
	responsesvacation[name] = dreamvacation #store name and dream vacation in responsesvacation dictionary
	repeat = input("Do you want to enter another name? y or n ")
	if repeat == "n":
		pollingactive = False
print(responsesvacation)
for name, dreamvacation in responsesvacation.items():
	print(name+ " wants to visit " +dreamvacation)