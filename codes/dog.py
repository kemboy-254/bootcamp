
# Python3 program to
# demonstrate instantiating
# a class
 
 
class Dog:
     
    # A simple class
    # attribute
    species = "Canis Familiaris"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.species)
        
 
# Driver code
# Object instantiation
Rodger = Dog()
 
# Accessing class attributes
# and method through objects
print(Rodger.species)
Rodger.fun()