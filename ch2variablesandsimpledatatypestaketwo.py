#Python Crash Course Chapter 2 Variables and Simple Data Types Page 19

message = "Hello Python world!"
print(message) #print Hello Python world!
message = "Hello Python Crash Course world"
print(message) #print Hello Python Crash Course world!
name = "ada lovelace"
print(name.title()) #print Ada Lovelace
#A method is an action on data. The dot (.) after name in name.title() tells Python to make the title() method act on the variable name. Every method is followed by a set of parentheses, because methods often need additional information which is provided inside the parentheses. However, title() parentheses are empty because it needs no additional information.
name = name.title()
print(name.upper()) #print ADA LOVELACE
print(name.lower()) #print ada lovelace
firstname = "ada"
lastname = "lovelace"
fullname = firstname+ " " +lastname
print(fullname) #print ada lovelace
print("Hello " +fullname.title()+ "!") #print Hello Ada Lovelace!
print("\tPython") #print     Python
print("Languages:\nPython\nc\nJavaScript") #print Languages:\n Python\n c\n JavaScript\n
favoritelanguage = "python     "
print(favoritelanguage.rstrip()) #print python
favoritelanguage = "     python"
print(favoritelanguage) #print     python
print(favoritelanguage.lstrip()) #print python
favoritelanguage = "     python     "
print(favoritelanguage) #print     python
print(favoritelanguage.strip()) #print python

name = "Jack Dawson"
print("Hello " +name+ ", would you like to learn some Python today?")
print(name.lower()) #print jack dawson
print(name.upper()) #print JACK DAWSON
print(name.title()) #print Jack Dawson
print("Steve Jobs said, \"You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something--your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.\"")
famousquote = "Steve Jobs said, \"You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future. You have to trust in something--your gut, destiny, life, karma, whatever. This approach has never let me down, and it has made all the difference in my life.\""
print(famousquote)
name = "\tJack\n Dawson   "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#none of the strip()s printed Jack Dawson in one line.  lstrip() and strip() removed the tab \t.

print(3 ** 2) #print 9 exponents
age = 23
print("Happy " +str(age)+ "rd Birthday!") #print Happy 23rd Birthday!
print(3/2) #print 1.5
print(3.0/2) #print 1.5
print(3/2.0) #print 1.5
print(3.0/2.0) #print 1.5

import this #return The Zen of Python by Tim Peters
