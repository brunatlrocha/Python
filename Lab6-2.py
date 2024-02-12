# Bruna Rocha
import time
from adafruit_circuitplayground import cp

morse_code_dict = {
    'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**', 'E': '*', 'F': '**-*', 'G': '--*', 'H': '****',
    'I': '**', 'J': '*---', 'K': '-*-', 'L': '*-**', 'M': '--', 'N': '-*', 'O': '---', 'P': '*--*',
    'Q': '--*-', 'R': '*-*', 'S': '***', 'T': '-', 'U': '**-', 'V': '***-', 'W': '*--', 'X': '-**-',
    'Y': '-*--', 'Z': '--**',
    '1': '*----', '2': '**---', '3': '***--', '4': '****-', '5': '*****',
    '6': '-****-', '7': '--***', '8': '---**', '9': '----*', '0': '-----',
    '.': '--*-', ',': '--**--', ':': '---***', '?': '--**--',
}

def switchLedsOn(cp, color=(255,255,255), leds=10):
        for i in range(leds):
            cp.pixels[i] = color

def turnOffLeds(cp, color=(0,0,0), leds=10, delay=1):
    for i in range(leds):
        cp.pixels[i] = color
    cp.pixels.show()
    time.sleep(delay * 1)
    turnOffLeds(cp)

def Dot(cp, delay=1):
    switchLedsOn(cp, (102, 0, 51))
    time.sleep(delay * 1)
    turnOffLeds(cp)

def Dash(cp, delay=1):
    switchLedsOn(cp, (50, 8, 184))
    time.sleep(delay * 3)
    turnOffLeds(cp)

def betweenLetters(cp, delay=1):
    turnOffLeds(cp)
    time.sleep(delay * 3)

def betweenWords(cp, delay=1):
    turnOffLeds(cp)
    time.sleep(delay * 7)
    
def CPMorseCode():
    while True:
        try:
            code = input('Enter Morse Code (   . - , only): ')
            
            for symbol in code:
                if symbol == '.':
                    Dot(cp)
                elif symbol == '-':
                    Dash(cp)
                elif symbol == ',':
                    betweenLetters(cp)
                elif symbol == ' ':
                    betweenWords(cp)
                else: print('Invalid choice. Try again')
        except ValueError:
                print('Invalid input')
        
        except KeyboardInterrupt:
            print("\n Existing Morse Code.")
            break
        
if __name__ == "__main__":
    CPMorseCode()