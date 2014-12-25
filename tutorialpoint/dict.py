#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
copyDict = dict


tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['Name'])      # Prints value for 'one' key

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print (dict)
print (copyDict)
print (dict.items())
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

##Properties of dictionary keys
# should be unique
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'};

print ("dict['Name']: ", dict['Name'])

#Keys must be immutable.
#dict = {['Name']: 'Zara', 'Age': 7}