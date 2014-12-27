# Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. 
# Such a file is called a module; definitions from a module can be imported into other modules or into the main module

# A module is a file containing Python definitions and statements.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__

# Fibonacci numbers module
print ("fibo module initialised")

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end='  ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    print (sys.argv)
    fib(int(sys.argv[1]))    