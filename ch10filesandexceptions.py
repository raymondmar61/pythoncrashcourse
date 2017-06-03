#open and prints pi_digits.txt containing 30 digits pi as is
#open('pi_digits.txt') returns an object representing pi_digits.txt. Python stores this object in file_object
#The keyword with closes the file once access to it is no longer needed.
#The read() method reads the entire contents of the file and store it as one long string in contents
with open("pi_digits.txt") as file_object:
	contents = file_object.read()
	print(contents)
#To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.  Absolute or relative is valid.
with open("/home/mar/Python/alphabet.txt") as file_object:
	contents = file_object.read()
	print(contents)
	print("\n")

#After we call open(), an object representing the file and its contents is stored in the variable file_object
filepath = "/home/mar/Python/alphabet.txt"
with open(filepath) as file_object:
	contents = file_object.read()
	print(contents)

#Reading Line by Line
#You can use a for loop on the file object to examine each line from a file one at a time
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line) #prints each line with a blank line under each line.  These blank lines appear because an invisible newline character is at the end of each line in the text file.
#Using rstrip() on each line in the print statement eliminates these extra blank lines:
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#Making a List of Lines from a File
#When you use with, the file object returned by open() is only available inside the with block that contains it. If you want to retain access to a file’s contents outside the with block, you can store the file’s lines in a list inside the block and then work with that list.
with open("pi_digits.txt") as file_object:
	#the readlines() method takes each line from the file and stores it in a list.  The list is stored in "lines" for which we can continue to work with after the with block ends.
	lines = file_object.readlines()
#we use a simple for loop to print each line from lines. Because each item in lines corresponds to each line in the file, the output matches the contents of the file exactly
for eachline in lines:
	print(eachline.rstrip())

pi_string = ''
for eachline in lines:
	pi_string += eachline.rstrip() #Using rstrip() on each line in the print statement eliminates these extra blank lines:
print(pi_string) #prints everything lines = file_object.readlines() in one line
print(len(pi_string))

#Is Your Birthday Contained in Pi?
with open("pi_million_digits.txt") as file_object:
	lines = file_object.readlines()
pi_string = ""
for line in lines:
	pi_string += line.rstrip()
birthday = input("Enter your birthday in the form of mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi.")
else:
	print("Your birthday doesn't appears in the first million digits of pi.")

#10-1 (197)
with open("learning_python.txt") as file_object:
	contents = file_object.read()
	print(contents)
with open("learning_python.txt") as file_object:
	for line in file_object:
		print(line.rstrip())
print("\n")
with open("learning_python.txt") as file_object:
	lines = file_object.readlines()
for eachline in lines:
	print(eachline.rstrip())

#10-2 (197)
# with open("learning_python.txt") as file_object:
# 	for line in file_object:
# 		line.replace("Python","C")
# 		print(line)
message = "I really like dogs."
message.replace("dog","cat")
print(message)
with open("learning_python.txt") as file_object:
	contents = file_object.read()
	contents.replace("Python","C+") #doesn't work
	print(contents)

#Writing to a File
#To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file
#The first argument is still the name of the file we want to open. The second argument, 'w', tells Python that we want to open the file in write mode.  You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.  The open() function automatically creates the file you’re writing to if it doesn’t already exist.
with open("programming.txt", "w") as file_object:
	#we use the write() method on the file object to write a string to the file.
	file_object.write("I love programming.")

#Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

#Writing Multiple Lines
#The write() function doesn’t add any newlines to the text you write. So if you write more than one line without including newline characters
with open("programming.txt", "w") as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
	file_object.write("4323423.\n")
	file_object.write(str(984))
	file_object.write("\n")

#Appending to a File
#If you want to add content to a file instead of writing over existing content, you can open the file in append mode.  When you open a file in append mode, Python doesn’t erase the file before returning the file object. Any lines you write to the file will be added at the end of the file. If the file doesn’t exist yet, Python will create an empty file for you.
with open("programming.txt","a") as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

