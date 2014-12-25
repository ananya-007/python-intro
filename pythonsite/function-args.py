def fib2(n): # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result

f100 = fib2(100)
print (f100)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

ask_ok('Do you really want to quit?')

# The default values are evaluated at the point of function definition in the defining scope, so that

i = 5

def f(arg=i):
    print(arg)

i = 6
f()     


#Default value is evaluated only once, so be careful while using mutable objects
def f(a, L=[]):
    L.append(a)
    return L

print (f(1))
print (f(2))
print (f(3))

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print (f(1))
print (f(2))
print (f(3))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# In a function call, keyword arguments must follow positional arguments
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument   

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")         

# Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

def concat(*args, sep="/"):
   return sep.join(args)

print (concat("earth", "mars", "venus"))
print (concat("earth", "mars", "venus", sep="."))

# Unpacking Argument Lists
seq = list(range(3, 6))            # normal call with separate arguments
print (seq)
args = [3, 6]
seq = list(range(*args))            # call with arguments unpacked from a list
print (seq)

# n the same fashion, dictionaries can deliver keyword arguments with the **-operator:
def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)     