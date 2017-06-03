#Creating and Using a Class
#You can model almost anything using classes. Let’s start by writing a simple class, Dog, that represents any dog.
#Two pieces of information (name and age) and those two behaviors (sit and roll over) will go in our Dog class because they’re common to most dogs.
#This class will tell Python how to make an object representing a dog. After our class is written, we’ll use it to make individual instances, each of which represents one specific dog.
#Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over():
class Dog():
#A function that’s part of a class is a method.
#The __init__() method is a special method Python runs automatically whenever we create a new instance based on the Dog class.
#The self parameter is required in the method definition, and it must come first before the other parameters. It must be included in the definition because when Python calls this __init__() method later (to create an instance of Dog), the method call will automatically pass the self argument. Every method call associated with a class automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.
	#When we make an instance of Dog, Python will call the __init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it. Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.
	def __init__(self, name, age):
		#Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.  self.name = name takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance being created.  The same process happens with self.age = age. Variables that are accessible through instances like this are called attributes.
		self.name = name
		self.age = age
	#The Dog class has two other methods defined: sit() and roll_over().  Because these methods don’t need additional information like a name or age, we just define them to have one parameter, self. The instances we create later will have access to these methods. In other words, they’ll be able to sit and roll over. For now, sit() and roll_over() don’t do much. They simply print a message saying the dog is sitting or rolling over.
	def sit(self):
		print(self.name.title() + " is now sitting.")
	def roll_over(self):
		print(self.name.title() + " rolled over!")

#Making an Instance from a Class
#Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.
#we tell Python to create a dog whose name is 'willie' and whose age is 6.
#When Python reads this line, it calls the __init__() method in Dog with the arguments 'willie' and 6. The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided. The __init__() method has no explicit return statement, but Python automatically returns an instance representing this dog. We store that instance in the variable my_dog.
my_dog = Dog('willie', 6)
#To access the attributes of an instance, you use dot notation.
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#Calling Methods
#After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
#give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot. When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code.
my_dog.sit()
my_dog.roll_over()

#Creating Multiple Instances
#You can create as many instances from a class as you need. Let’s create a second dog called your_dog:
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

#we create a dog named Willie and a dog named Lucy. Each dog is a separate instance with its own set of attributes, capable of the same set of actions

#9-1 (166)
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name+ " serves " + self.cuisine_type+" food.")
	def open_restaurant(self):
		print(self.restaurant_name+ " is open!")
my_restaurant = Restaurant("Ray's Place","Diner")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#9-2 (166)
second_restaurant = Restaurant("James' Place","Chinese")
second_restaurant.describe_restaurant()
third_restaurant = Restaurant("Michelle's Place","Mexican")
third_restaurant.describe_restaurant()
fourth_restaurant = Restaurant("Mars Mayflower","Chinese")
fourth_restaurant.describe_restaurant()

