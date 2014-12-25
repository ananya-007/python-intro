# Function definition is here ...Required arguments
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
#printme()

# Function definition is here
def printinfo( name, age=35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function with keyword arguments
printinfo( age=50, name="miki" )

# Now you can call printinfo function
printinfo( "mouse", 25 )
printinfo("miki")

# Function with variable length argument
# An asterisk (*) is placed before the variable name that will hold the values of all nonkeyword variable arguments
def printVarArgs( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   print ("Variable arguments are")
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printVarArgs( 10 );
printVarArgs( 70, 60, 50 );