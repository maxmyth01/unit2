#Max Low
#9-25-17
#quiz2.py -- numbers , bigger smaller same, divisible by 3, product and correct person

numone = int(input('Enter a number: '))
numtwo = int(input('Enter a 2nd number: '))

if numone > numtwo:
    print('The first number is bigger')
elif numtwo > numone:
    print('The second number is bigger')
else:
    print('The numbers are the same')

   
if numone % 3 == 0 and numtwo % 3 == 0:
    print('They are both divisible by 3')
elif numone % 3 == 0:
    print('Only the first number is divisible by three')
elif numtwo % 3 == 0:
    print('Only the second number is divisible by three')
else:
    print('Neither number is divisible by 3')

product = int(input('What is the product of your two numbers?: '))
if product == numone*numtwo:
    print('correct')
else:
    print('incorrect')