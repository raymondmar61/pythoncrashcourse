class User():
	def __init__(self, first_name, last_name, email, hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.hobby = hobby
	def describe_user(self):
		print(self.first_name+ " " +self.last_name+ "\'s email address is " +self.email+ ".  A hobby is " +self.hobby+ ".")