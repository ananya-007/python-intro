from . import A

print ("Initialising module B")

def increment (a):
	# print ("add method called" " inside module B")
	return A.increment(a)