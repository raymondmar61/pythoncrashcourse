from  ch9usertaketwo import Userimport2
class Adminimport2(Userimport2):
	def __init__(self, firstname, lastname, age, favoritefood):
		super().__init__(firstname, lastname, age, favoritefood)
	def showprivileges(self):
		privileges = ["can add post","can delete post","can ban user", "all access"]
		print(privileges)