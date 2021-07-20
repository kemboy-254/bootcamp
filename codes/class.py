"""Python program fo instanciating a class"""

class Dog(object):
	"""docstring for Dog"""
	attr1 = "mammal"
	attr2 = "dog"
	def fun(self): #function associated with a class
		#super(Dog, self).__init__()
		#self.arg = arg

		print("i'm a ", self.attr1)
		print("i'm a ", self.attr2)

Rodger = Dog()

#accessong class attributes
#and method throiugh objects
print(Rodger.attr1)
Rodger.fun()
		