#10-3 (199)
name = input("What's your name? ")
with open("guest.txt", "w") as file_object:
	file_object.write(name+"\n")

#10-4 (199)
while True:
	fullname = input("What's your full name?  Enter q to quit. ")
	if fullname == "q":
		break
	print(fullname+ " welcome.  I hope you're having a good day!")
	with open("guest_book.txt", "a") as file_object:
		file_object.write(fullname+"\n")

#10-5 (199)
reason = input("Why do you like programming?  Enter q to quit. ")
while True:	
	if reason == "q":
		break
	with open("likeprogramming.txt", "a") as file_object:
		file_object.write(reason+"\n")
	reason = input("Do you have another reason why?  Enter q to quit. ")

#Exceptions
#Whenever an error occurs that makes Python unsure what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running. If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
#Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong.
#Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you write.

#try-except
#When you think an error may occur, you can write a try-except block to handle the exception that might be raised. You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception.
#We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except block. If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised and runs the code in that block.
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

#Using Exceptions to Prevent Crashes
#We can make this program more error resistant by wrapping the line that might produce errors in a try-except block. The error occurs on the line that performs the division, so that’s where we’ll put the try-except block. This example also includes an else block.
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	#If the try statement doesn’t succeed because of a division by zero error, we print a friendly message telling the user how to avoid this kind of error. The program continues to run, and the user never sees a traceback.
	except ZeroDivisionError:
		print("You can't divide by 0!")
	#Any code that depends on the try block succeeding is added to the else block. In this case if the division operation is successful, we use the else block to print the result.
	else:
		print(answer)
#The try-except-else block works like this: Python attempts to run the code in the try statement. The only code that should go in a try statement is code that might cause an exception to be raised. Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the else block. The except block tells Python what to do in case.

#Handling the FileNotFoundError Exception
#One common issue when working with files is handling missing files.
#alice.txt file doesn't exist.
try:
	with open("mobydick.txt") as fobj:
		contents = fobj.read()
except FileNotFoundError:
	print("Sorry the file doesn't exist.")

#Analyzing Text
#You can analyze text files containing entire books. Many classic works of literature are available as simple text files because they are in the public domain. The texts used in this section come from Project Gutenberg (http://gutenberg.org/), a great resource if you’re interested in working with literary texts in your programming projects.
#We’ll use the string method split(), which can build a list of words from a string.  The split() method separates a string into parts wherever it finds a space and stores all the parts of the string in a list.
title = "Alice In Wonderland"
print(title.split()) #prints ['Alice','In','Wonderland']

#To count the number of words in Alice in Wonderland we’ll use split() on the entire text. Then we’ll count the items in the list to get a rough idea of the number of words in the text.
try:
	with open("alice.txt") as objectasfile:
		contents = objectasfile.read()
except FileNotFoundError:
	print("Sorry the file doesn't exist.")
else:
	words = contents.split()
	num_words = len(words)
	print("The file has about " ,num_words)
	print("The file has about " +str(num_words)+ " words.")

#let’s move the bulk of this program to a function called count_words(). By doing so, it will be easier to run the analysis for multiple books.
def count_words(filename):
	try:
		with open(filename) as objectasfile:
			contents = objectasfile.read()
	except FileNotFoundError:
		print("Sorry, " +filename+ " the file doesn't exist.")
	else:
		words = contents.split()
		num_words = len(words)
		print(filename+ " has about " +str(num_words)+ " words.")
#one step further.  Create a for loop for all the books.
filenames = ["alice.txt","moby_dick.txt","little_women.txt"]
for eachfilenames in filenames:
	count_words(eachfilenames)

#Failing Silently
#To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block.  Example below for one book .txt file.
filename = "moby_dick.txt"
try:
	with open(filename) as objectasfile:
		contents = objectasfile.read()
except FileNotFoundError:
	pass #when a FileNotFoundError is raised, the code in the except block runs, but nothing happens. No traceback is produced, and there’s no output in response to the error that was raised.
