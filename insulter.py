#Max Low
#9-15-17
#insluter.py -- 5 random insults

from random import randint

insultNum = randint(1,5)

name = input('Enter your name')

if insultNum == 1:
    print('You Suck at life')
if insultNum == 2:
    print('Everyone is smarter than you')
if insultNum == 3:
    print('You are a terrible programmer')
if insultNum == 4:
    print(name, ', well thats a terrible name')
if insultNum == 5:
    print('The world hates you')
