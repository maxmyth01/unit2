#Max Low
#9-15-17
#adventure.py -- two choices

mountain = str(input('You arrive at the foot of a mountain. The climb looks to be hard and gruling and will probably kill you. Do you dare climb the Mountain?(yes or no)'))
if 'yes' in mountain:
    cave = str(input('Good choice, you begin up the mountain as and boulder falls in to the spot you were standing moments ago . . . As you continue higher up you see a bright light coming from a cave up a head. Do you enter the cave?(yes or no)'))
    if 'yes' in cave:
        print('As you explore deeper into the cave walls seem to glow, and the tempature increases but you carry on. Until . . . you being to  . . . pass out from the heat . . . as you fall the the ground, you spot a river of lava deep in the cave, ever increasing in size. You know the end is neigh, as you go unconcious.(GAMEOVER)')
    elif 'no' in cave:
        print('You contine higher up the mountain, as a collum of fire and lava erupts from the cave. You luckly survive and continue higher to the summit. Good for You. You reached the top.(YOU WIN)')
    else:
        print('INVAILD INPUT, GAMEOVER')
elif 'no' in mountain:
    print('Have a nice day, as you begin to walk away from the mountain the ground shakes as an boulder falls twards you, GAMEOVER')
else:
    print('INVAILD INPUT, GAMEOVER')