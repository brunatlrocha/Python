"""Bruna Thalia Lima da Rocha"""
"""Student Number: 041-105-020"""

from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

blue = (0,0,255)

def switchLedsOn(cp, leds = None, color = (0,0,0)):
    for i in range(leds):
        cp.pixels[i] = color
# Function to get user's choice and validate it

while True:
        number = input("Number of LED: ")
        try:
            number = int(number)
            if 0 < number <= 10:
                switchLedsOn(cp, number, blue)
                restart = input("Do you want to play again? y/n: ")
                off = restart.lower()
                if off == "n":
                    switchLedsOn(cp, number)
                    print("Bye")
                    break
                else:
                    print ("starting game again")
                    switchLedsOn(cp, number)
                    done = False
            else:
                print("Put a number between 1 - 10")
        except:
            print("Invalid input :(")
