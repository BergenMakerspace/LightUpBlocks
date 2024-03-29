# Trinket IO Color Wheel demo
# Welcome to CircuitPython! :)

import board
import adafruit_dotstar as dotstar
import time

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.1)

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
        return (int(pos*3), 0, int(255 - pos*3))

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  i = (i+1) % 256  # run from 0 to 255
  time.sleep(0.001) # make bigger to slow down
