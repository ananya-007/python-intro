## Below code throw exceptions

# 10 * (1/0)

# 4 + spam*3

# '2' + 2

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")\

# First, the try clause (the statement(s) between the try and except keywords) is executed.
# If no exception occurs, the except clause is skipped and execution of the try statement is finished.
# If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named
#  after theexcept keyword, the except clause is executed, and then execution continues after the try statement.
# If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; 
# if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

# A try statement may have more than one except clause, to specify handlers for different exceptions.
# At most one handler will be executed. 
# Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same try statement.
# An except clause may name multiple exceptions as a parenthesized tuple

# The last except clause may omit the exception name(s), to serve as a wildcard.
# Use this with extreme caution, since it is easy to mask a real programming error in this way! 
# It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well)

import sys
fileName = 'notMyFile.txt'
try:
    f = open(fileName)
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# The try ... except statement has an optional else clause, which, when present, must follow all except clauses.
# It is useful for code that must be executed if the try clause does not raise an exception
fileName = 'sample.txt'
try:
    f = open(fileName, 'r')
except IOError as err:
    print('IOError : {0}'.format(err))
else:
    print(fileName, 'has', len(f.readlines()), 'lines')
    f.close()

# When an exception occurs, it may have an associated value, also known as the exception’s argument. 
# The presence and type of the argument depend on the exception type.
# The except clause may specify a variable after the exception name. The variable is bound to an exception instance with the arguments stored in instance.args.
# For convenience, the exception instance defines __str__() so the arguments can be printed directly without having to reference .args. One may also instantiate an exception first before raising it and add any attributes to it as desired.    
try:
   raise Exception('spam', 'eggs')
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x)
   print('y =', y)

# Exception handlers don’t just handle exceptions if they occur immediately in the try clause, but also if they occur inside functions that
# are called (even indirectly) in the try clause
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

    