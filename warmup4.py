#Max Low
#9-18-17
#warmup.py - buzz game on 7's or divisible by 7

buzz = int(input('Enter a number'))
if buzz // 7 == 0:
    print('buzz')
buzz = str(buzz)
if '7' in buzz:
    print('buzz')
else:
    print(buzz)