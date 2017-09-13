#Max Low
#9-13-17
#movie.py -- give an age and type of movie you can watch

age = float(input('Enter your age: '))

if age <=8:
    print('You can watch G movies')
elif age <=13:
    print('You can watch PG movies')
elif age <=17:
    print('You can watch PG-13 movies')
else:
    print('You can watch R movies')

