"""Bruna Thalia Lima da Rocha"""
"""Student Number: 041-105-020"""

from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.03

def switchLedsOn(cp, color, leds = 10):
    for i in range(leds):
        cp.pixels[i] = color
        
def displayColorForTemperature(temperature=20):
    if -40 <= temperature < -10:
        color = (0, 0, 139)
    elif -10 <= temperature < 0:
        color = (0, 0, 255)
    elif 0 <= temperature < 15:
        color = (0, 255, 0)
    elif 15 <= temperature < 22:
        color = (0, 128, 0)
    else:
        color = (255, 0, 0)
        
    print("Temperature in degrees Celsius:", temperature)
    print("Color:", color)
    
    switchLedsOn(cp, color)

displayColorForTemperature(temperature = cp.temperature)
    

