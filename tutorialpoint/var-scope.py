total = 0; # This is global variable.
globalA = 10
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2 # Here total is local variable.
   print ("Inside the function local total : ", total)
   print ("Inside the function globalA : ", globalA)
   return total

globalA = 5
# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total )