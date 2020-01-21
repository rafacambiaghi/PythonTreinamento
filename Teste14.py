#l = [1,2,3]
#l.count(2)
#print(type(1))
#print(type([]))
#print(type(()))
#print(type({}))

#class Exemplo(object):
#    pass
#x = Exemplo()
#print(type(x))


#class Dog(object):
# def __init__(self, breed):
#   self.breed = breed
#sam = Dog(breed= 'Lab')
#frank = Dog(breed= 'Huskie')
#print(sam.breed)
#print(frank.breed)   

#class Dog(object):
# species = 'mammal'
# def __int__(self, breed, name):
#   self.breed = breed
#   self.breed = name
#sam = Dog('Lab', 'Sam')
#print(sam.name)
#print(sam.species)

class Circle(object):
 pi = 3.14
 def __init__(self, radius=1):
  self.radius = radius

 def area(self):
  return self.radius * self.radius * Circle.pi

 def setRadius(self, radius):
    self.radius = radius

 def getRadius(self):
  return self.radius

c = Circle()

c.setRadius(2)
print('O raio é:', c.getRadius())
print('A área é:', c.area())
