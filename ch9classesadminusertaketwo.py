class Userimport():
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
class Adminimport(Userimport):
	def __init__(self, firstname, lastname, age, favoritefood):
		super().__init__(firstname, lastname, age, favoritefood)
	def showprivileges(self):
		privileges = ["can add post","can delete post","can ban user", "all access"]
		print(privileges)