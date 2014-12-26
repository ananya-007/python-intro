tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print (tel)

print (tel['jack'])

del tel['sape']
tel['irv'] = 4127
print (tel)

print (list(tel.keys()))

print (sorted(tel.keys()))

print ('guido' in tel)

print ('jack' not in tel)

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
telNo = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print (telNo)

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
numbers = {x: x**2 for x in (2, 4, 6)}
print (numbers)

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
simple = dict(sape=4139, guido=4127, jack=4098)
print (simple)

