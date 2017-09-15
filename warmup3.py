#Max Low
#9-15-17
# warmup3.py -- divisible by 3, 2, both, neither

num = int(input('Enter a number: '))

if num % 2 == 0:
    if num % 3 == 0:
        print(num, 'is divisible by 2 and 3')
    else:
        print(num, 'is divisible by 2')

elif num % 3 == 0:
    if num % 3 ==0:
        print(num, 'is divisible by 3')
        
else:
    print(num,'is not divisible by 2 or 3')
        