else:
	words = contents.split()
	num_words = len(words)
	print(filename+ " has about " +str(num_words)+ " words.")

def count_words(filename):
	try:
		with open(filename) as objectasfile:
			contents = objectasfile.read()
	except FileNotFoundError:
		pass
	else:
		words = contents.split()
		num_words = len(words)
		print(filename+ " has about " +str(num_words)+ " words.")

filenames = ["alice.txt","moby_dick.txt","little_women.txt"]
for eachfilenames in filenames:
	count_words(eachfilenames)		

#The pass statement also acts as a placeholder. It’s a reminder that you’re choosing to do nothing at a specific point in your program’s execution and that you might want to do something there later. For example, in this program we might decide to write any missing filenames to a file called missing_files.txt. Our users wouldn’t see this file, but we’d be able to read the file and deal with any missing texts.

#10-6 (207)
number1 = input("Enter one number ")
number2 = input("Enter another number ")
try:
	sumnumber = (float(number1) + float(number2))
except ValueError:
	print("Please enter a number")
else:
	print(sumnumber)

#10-7 (208)
while True:
	number1 = input("Enter one number. Type q to quit. ")
	if number1 == "q":
		break
	number2 = input("Enter another number. Type q to quit. ")
	if number2 == "q":
		break
	try:
		sumnumber = (float(number1) + float(number2))
	except ValueError:
		print("Please enter a number.  Try again.")
	else:
		print(sumnumber)

#10-8 (208)
try:
	with open("cats.txt") as readfileobject:
		contents = readfileobject.read()
		print(contents)
except FileNotFoundError:
	print("File not found")

#10-9 (208)
try:
	with open("dogs.txt") as readfileobject:
		contents = readfileobject.read()
		print(contents)
except FileNotFoundError:
	pass

#10-10 (208)
with open("alice.txt") as file_object:
	contents = file_object.read()
	words = contents.split()
	#The lower method returns a copy of the string in all lowercase letters. Once a string has been created, nothing can modify its contents, so you need to create a new string with what you want in it. http://stackoverflow.com/questions/17329113/convert-list-to-lower-case
	words = [word.lower() for word in words]
	numberthe = words.count("the")
	print(numberthe)

#Storing Data
#You’ll store information users provide in data structures such as lists and dictionaries. When users close a program, you’ll almost always want to save the information they entered. A simple way to do this involves storing your data using the json module.
#The json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs. You can also use json to share data between different Python programs.
#The JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages.
#JSON (JavaScript Object Notation)

#Using json.dump() and json.load()
#The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data. Here’s how you can use json.dump() to store a list of numbers
import json #import json module
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json' #It’s customary to use the file extension .json to indicate that the data in the file is stored in the JSON format.
with open(filename, 'w') as f_obj: #open the file in write mode, which allows json to write the data to the file
	json.dump(numbers, f_obj) #use the json.dump() function to store the list numbers in the file numbers.json
#Now we’ll write a program that uses json.load() to read the list back into memory
filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj) #we use the json.load() function to load the information stored in numbers.json, and we store it in the variable numbers
print(numbers) #print the recovered list of numbers

#Saving and Reading User-Generated Data\
#storing the user’s name
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
	json.dump(username, f_obj) #use json.dump(), passing it a username and a file object, to store the username in a file
	print("We'll remember you when you come back, " + username + "!")
#greets a user whose name has already been stored
filename = 'username.json'
with open(filename) as f_obj:
	username = json.load(f_obj) #use json.load() to read the information stored in username.json into the variable username.
	print("Welcome back, " + username + "!")

#We need to combine these two programs into one file.
import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")

#Refactoring
#Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.
import json
def greet_user():
	"""Greet the user by name."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")
greet_user()

import json
def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
greet_user()

import json
def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username
def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you com back, " +username+ "!")
greet_user()

#10-11 (214)
#10-12 (214)
#10-13 (214)