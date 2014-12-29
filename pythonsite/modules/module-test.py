from library import B , A
import imp

num = 10

print ('Result from module A is {0}: '.format(A.increment (num)))
print ('Result from module B is {0}: '.format(B.increment (num)))

B.A.step = 20
print ("Setting increment step to {0}".format(A.step))

print ('Result from module A is {0}: '.format(A.increment (num)))
print ('Result from module B is {0}: '.format(B.increment (num)))

print ("IDs of modules A in main and B are {0} , {1}".format(id(A), id(B.A)))

print ("Importing module A again inside main")
imp.reload(A)
print ('Result from module A is {0}: '.format(A.increment (num)))
print ('Result from module B is {0}: '.format(B.increment (num)))