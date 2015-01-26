#Decorator function which returns  new function , by taking an existing function. It uses the given function
def decorator(fn):
	def inner_fn(n):
		return fn(n) + 1
	return inner_fn

def fn(n):
	return (n + 1)

#classical way is to define a new function and passing it to decorator
f = decorator(fn)

print (f(1))
print (f(3))


#short way is to add the decorator function after @
# In the example below, then, decorator is called with f as an argument, and it returns a new function that replaces f
@decorator
def f(n):
    return n + 1

print (f(1))
print (f(3))

def wrap_with_prints(fn):
    # This will only happen when a function decorated
    # with @wrap_with_prints is defined
    print('wrap_with_prints runs only once')
 
    def wrapped():
        # This will happen each time just before
        # the decorated function is called
        print('About to run %s' % fn.__name__)
        # Here is where the wrapper calls the decorated function
        fn()
        # This will happen each time just after
        # the decorated function is called
        print('Done running %s' % fn.__name__)
 
    return wrapped
 
@wrap_with_prints
def func_to_decorate():
    print('Running the function that was decorated.')
 
func_to_decorate()