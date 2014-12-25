#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)

def increment( num):
	num = num + 1
	return num  

# Now you can call printme function
printme("I'm first call to user defined function!");
printme("Again second call to the same function");

a = 3
increment (a)
print ("Value of a after function call is ", a)

# Function definition is here ..pass be reference
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)