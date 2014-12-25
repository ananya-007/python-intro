# A tuple consists of a number of values separated by commas, for instance:
t = 12345, 54321, 'hello!'
print (t[0])
print (t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print (u)

# Tuples are immutable:
# t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print (v)

# Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
# Tuples are immutable, and usually contain an heterogeneous sequence of elements that are accessed via unpacking (see later in this section) 
# or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous 
# and are accessed by iterating over the list.
empty = ()
singleton = 'hello',    # <-- note trailing comma
print (len(empty))

print (len(singleton))

print (singleton)

# Below is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. 
t = 12345, 54321, 'hello!'

# The reverse operation is also possible
# This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side. 
# Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence.
#  Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.
x, y, z = t
t = [1,2,3]
x,y,z = t
print (x,y,z)