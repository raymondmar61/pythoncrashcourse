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