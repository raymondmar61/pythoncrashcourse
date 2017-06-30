from ch9classescartaketwo import Carimport

#Inheritance
class ElectricCar(Carimport): #the name of the parent class must be in parentheses
	def __init__(self, make, model, year):
		super().__init__(make, model, year) #super() makes connection between parent Car and child ElectricCar
		self.batterysize = 70
	def describebattery(self): #prints information about batterysize
		print("This car has a " +str(self.batterysize)+ "-kWh battery.")