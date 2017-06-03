from ch9classesadminuser import User

class Admin(User):
	def __init__(self,first_name, last_name, email, hobby):
		super().__init__(first_name, last_name, email, hobby)
		self.privileges = Privileges()
class Privileges():
	def __init__(self):
		privileges = ["can add post, too","can delete post, too","can ban user, too"]
		self.privileges = privileges
		print(self.privileges)