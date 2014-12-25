# You can use the lambda keyword to create small anonymous functions. These functions are called anonymous because they are not declared in the standard manner by using the def keyword.

# Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

# An anonymous function cannot be a direct call to print because lambda requires an expression.


# Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function stack allocation during invocation for performance reasons.


globalA = 10
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2 + globalA;
 

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
globalA = 5
print ("Value of total : ", sum( 20, 20 ))

def make_incrementor(n):
    return lambda x: x + n

def sec_incrementer():
	secret = 5
	return lambda x : x + secret

f1 = make_incrementor(1)
f2 = make_incrementor(2)
fs = sec_incrementer()

print (f1(2))
print (f2(2))
print (fs(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print (pairs)