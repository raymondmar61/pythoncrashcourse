print("Hello Python world!  Print() is a function.")
message = ("Hello Python world!  Print() is a function.")
print(message)
message = ("Hello Python Crash Course world!")
print(message)
# Many programming errors are simple, single-character typos in one
# line of a program. If you’re spending a long time searching for one of these
# errors, know that you’re in good company. Many experienced and talented
# programmers spend hours hunting down these kinds of tiny errors. Try to
# laugh about it and move on, knowing it will happen frequently throughout
# your programming life.

# A method is an action that Python can perform on a piece of data. The
# dot (.) after name in name.title() tells Python to make the title() method
# act on the variable name. Every method is followed by a set of parentheses,
# because methods often need additional information to do their work.  That information is provided in the parentheses.
name = "ada lovelace"
print(name.title()) #The title() function doesn’t need any additional information, so its parentheses are empty.  title() displays each word in titlecase, where each word begins with a capital letter.
print(name.upper())
print(name.lower())
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name #use plus symbol to combine strings or concatenation
print(full_name)
print("Hello, " + full_name.title() + "!")
stringsavevariable = print("Hello, " + full_name.title() + "! variable save")
print(stringsavevariable)

#whitespace.  use "\t" for tab, \n for new line
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

#Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language = favorite_language.rstrip() #remove spaces permanently, obviously print statement doesn't change the value of the assigned variable
print(favorite_language)
#You can also strip whitespace from the left side of a string using the lstrip() method or strip whitespace from both sides at once using strip()

#Python calls any number with a decimal point a float. This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number.
#When you use integers within strings like this, you need to specify explicitly that you want Python to use the integer as a string of characters. You can do this by wrapping the variable in the str() function, which tells Python to represent non-string values as strings.
age = 23
print("Happy " +str(age)+ "rd birthday!")