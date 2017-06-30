class Carimport():
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

#Instances as attributes
class Battery2import():
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
class ElectricCar2import(Carimport):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery2import()