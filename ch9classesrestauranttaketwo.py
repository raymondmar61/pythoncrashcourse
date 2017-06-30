class Restaurantimport():
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