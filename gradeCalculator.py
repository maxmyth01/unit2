#Max Low
#9-13-17
#gradeCalculator -- convert a numerical grade to a letter

grade = float(input('Input your grade: '))

if grade > 100:
    print('Show off')

elif grade >=90:
    print('You got an A')
    
elif grade >=80:
    print('You got a B')

elif grade >=70:
    print('You got a C')

elif grade >=60:
    print('You got a D')
    
else:
    print('You got a failing grade')