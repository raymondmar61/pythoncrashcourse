#Python Crash Course Chapter 9 Classes
#capitalized names refer to classes; a lowercase name like my_dog refers to a single instance created from a class.
#A function that’s part of a class is a method. Everything you learned about functions applies to methods as well
#If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. When one class inherits from another, it automatically takes on all the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class.
# are included

class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def sit(self):
		print(self.name.title()+ " is now sitting.")
	def rollover(self):
		print(self.name.title()+ " rolled over!")
mydog = Dog("Willie",6)
print("My dog's name is " + mydog.name.title() + ".") #print My dog's name is Willie
print("My dog is " + str(mydog.age) + " years old.") #print My dog is 6 years old.
mydog.sit() #return Willie is now sitting.
mydog.rollover()#return Willie rolled over!
yourdog = Dog("Lucy",3)
print("My dog's name is " + yourdog.name.title() + ".") #print My dog's name is Lucy
print("My dog is " + str(yourdog.age) + " years old.") #print My dog is 3 years old.
yourdog.sit() #return Lucy is now sitting.
yourdog.rollover()#return Lucy rolled over!
noduplicateclassdog = Dog("Lucy",3)
print("My dog's name is " + noduplicateclassdog.name.title() + ".") #print My dog's name is Lucy
print("My dog is " + str(noduplicateclassdog.age) + " years old.") #print My dog is 3 years old.
noduplicateclassdog.sit() #return Lucy is now sitting.
noduplicateclassdog.rollover()#return Lucy rolled over!
print("\n")

class Restaurant():
	def __init__(self, restaurantname, cuisinetype):
		self.restaurantname = restaurantname
		self.cuisinetype = cuisinetype
	def describerestaurant(self):
		print(self.restaurantname)
		print(self.cuisinetype)
	def openrestaurant(self):
		print("Restaurant is open!")
	def setnumberserved(self, initialcustomersserved):
		self.customersserved = initialcustomersserved
	def readnumberserved(self):
		print(self.customersserved, "customers have been served.")
	def incrementnumberserved(self, incrementcustomers):
		self.customersserved += incrementcustomers
myrestaurant = Restaurant("Ming River Restaurant","Chinese")
myrestaurant.describerestaurant() #return Ming River Restaurant\n Chinese
myrestaurant.openrestaurant() #return Restaurant is open!
myrestaurant.setnumberserved(500)
myrestaurant.readnumberserved() #return 500 customers have been served.
myrestaurant.incrementnumberserved(100)
myrestaurant.readnumberserved() #return 600 customers have been served.
restaurant2 = Restaurant("Santos Tacos","Mexican")
restaurant2.describerestaurant() #return Santos Tacos\n Mexican
restaurant2.openrestaurant() #return Restaurant is open!
restaurant2.setnumberserved(399)
restaurant2.readnumberserved() #return 399 customers have been served.
restaurant2.incrementnumberserved(12)
restaurant2.readnumberserved() #return 411 customers have been served.
class User():
	def __init__(self, firstname, lastname, age, favoritefood):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.favoritefood = favoritefood
		self.loginattempts = 0
	def describeuser(self):
		print(self.firstname+ " " +self.lastname+ " is" ,self.age, "years old.  Favorite food is " +self.favoritefood+".")
	def greetuser(self):
		print(self.firstname+ " welcome to the website.")
	def incrementloginattempts(self):
		self.loginattempts += 1
		print(self.firstname+ " logged on" ,self.loginattempts, "times.")
	def resetloginattempts(self):
		self.loginattempts = 0
brad = User("Brad","Johnson",45,"Pizza")
brad.describeuser() #return Brad Johnson is 45 years old.  Favorite food is Pizza.
brad.greetuser() #return Brad welcome to the website.
brad.incrementloginattempts() #return Brad logged on 1 times.
brad.incrementloginattempts() #return Brad logged on 2 times.
brad.incrementloginattempts() #return Brad logged on 3 times.
brad.resetloginattempts()
brad.incrementloginattempts() #return Brad logged on 1 times.
print("\n")

