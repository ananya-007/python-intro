# Raising an exception

# The sole argument to raise indicates the exception to be raised. This must be either an exception instance or
# an exception class (a class that derives from Exception).

# raise NameError('HiThere')

# If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement
# allows you to re-raise the exception:
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise

# Defining clean-up actions

# A finally clause is always executed before leaving the try statement, whether an exception has occurred or not.
# When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in a except or else clause),
# it is re-raised after the finally clause has been executed.
# The finally clause is also executed “on the way out” when any other clause of the try statement is left via a break, continue or return statement.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)

divide(2, 0)

# divide("2", "1")

fileName = 'sample.txt'

#### Predefined Clean-up Actions
for line in open(fileName):
    print(line, end="")
# The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing    

# The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.
with open(fileName) as f:
    for line in f:
        print(line, end="")