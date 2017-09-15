#Max Low
#9-14-17
#fortuneTeller.py -- give a fortune based on color and number

color = input('Pick red or blue') 
num = int(input('Pick a number from 1-4: '))

if color == 'red':
    if num == 1:
        print('You will win the lottery')
    elif num == 2:
        print('Your life will be terribe')
    elif num == 3:
         print('You will live a long happy life')
    elif num == 4:
        print('You will be a terrific programmer')
    else:
        print('invalid number')
        
elif color == 'blue':
    if num == 1:
        print('You will drown in a river')
    elif num == 2:
        print('You will become old and wise')
    elif num == 3:
         print('You will achieve your goals')
    elif num == 4:
        print('You are a terrible programmer')
    else:
        print('invalid number')
        
else:
    print('invalid color')
