import fibo
import imp


fibo.fib(1000)

localfib2 = fibo.fib2

series = localfib2(1000)

imp.reload(fibo)

print (series)

import sys
# The variable sys.path is a list of strings that determines the interpreter’s search path for modules
print (sys.path)
print (fibo.__name__)
print ("Symbols defined in fibo :\n", dir(fibo))
print ("Symbols defined in sys : \n", dir(sys))
print ("Symbols in the current scope : \n" , dir())

# from lib import routines
from lib import routines
routines.add(2,3)
