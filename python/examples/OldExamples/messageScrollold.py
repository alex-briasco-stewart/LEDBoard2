

import sys
import time

from neopixel import *
from constants import alphabet, letterSpace, space

WAIT_MS = 100
NUMROWS = 5
NUMCOLS = 48

col = Color(0, 0, 255)
off = Color(0, 0, 0)

LED_COUNT      = 240      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2812_STRIP

def copyLetter(loc, dest, let):
    #loc is the int location of where to start the copy
    #dest is the destination array with length L (0<=loc<L)
    #let is the character to copy (from alphabet)
    #prereqthat dest and let are the same height
    for i in range(len(let)):   #rows
        for j in range(len(let[i])):    #columns
            dest[i][j+loc] = let[i][j]

    return loc + len(let[0]);

def printToBoard(step, ledArr, strip):
    #print step
    # step == offset
    for i in range(NUMROWS):
        for j in range(NUMCOLS):
            if i%2 == 0 :#fill row going to the right
                if(ledArr[i][(step+j)%len(ledArr[0])]==1):
                    strip.setPixelColor(i*NUMCOLS+j, col)
                else:
                    strip.setPixelColor(i*NUMCOLS+j, off)
            else:
                if(ledArr[i][(step+j)%len(ledArr[0])]==1):
                    strip.setPixelColor(i*NUMCOLS+NUMCOLS-j-1, col)
                else:
                    strip.setPixelColor(i*NUMCOLS+NUMCOLS-j-1, off)
    strip.show()



if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    message = " boi boi ".lower()
    ledArr = [[], [], [], [], []]
    loc = 0

    for i in range(len(message)):
        toCopy = alphabet[message[i]]
        letSpace = 0

        if toCopy!=space:
            letSpace+=1

        for a in range(5):
            for b in range(len(toCopy[a])+letSpace):
                ledArr[a].append(0)

        loc = copyLetter(loc, ledArr, toCopy)
        if letSpace==1:
            loc = copyLetter(loc, ledArr, letterSpace)

    for c in range(len(ledArr)):
        print ledArr[c]
    print "Ctrl-C to exit."
    count = 0;
    while True:
        printToBoard(count, ledArr, strip)
        count+=1
        time.sleep(WAIT_MS/1000.0)
