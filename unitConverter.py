#Max Low
#9-14-17
#unitConverter.py - choose a converter

converter = int(input('1) Kilometer to Miles, 2) Kilograms to Pounds, 3) Liters to Gallons, 4)Celsius to Fahrenheit'))
while True:
    if converter < 0 or converter > 4:
        print('Error Invalid Converter Number')

    if converter == 1:
        km_to_mi = float(input('Enter a Distance in Kilometers'))
        print(km_to_mi,'Kilometers is', km_to_mi*0.621371 ,'miles')

    if converter == 2:
        kg_to_lbs = float(input('Enter a mass in Kilograms'))
        print(kg_to_lbs,'kilograms is', kg_to_lbs*2.20462 ,'pounds')
    
if converter == 3:
        L_to_G = float(input('Enter a volume in liters'))
        print(L_to_G,'liters is', L_to_G*0.264172 ,'gallons')
    
if converter == 4:
        C_to_F = float(input('Enter a tempature in celsius'))
        print(C_to_F,'degrees celsius is', (C_to_F*1.8)+32 ,'degrees Fahrenheit')
