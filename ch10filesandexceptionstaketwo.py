#Python Crash Course Chapter 10 Files And Exceptions
#skipped json module which allows you to save user data so it isn’t lost when your program stops running.
#When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function.
#"r" read mode, "w" write mode, "a" append mode, "r+" read and write mode, default is read mode

#The keyword with closes the file once access to it is no longer needed. Notice how we call open() in this program but not close().
with open("pi_digits.txt") as fileobject: #Python stores the text file pi_digits.txt object as fileobject
	contents = fileobject.read()
	print(contents) #print 3.1415926535\n 8979323846\n 2643383279
print("Is there a blank line above?")
#The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. If you want to remove the extra blank line, you can use rstrip() in the print statement
with open("pi_digits.txt") as fileobject: #Python stores the text file pi_digits.txt object as fileobject
	contents = fileobject.read()
	print(contents.rstrip()) #print 3.1415926535\n 8979323846\n 2643383279.  rstrip() method removes or strips any whitespace characters from the right side of a string.
#To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.  Here are relative paths.
#with open('text_files/filename.txt') as fileobject: on Linux and OS X
#with open('text_files\filename.txt') as fileobject: on Windows
#Absolute paths are usually longer than relative paths, so it’s helpful to store them in a variable and then pass that variable to open(). On Linux and OS X, absolute paths look like this:  file_path = '/home/ehmatthes/other_files/text_files/filename.txt' with open(file_path) as fileobject:.  Windows:  file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt' with open(file_path) as fileobject:

#You can use a for loop on the file object to examine each line from a file one at a time:
filename = "pi_digits.txt"
with open(filename) as fileobject:
	for eachline in fileobject:
		print(eachline) #print 3.1415926535\n\n 8979323846\n\n 2643383279
with open(filename) as fileobject:
	for eachline in fileobject:
		print(eachline.rstrip()) #print 3.1415926535\n 8979323846\n 2643383279

#When you use with, the file object returned by open() is only available inside the with block that contains it. If you want to retain access to a file’s contents outside the with block, you can store the file’s lines in a list inside the block and then work with that list.
filename = "pi_digits.txt"
with open(filename) as fileobject:
	lines = fileobject.readlines() #readlines() method takes each line from the file and stores it in a list.
print(lines) #print ['3.1415926535\n', '8979323846\n', '2643383279']
pistring = ""
for line in lines:
	print(line.rstrip()) #print 3.1415926535\n 8979323846\n 2643383279
	pistring += line.rstrip()
print(pistring) #print 3.141592653589793238462643383279
filename = "pi_million_digits.txt"
with open(filename) as fileobject:
	lines = fileobject.read()
print(lines[0:52]) #print 3.14159265358979323846264338327950288419716939937510
# birthday = input("Enter your birthday in the form of mmddyy: ")
# if birthday in lines:
# 	print("Your birthday appears in the first million digits of pi")
# else:
# 	print("Your birthday doesn't appear in the first million digits of pi")

with open("learning_python.txt") as fileobject:
	learn = fileobject.read()
	print(learn) #print In Python you can print\n In Python you can write functions\n In Python you can for loops\n In Python you can while loops\n
with open("learning_python.txt") as fileobject:
	learnlist = fileobject.readlines()
	print(learnlist) #print ['In Python you can print\n', 'In Python you can write functions\n', 'In Python you can for loops\n', 'In Python you can while loops']
for eachline in learnlist:
	print(eachline.rstrip()+" y") #print In Python you can print y\n In Python you can write functions y\n In Python you can for loops y\n In Python you can while loops y
with open("learning_python.txt") as fileobject:
	learn = fileobject.read()
learn =  learn.replace("Python","C")
print(learn) #print In C you can print\n In C you can write functions\n In C you can for loops\n In C you can while loops

filename = "programming.txt"
with open (filename, "w") as fileobject:
	fileobject.write("I love programming on 081817.")
	fileobject.write("I love creating new games on 081817.\n")
	fileobject.write("I love creating new games on 081817 new line.\n")
	fileobject.write("I love creating new \t games on 081817 tab.\n")
#The open() function automatically creates the file you’re writing to if it doesn’t already exist. However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the file before returning the file object.
#Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.
with open (filename, "a") as fileobject:
	fileobject.write("I also love finding meaning in large datasets.\n")
	fileobject.write("I love creating apps that can run in a browser.\n")
# name = input("What is your name ")
# with open ("guest.txt","w") as fileobject:
# 	fileobject.write(name)
# while True:
# 	name = input("What is your name?  Type q to quit ")
# 	if name == "q":
# 		break
# 	print("Welcome "+name+".  You're entered in the guest book")
# 	with open ("guest_book.txt","a") as fileobject:
# 		fileobject.write(name+" is coming to the dance.\n")
# while True:
# 	likeprogramming = input("Why do you like programming?  Type q to quit ")
# 	if likeprogramming == "q":
# 		break	
# 	with open ("likeprogramming.txt","a") as fileobject:
# 		fileobject.write(likeprogramming+"\n")
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
# 	first_number = input("\nFirst number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("Second number: ")
# 	if second_number == 'q':
# 		break
# 	try:
# 		answer = int(first_number) / int(second_number)
# 	except ZeroDivisionError:
# 		print("You can't divide by 0!")
# 	else:
# 		print(answer)
filename = "alices.txt"
try:
	with open(filename,"r") as fileobject:
		contents = fileobject.read()
except FileNotFoundError:
	print(filename+" file doesn't exist.")
else:
	print(contents)
#create a function to verify multiple files
def filecheck(filename):
	try:
		with open(filename,"r") as fileobject:
			contents = fileobject.read()
	except FileNotFoundError:
		print(filename+" file doesn't exist.")
		#Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened.  If yes, then use pass.
	else:
		print(contents)
textfilelist = ["cats","catss","guest","programming"]
for eachtextfilelist in textfilelist:
	eachtextfilelist = eachtextfilelist+".txt"
	filecheck(eachtextfilelist)
# while True:
# 	twonumbers = input("Enter two numbers separated by a space ")
# 	twonumbers = twonumbers.split()
# 	try:
# 		addition = int(twonumbers[0]) + int(twonumbers[1])
# 	except ValueError:
# 		print("friendly message incorrect numbers input ValueError")
# 	except IndexError:
# 		print("friendly message incorrect numbers input IndexError")
# 	else:
# 		if twonumbers[0] == "q" or twonumbers[1] == "q":
# 			break
# 		print(addition)
#skipped json module p208-214