#9-3 (166)
class User():
	def __init__(self, first_name, last_name, email, hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.hobby = hobby
	def describe_user(self):
		print(self.first_name+ " " +self.last_name+ "\'s email address is " +self.email+ ".  A hobby is " +self.hobby+ ".")
	def greet_user(self):
		print(self.first_name+ " " +self.last_name+ ", welcome to the website!")

my_user = User("Raymond","Mar","hotmail.com","Reading books")
my_user.describe_user()
my_user.greet_user()
my_user = User("Alpha","Bravo","gmail.com","Working out at the gym")
my_user.describe_user()
my_user.greet_user()
my_user = User("Sierra","Tango","yahoo.com","Playing board games")
my_user.describe_user()
my_user.greet_user()

#Working with Classes and Instances
#Let’s write a new class representing a car. Our class will store information about the kind of car we’re working with, and it will have a method that summarizes this information
class Car():
	#The __init__() method takes in these parameters and stores them in the attributes that will be associated with instances made from the Car() class. When we make a new Car instance, we’ll need to specify a make, model, and year for our instance.
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def get_description(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
#we make an instance from the Car class and store it in the variable my_new_car. Then we call get_descriptive_name() to show what kind of car we have.
mynewcar = Car("Audi","A4",2016)
print(mynewcar.get_description()) #get_description() method no print statement.  Print the printstatement when calling the method from Car class

#Setting a Default Value for an Attribute
#When setting a default value, it makes sense to specify this initial value in the body of the __init__() method; if you do this for an attribute, you don’t have to include a parameter for that attribute.
#Let’s add an attribute called odometer_reading that always starts with a value of 0. We’ll also add a method read_odometer() that helps us read each car’s odometer
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_description(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " +str(self.odometer_reading) + " miles on it.")
mynewcar = Car("Audi","A6",2019)
print(mynewcar.get_description())
mynewcar.read_odometer() #read_odometer() method yes print statement.  Don't need printstatement when calling the method from Car class

#Modifying Attribute Values
#You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method.
#1. Modifying an Attribute’s Value Directly.  The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly
mynewcar.odometer_reading = 23
mynewcar.read_odometer()
#2. Modifying an Attribute’s Value Through a Method.  Pass the new value to a method that handles the updating internally.
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_description(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " +str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):		
		self.odometer_reading = mileage
mynewcar = Car("Audi","A8",2019)
print(mynewcar.get_description())
mynewcar.update_odometer(2323)
mynewcar.read_odometer()

class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 5000
	def get_description(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " +str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		#Set the odometer reading to the given value.
		#Reject the change if it attempts to roll the odometer back.
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")	
mynewcar = Car("Audi","A8",2019)
print(mynewcar.get_description())
mynewcar.update_odometer(2323)
mynewcar.read_odometer()

#Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value.  Here’s a method that allows us to pass this incremental amount and add that value to the odometer reading:
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 5000
	def get_description(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " +str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		#Set the odometer reading to the given value.
		#Reject the change if it attempts to roll the odometer back.
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles

myusedcar = Car("Audi","A4",2016)
print(myusedcar.get_description())
myusedcar.update_odometer(23500)
myusedcar.read_odometer() #prints the odometer 23500
myusedcar.increment_odometer(100)
myusedcar.read_odometer() #prints the odometer 23600.  Seems call the read_odometer() method with updated odometer since increment_odometer() method is last method in class Car()

#9-4 (171)
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.numbered_served = 0 #attribute called number_served with a default value of 0
	def describe_restaurant(self):
		print(self.restaurant_name+ " serves " + self.cuisine_type+" food.")
	def open_restaurant(self):
		print(self.restaurant_name+ " is open!")
	def set_number_served(self, customers):
		self.number_served = customers
		print("Today the restaurant began with " +str(self.number_served))
	def customers_today(self):
		print("The restaurant served so far " +str(self.number_served))
	def increment_number_served(self, morecustomers):
		self.number_served += morecustomers

my_restaurant = Restaurant("Ray's Place","Diner")
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(5)
my_restaurant.increment_number_served(55)
my_restaurant.customers_today()

#9-5 (171)
class User():
	def __init__(self, first_name, last_name, email, hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.hobby = hobby
		self.login_attempts = 0
	def describe_user(self):
		print(self.first_name+ " " +self.last_name+ "\'s email address is " +self.email+ ".  A hobby is " +self.hobby+ ".")
	def greet_user(self):
		print(self.first_name+ " " +self.last_name+ ", welcome to the website!")
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(self.login_attempts)
	def reset_login_attempts(self):
		self.login_attempts = 0

# login = User() #must have values in class User() __init__ to work
login = User("Raymond","Mar","hotmail.com","Reading books")
login.increment_login_attempts() #prints 1 
login.increment_login_attempts() #prints 2
login.increment_login_attempts() #prints 3
login.increment_login_attempts() #prints 4
login.reset_login_attempts()
login.increment_login_attempts() #prints 1

#Inheritance
#You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. When one class inherits from another, it automatically takes on all the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class. The child class inherits every attribute and method from its parent class but is also free to define new attributes and methods of its own.
#The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class. To do this, the __init__() method for a child class needs help from its parent class.
#let’s model an electric car. An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class we wrote earlier. Then we’ll only have to write code for the attributes and behavior specific to electric cars.
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_description(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()
	def read_odometer(self):
		print("This car has " +str(self.odometer_reading) + " miles on it.")
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		self.odometer_reading += miles
#we define the child class, ElectricCar. The name of the parent class must be included in parentheses in the definition of the child class.	
class ElectricCar(Car):
	#__init__() method takes in the information required to make a Car instance
	def __init__(self, make, model, year):
		#super() function helps Python make connections between the parent and child class. This line tells Python to call the __init__() method from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes of its parent class. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
		super().__init__(make, model, year)
#calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car.
my_tesla = ElectricCar("Tesla","Model S",2016)
print(my_tesla.get_description())
#Aside from __init__(), there are no attributes or methods yet that are particular to an electric car. At this point we’re just making sure the electric car has the appropriate Car behaviors from parent class Car.

#Defining Attributes and Methods for the Child Class
#you can add any new attributes and methods necessary to differentiate the child class from the parent class.
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		#attribute will be associated with all instances created from the ElectricCar class but won’t be associated with any instances of Car
		self.battery_size = 70
	def describe_battery(self):
		print("This car has a " +str(self.battery_size)+ "-kWh battery.")
my_tesla = ElectricCar("Tesla","Model S",2018)
print(my_tesla.get_description())
my_tesla.describe_battery()

#Overriding Methods from the Parent Class
#You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 70
	def describe_battery(self):
		print("This car has a " +str(self.battery_size)+ "-kWh battery.")
	def fill_gas_tank():
		print("This car doesn't need a gas tank!")
#Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead. When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class.

#Instances as Attributes
#you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.
class Battery():
	def __init__(self, battery_size=80):
		self.battery_size = battery_size
	def describe_battery(self):
		print("This car has a " +str(self.battery_size)+ "-kWh battery.")
	def get_range(self):
		if self.battery_size == 80:
			range = 260
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		#attribute self.battery create a new instance of Battery; any ElectricCar instance will now have a Battery instance created automatically.
		self.battery = Battery()
my_tesla = ElectricCar("Tesla","Model T",2020)
print(my_tesla.get_description())
#When we want to describe the battery, we need to work through the car’s battery attribute.  Look at the instance my_tesla, find its battery attribute self.battery, and call the method describe_battery() that’s associated with the Battery instance stored in the self.battery attribute.
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#9-6 (178)
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name+ " serves " + self.cuisine_type+" food.")
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
	def flavor(self):
		flavors = ["vanilla","chocolate","strawberry","mango"]
		self.flavors  = flavors
		print(self.flavors)
myicecream = IceCreamStand("Ray's Ice Cream","Ice Cream")
myicecream.describe_restaurant()
myicecream.flavor()

#9-7 (178)
class User():
	def __init__(self, first_name, last_name, email, hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.hobby = hobby
		self.login_attempts = 0
	def describe_user(self):
		print(self.first_name+ " " +self.last_name+ "\'s email address is " +self.email+ ".  A hobby is " +self.hobby+ ".")
	def greet_user(self):
		print(self.first_name+ " " +self.last_name+ ", welcome to the website!")
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(self.login_attempts)
	def reset_login_attempts(self):
		self.login_attempts = 0
class Admin(User):
	def __init__(self,first_name, last_name, email, hobby):
		super().__init__(first_name, last_name, email, hobby)
	def show_privileges(self):
		privileges = ["can add post","can delete post","can ban user"]
		self.privileges = privileges
		print(self.privileges)
myadmin = Admin("Raymond","Mar","must have email attribute","must have hobby attribute")		
myadmin.show_privileges()

#9-8 (178)
class User():
	def __init__(self, first_name, last_name, email, hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.hobby = hobby
	def describe_user(self):
		print(self.first_name+ " " +self.last_name+ "\'s email address is " +self.email+ ".  A hobby is " +self.hobby+ ".")
class Admin(User):
	def __init__(self,first_name, last_name, email, hobby):
		super().__init__(first_name, last_name, email, hobby)
		self.privileges = Privileges()
class Privileges():
	def __init__(self):
		privileges = ["can add post, too","can delete post, too","can ban user, too"]
		self.privileges = privileges
		print(self.privileges)
myadmin = Admin("Raymond","Mar","must have email attribute","must have hobby attribute")		
myadmin.privileges
#myadmin.privileges() #() not needed because there's no method in class Privileges()

#9-9 (178)
class Battery():
	def __init__(self, battery_size=80):
		self.battery_size = battery_size
	def describe_battery(self):
		print("This car has a " +str(self.battery_size)+ "-kWh battery.")
	def get_range(self):
		if self.battery_size == 80:
			range = 260
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
my_tesla = ElectricCar("Tesla","Model T2",2022)
print(my_tesla.get_description())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Importing Classes
#Python lets you store classes in modules and then import the classes you need into your main program
#no need for .py in ch9classescar.py.  Just ch9classescar
from ch9classescar import Car
my_new_car = Car("Audi","A3",2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 100
my_new_car.read_odometer()
#When you instead move the class to a module and import the module, you still get all the same functionality, but you keep your main program file clean and easy to read.

#Storing Multiple Classes in a Module
#You can store as many classes as you need in a single module, although each class in a module should be related somehow.
#The classes Battery and ElectricCar both help represent cars, so let’s add them to the module ch9classescar.py
from ch9classescar import ElectricCar
my_tesla = ElectricCar("Tesla","Model Z","2017")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Importing Multiple Classes from a Module
#If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar.
#You import multiple classes from a module by separating each class with a comma. Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.
from ch9classescar import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

#Importing an Entire Module
#You can also import an entire module and then access the classes you need using dot notation.
import ch9classescar
my_beetle = ch9classescar.Car('volkswagen', 'beetle', 2017)
print(my_beetle.get_descriptive_name())
my_tesla = ch9classescar.ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.get_descriptive_name())

#Importing All Classes from a Module
#You can import every class from a module using the following syntax: from module_name import *
#This method is not recommended for two reasons. First, it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses.

#Importing a Module into a Module
#Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.
#For example, let’s store the Car class in one module and the ElectricCar and Battery classes in a separate module. We’ll make a new module called electric_car.py—replacing the electric_car.py file we created earlier—and copy just the Battery and ElectricCar classes into this file
from ch9classescar import Car
from ch9classescar_electric import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2000)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2000)
print(my_tesla.get_descriptive_name())

#9-10 (184)
from ch9classesrestaurant import Restaurant
yourrestaurant = Restaurant("Alpha's Hot Dogs","Fast Food")
yourrestaurant.describe_restaurant()

#9-11 (184)
from ch9classesadmin import Admin, Privileges
youradmin = Admin("Raymond","Mar","must have email attribute","must have hobby attribute")		
youradmin.privileges

#9-12 (184)
from ch9classesadminprivilegesadmin import Admin, Privileges
youradmin = Admin("Raymond","Mar","must have email attribute","must have hobby attribute")		
youradmin.privileges

#The Python Standard Library
#The Python standard library is a set of modules included with every Python installation.  You can use any function or class in the standard library by including a simple import statement at the top of your file. Let’s look at one class, OrderedDict, from the module collections.
#Dictionaries allow you to connect pieces of information, but they don’t keep track of the order in which you add key-value pairs. If you’re creating a dictionary and want to keep track of the order in which key-value pairs are added, you can use the OrderedDict class from the collections module. Instances of the OrderedDict class behave almost exactly like dictionaries except they keep track of the order in which key-value pairs are added.

#import OrderedDict class from the collections module
from collections import OrderedDict
#create an instance of the OrderedDict class and store this instance in favorite_languages.  Notice there are no curly brackets; the call to OrderedDict() creates an empty ordered dictionary for us and stores it in favorite_languages.
favorite_languages = OrderedDict()
#add each name and language to favorite_languages one at a time
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
#when we loop through favorite_languages, we know we’ll always get responses back in the order they were added
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

#9-13 (186)
from collections import OrderedDict
glossary = OrderedDict()
glossary["dictionary"] = "lists and values"
glossary["ifthenelse"] = "a loop"
glossary["lists"] = "store values in one container"
glossary["print"] = "statement to return a value"
glossary["set()"] = "function returns unique values"
glossary["string"] = "words"
glossary["variable"] = "store a value"
for term, definition in glossary.items():
	print(term+": " +definition)

#9-14 (186)
from random import randint
class Die():
	def __init__(self, sides=6):
		self.sides = sides
	def roll_die(self):
		print(randint(1,self.sides))
dice = Die(10)
x = 1
while x < 11:
	dice.roll_die()
	x += 1

#9-15 (186)
#One excellent resource for exploring the Python standard library is a site called Python Module of the Week. Go to http://pymotw.com/ and look at the table of contents. Find a module that looks interesting to you and read about it, or explore the documentation of the collections and random modules.