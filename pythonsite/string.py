#!/usr/bin/python

str = 'Hello World!'
newStr = str

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[0:1])     # Prints characters starting from 3rd to 5th
print (str[2:56])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (3 * str)      # Prints string two times
print (str + "TEST") # Prints concatenated string
print (str[:-2])
print (str[-2:])
print (str[2:-2])

# str[0] = 'B'
print (str)
# print (str[56])

print ("My name is %s and weight is %d kg!" % ('Zara', 21) )

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

print ('C:\\nowhere')
print (r'C:\\nowhere')

text = ('Put several strings within parentheses '
            'to have them joined together.')
print (text) 
