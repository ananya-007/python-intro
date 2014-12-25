#!/usr/bin/python

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
else:
	print ('Count is not less than 9')   


for letter in 'Python':     # First Example
   print ('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print ('Current fruit :', fruit)


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :' , index , fruits[index])

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
for item in tinydict:
	print (item)

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
   		print (num , "is a prime number")

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)

for letter in 'Python': 
   if letter == 'h':
      pass # used or stubs
      #print ('This is pass block')
   print ('Current Letter :', letter)   

print ("Good bye!")