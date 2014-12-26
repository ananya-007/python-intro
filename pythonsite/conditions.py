a = 10
b = 12
c = 13

# Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.
if (a < b == c):
	print (True)
else:
	print (False)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print (non_null)

# When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.
# It is possible to assign the result of a comparison or other Boolean expression to a variable.


# Comparing sequences and other types
# Sequence objects may be compared to other objects with the same sequence type. 

print ((1, 2, 3)              < (1, 2, 4))
print ([1, 2, 3]              < [1, 2, 4])
print ('ABC' < 'C' < 'Pascal' < 'Python')
print ((1, 2, 3, 4)           < (1, 2, 4))
print ((1, 2)                 < (1, 2, -1))
print ((1, 2, 3)             == (1.0, 2.0, 3.0))
print ((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))