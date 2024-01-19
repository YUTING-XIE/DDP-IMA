# 1. roll_dice from 1-6
import random  #shold add the random bexcasue Python does not have a random function

def roll_dice():
    return random.randrange(1,7)

print(roll_dice())  
print(roll_dice())
print(roll_dice())


#2. light on/off
def toggle_light(light_on): 
    if light_on == True:  # very important, this place can be [if light_on:]
        light_on = False  # True or False are [boolean] 
        print("Light turned off.")
    else:
        light_on = True 
        print("Light turned on.")
        return light_on

toggle_light(True)
 #: True: Non-zero numbers, non-empty strings, non-empty lists, and generally most objects are truthy.
 #: False: 0, None, empty strings "", empty lists [], empty tuples (), and empty dictionaries {} are falsy. 
