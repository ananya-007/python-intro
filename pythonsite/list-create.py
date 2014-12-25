squares = []
for x in range(10):
     squares.append(x**2)
print (squares)

# Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:
print(x)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
print (squares)

# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
# For example, this listcomp combines the elements of two lists if they are not equal:

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (combs)

# This is equivalent to 
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print (combs)       

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print ([x*2 for x in vec])

# filter the list to exclude negative numbers
print ([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec]) 

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print ([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print ([(x, x**2) for x in range(6)]) 

# the tuple must be parenthesized, otherwise an error is raised
# print ([x, x**2 for x in range(6)])


# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print ([num for elem in vec for num in elem])

from math import pi
print ([str(round(pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print (matrix)

matrixT = [[row[i] for row in matrix] for i in range(4)]
print(matrixT)

# As we saw in the previous section, the nested listcomp is evaluated in the context of the for that follows it, so this example is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print (list(zip(*matrix)))