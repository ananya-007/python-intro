items = [1, 2, 3, 4, 5]
squared = []
for x in items:
	squared.append(x ** 2)
print (squared)


## Custom map function
def mymap(aFunc, aSeq):
	result = []
	for x in aSeq: result.append(aFunc(x))
	return result

def sqr(x): return x ** 2

squared =  mymap(sqr, items)
print (squared)

# Since it's a built-in, map is always available and always works the same way.
# It also has some performance benefit because it is usually faster than a manually coded for loop.
# On top of those, map can be used in more advance way. For example, given multiple sequence arguments, 
# it sends items taken form sequences in parallel as distinct arguments to the function:

squared = list (map (sqr, items))
print (squared)

squared = list(map((lambda x: x **2), items))
print (squared)

# The syntax of map function looks like this
# map(aFunction, aSequence)

def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = list(map(lambda x: x(r), funcs))
    print (value)

# Advanced usage of map
powered = list(map(pow,[2, 3, 4], [10, 11, 12]))
print (powered)

filtered = list( filter((lambda x: x < 0), range(-5,5)))
print (filtered)

from functools import reduce

# Custom version of reduce
def myreduce(fnc, seq):
	tally = seq[0]
	for next in seq[1:]:
		tally = fnc(tally, next)
	return tally

result = myreduce( (lambda x, y: x * y), items)
print (result)
result = reduce ((lambda x, y : x * y) , items)
print (result)

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
print (' '.join(L))