#Modifying Attribute Values.  There are three ways:  change the value directly through an instance, set the value through a method, or increment the value through a method
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometerreading = 0
	def getdescriptivename(self):
		longname = str(self.year)+ " " +self.make+ " " +self.model
		return longname.title()
	def updateotometer(self, mileage):
		self.odometerreading = mileage
	def readodometer(self):
		print("This car has " +str(self.odometerreading)+ " miles on it.")
	def incrementodometer(self, miles):
		self.odometerreading += miles
mynewcar = Car("audi","a4", 2016)
print(mynewcar.getdescriptivename()) #print 2016 Audi A4
mynewcar.readodometer() #return This car has 0 miles on it.
mynewcar.odometerreading = 23
mynewcar.readodometer() #return This car has 23 miles on it.
mynewcar.updateotometer(458)
mynewcar.readodometer() #return This car has 458 miles on it.
usedcar = Car("subaru","outback", 2013)
print(usedcar.getdescriptivename()) #print 2013 Subaru Outback
usedcar.updateotometer(23500)
usedcar.readodometer() #return This car has 23500 miles on it.
usedcar.incrementodometer(100)
usedcar.readodometer() #return This car has 23600 miles on it.
print("\n")

#Inheritance
class ElectricCar(Car): #the name of the parent class must be in parentheses
	def __init__(self, make, model, year):
		super().__init__(make, model, year) #super() makes connection between parent Car and child ElectricCar
		self.batterysize = 70
	def describebattery(self): #prints information about batterysize
		print("This car has a " +str(self.batterysize)+ "-kWh battery.")
mytesla = ElectricCar("Tesla","Model S",2016)
print(mytesla.getdescriptivename()) #print 2016 Tesla Model S
mytesla.describebattery() #return This car has a 70-kWh battery.
#You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.  Define a method in the child class with the same name as the method you want to override in the parent class. Python disregards the parent class method and only pay attention to the method you define in the child class.

#Instances as attributes
class Battery2():
	def __init__(self, batterysize = 702):
		self.batterysize = batterysize
	def describebattery(self):
		print("This car has a " +str(self.batterysize)+ "-kWh battery.")
	def getrange(self):
		if self.batterysize == 702:
			range = 240
		elif self.batterysize == 852:
			range = 270
		message = ("This car can go approximately " +str(range)+ " miles on a full charge.")
		print(message)
	def upgradebattery(self):
		self.batterysize = 852
		print("Your car now has a battery size of" ,self.batterysize)
