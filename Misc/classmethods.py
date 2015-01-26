class Person:
	
	noOfPeople = 0

	def __init__(self):
		self.age = 1
		Person.noOfPeople = Person.noOfPeople + 1
		print ("No of people so far ", Person.noOfPeople)
	
	def static_function(a,step=1):
		return a + step

	def increment_age(self, step=1):
		self.age =  Person.static_function(self.age,step)
		print ("Person's age is " , self.age)


p1 = Person()
p2 = Person()
p1.increment_age(5)


class Kls(object):
    def __init__(self, data):
        self.data = data
 
    def printd(self):
        print(self.data)
 
    @staticmethod
    def smethod(*arg):
        print('Static:', arg)
 
    @classmethod
    def cmethod(*arg):
        print('Class:', arg)

ik = Kls(23)
ik.printd()
ik.smethod()
ik.cmethod()

# Kls.printd() This results in error
Kls.smethod()
Kls.cmethod()