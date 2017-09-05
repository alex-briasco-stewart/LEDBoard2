import sys
import time

from neopixel import *

WAIT_MS = 100
NUMROWS = 7
NUMCOLS = 30

# col = Color(0, 0, 255)
# off = Color(0, 0, 0)

LED_COUNT      = 210      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2812_STRIP

# def Color(red, green, blue, white = 0):
# 	"""Convert the provided red, green, blue color to a 24-bit color value.
# 	Each color component should be a value 0-255 where 0 is the lowest intensity
# 	and 255 is the highest intensity.
# 	"""
# 	return (white << 24) | (red << 16)| (green << 8) | blue

def copyToBoard(ledArr, strip):
    #PRECONDITION: ledArr has dimensions equal to [NUMCOLS, NUMROWS]
    for i in range(NUMROWS):
        for j in range(NUMCOLS):
            if i%2 == 0 :#fill row going to the right
                strip.setPixelColor(i*NUMCOLS+j, ledArr[i][j])
                # if(ledArr[i][j)%len(ledArr[0])]==1):
                #     strip.setPixelColor(i*NUMCOLS+j, col)
                # else:
                #     strip.setPixelColor(i*NUMCOLS+j, off)
            else:
                strip.setPixelColor(i*NUMCOLS+NUMCOLS-j-1, ledArr[i][j])
                # if(ledArr[i][(step+j)%len(ledArr[0])]==1):
                #     strip.setPixelColor(i*NUMCOLS+NUMCOLS-j-1, col)
                # else:
                #     strip.setPixelColor(i*NUMCOLS+NUMCOLS-j-1, off)
    strip.show()

def wheel(i):
    if (i<85):
        return Color(i*3, 255-i*3, 0)
    elif (i<170):
        i -= 85
        return Color(255-i*3, 0, i*3)
    else:
        i -= 170
        return Color(0, i*3, 255-i*3)

def printBoardToTerminal(ledArr):
    for i in range(len(ledArr)):
        print ledArr[i]

def initBoardArr(ledArr, height, width):
    for i in range(height):
        ledArr.append([])
        for j in range(width):
            ledArr[i].append(0)

# If not changing fast enough, consider multiplying i - the count term
# If different pixles aren't different enough, multiply the term that changes with board position

def horizontalRainbow(ledArr, count, delay, strip):
    for i in range(count):
        for idx in range(NUMCOLS):
            col = wheel((2*idx + 2*i)%256)
            for j in range(NUMROWS):
                ledArr[j][idx] = col
        copyToBoard(ledArr, strip)
        time.sleep(delay)
def verticalRainbow(ledArr, count, delay, strip):
    for i in range(count):
        for idx in range(NUMROWS):
            col = wheel((2*idx + 2*i)%256)
            for j in range(NUMCOLS):
                ledArr[idx][j] = col
        copyToBoard(ledArr, strip)
        time.sleep(delay)
def diagRainbow(ledArr, count, delay, strip):
    for i in range(count):
        for idxv in range(NUMROWS):
            for idxh in range(NUMCOLS):
                ledArr[idxv][idxh] = wheel((2*idxv+2*idxh+2*i)%256)
        copyToBoard(ledArr, strip)
        time.sleep(delay)




def rainbows(seconds, strip):
    #functions to implement and cycle through:
    # progress bar that fdills up as block ends?
    # find more online
    ledArr = []
    initBoardArr(ledArr, NUMROWS, NUMCOLS)
    horizontalRainbow(ledArr, 1000, seconds/3.0/1000.0, strip)
    verticalRainbow(ledArr, 1000, seconds/3.0/1000.0, strip)
    diagRainbow(ledArr, 2000, seconds/3.0/1000.0, strip)