class ElectricCar2(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery2()
mytesla2 = ElectricCar2("Tesla2","Model S2",2016)
print(mytesla2.getdescriptivename()) #print 2016 Tesla2 Model S2
mytesla2.battery.describebattery() #return This car has a 702-kWh battery.  Also, it's like instance.attribute.method <--> mytesla2.battery.describebattery()
mytesla2.battery.getrange() #return This car can go approximately 240 miles on a full charge.
print("\n")

class IceCreamStand(Restaurant):
	def __init__(self, restaurantname, cuisinetype="Ice Cream"):
		super().__init__(restaurantname, cuisinetype)
	def flavors(self, icecreamflavors):
		self.icecreamflavors = icecreamflavors
		print(icecreamflavors)
vvanila = IceCreamStand("Icy Icy")
vvanila.describerestaurant() #return Icy Icy\n Ice Cream
vvanila.flavors(["Vanilla","Chocolate","Strawberry"]) #return ['Vanilla', 'Chocolate', 'Strawberry']
class Admin(User):
	def __init__(self, firstname, lastname, age, favoritefood):
		super().__init__(firstname, lastname, age, favoritefood)
	def showprivileges(self):
		privileges = ["can add post","can delete post","can ban user", "all access"]
		print(privileges)
david = Admin("Dave","Smith",54,"Cupcake")
david.showprivileges() #return ['can add post', 'can delete post', 'can ban user', 'all access']

mytesla3 = ElectricCar2("Tesla3","Model S3",2016)
print(mytesla3.getdescriptivename()) #print 2016 Tesla3 Model S3
mytesla3.battery.describebattery() #return This car has a 702-kWh battery.
mytesla3.battery.getrange() #return This car can go approximately 240 miles on a full charge.
mytesla3.battery.upgradebattery() #return Your car now has a battery size of 852
mytesla3.battery.getrange() #return This car can go approximately 270 miles on a full charge.
print("\n")

#Import Classes Importing Classes.  Store classes in modules or another file.  Import the classes.
from ch9classescartaketwo import Carimport
mynewcarimport = Carimport("audi","a4",2017)
print(mynewcarimport.getdescriptivename()) #print 2017 Audi A4
mynewcarimport.odometerreading = 2300
mynewcarimport.readodometer() #return This car has 2300 miles on it.
from ch9classescartaketwo import ElectricCar2import
myteslaimport = ElectricCar2import("tesla","model s",2017)
print(myteslaimport.getdescriptivename()) #print 2017 Tesla Model S
myteslaimport.battery.describebattery() #return This car has a 702-kWh battery.
myteslaimport.battery.getrange() #return This car can go approximately 240 miles on a full charge.
myteslaimport.battery.upgradebattery() #return Your car now has a battery size of 852
myteslaimport.battery.getrange() #return This car can go approximately 270 miles on a full charge.
from ch9classescartaketwo import Carimport, ElectricCar2import
mybeetle = Carimport("volkswagen","beetle",2016)
print(mybeetle.getdescriptivename()) #print 2016 Volkswagen Beetle
myteslaimport2 = ElectricCar2import("tesla2","roadster2",2016)
print(myteslaimport2.getdescriptivename()) #print 2016 Tesla2 Roadster2
import ch9classescartaketwo
mybeetle3 = ch9classescartaketwo.Carimport("volkswagen3","beetle3",2017)
print(mybeetle3.getdescriptivename())
myteslaimport3 = ch9classescartaketwo.ElectricCar2import("tesla3","roadster3",2016)
print(myteslaimport3.getdescriptivename()) #print 2016 Tesla3 Roadster3
from ch9classescartaketwo import Carimport
from ch9classescar_electrictaketwo import ElectricCar
mybeetle4 = Carimport("volkswagen4","beetle4",2017)
print(mybeetle4.getdescriptivename()) #print 2016 Volkswagen4 Beetle4
myteslaimport4 = ElectricCar("tesla4","roadster4",2016)
print(myteslaimport4.getdescriptivename()) #print 2016 Tesla4 Roadster4
myteslaimport4.describebattery() #return This car has a 70-kWh battery.
print("\n")

from ch9classesrestauranttaketwo import Restaurantimport
importChinese = Restaurantimport("Mang's","Chinese")
importChinese.describerestaurant() #return Mang's\n Chinese
importChinese.setnumberserved(78)
importChinese.readnumberserved() #return 78 customers have been served.
importChinese.incrementnumberserved(100)
importChinese.readnumberserved() #return 178 customers have been served.
from ch9classesadminusertaketwo import Userimport, Adminimport
beth = Userimport("Beth","Tango",45,"Cookies")
beth.describeuser() #Beth Tango is 45 years old.  Favorite food is Cookies.
ida = Admin("Ida","Whatney",39,"Dim Sum")
ida.showprivileges() #return ['can add post', 'can delete post', 'can ban user', 'all access']
from ch9classesadmintaketwo import Adminimport2
from ch9usertaketwo import Userimport2
beth2 = Userimport2("Beth2","Tango2",452,"Cookies2")
beth2.describeuser() #Beth2 Tango2 is 452 years old.  Favorite food is Cookies2.
ida2 = Adminimport2("Ida2","Whatney2",392,"Dim Sum2")
ida2.showprivileges() #return ['can add post', 'can delete post', 'can ban user', 'all access']
print("\n")

#order list order dictionary keep track of order
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"
print(favorite_languages) #print OrderedDict([('jen', 'python'), ('sarah', 'c'), ('edward', 'ruby'), ('phil', 'python')])
for name, language in favorite_languages.items():
	print(name+ "'s favorite language is " +language+ ".")