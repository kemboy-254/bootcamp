class Dog:
  species = "Canis Familiaris"
  def __init__(self, name, age, color):
    self.name = name
    self.age = age
    self.color = color
    
buddy = Dog("Buddy", 9, "Brown")
miles = Dog("Miles", 4, "White")


print(buddy.name,"is",buddy.age,"years old and he is",buddy.color,"in color")
print(miles.name,"is",miles.age,"years old and he is",miles.color,"in color")
print("Both",buddy.name,"and",miles.name,"belong to the",Dog.species,"species")