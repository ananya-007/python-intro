def print_sequence (seq):
	for i in seq:
		print (i, end = ' ')
	print()
x = 5
if x < 0:
     x = 0
     print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('More')

words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

# Loop over a slice copy of the entire list.
for w in words[:]:  
	if len(w) > 6:
		words.insert(0, w)
print (words)

#Ranges
print_sequence(range(5))

print_sequence(range(5,10))

print_sequence(range(0, 10, 3))

print(range(10))

print (list(range(5)))

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
   		print (num , "is a prime number")

for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found a number", num)   		


