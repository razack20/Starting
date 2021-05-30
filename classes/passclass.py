#passing classs to another class
class employee:
	def __init__(self, first, last, email):
		self.first = first
		self.last = last
		self.email = email		
class developer(employee):
	pass
d1=developer("mohamad","razack","abdul@123")
print(d1.first)
print(d1.last)

#********************************************************************#
#passing class to another class and creating one new argument
class employee:
	def __init__(self, first, last, email):
		self.first = first
		self.last = last
		self.email = email		
class developer(employee):
	def __init__(self, first, last, email,prog_lang):
		super().__init__(first,last,email)
		self.prog_lang = prog_lang
d1=developer("mohamad","razack","abdul@123","python")
print(d1.prog_lang)
