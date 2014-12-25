letters = ['a', 'b', 'c', 'd', 'e', 'f']
print (letters)
print (len(letters))
letters.append('g')
print (letters)

#Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)


letters[2:5] = ['C', 'D']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []

#Nesting of lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)
print (x[0])
print (x[0][1])

##List operations
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print (a)

print (a.index(333))
a.remove(333)
print (a)
a.reverse()
a.sort()
print (a.pop())

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
# The first to arrive now leaves
print (queue.popleft())
# The second to arrive now leaves
print (queue.popleft())
print (queue) # Remaining queue

#Deleting elements from a list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print (a)

del a[2:4]
print (a)

del a[:]
print (a)