import fibo
import imp

fibo.fib(1000)

localfib2 = fibo.fib2

series = localfib2(1000)

imp.reload(fibo)

print (series)

import sys
print (sys.path)
print (fibo.__name__)
print ("Symbols defined in fibo :\n", dir(fibo))
print ("Symbols defined in sys : \n", dir(sys))
print ("Symbols in the current scope : \n" , dir())