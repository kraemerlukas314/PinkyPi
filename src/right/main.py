### CODE FOR RIGHT HALF ###

import board
import digitalio
import time

data = digitalio.DigitalInOut(board.GP5)
data.direction = digitalio.Direction.INPUT
clock = digitalio.DigitalInOut(board.GP4)
clock.direction = digitalio.Direction.INPUT

while True:
    if (data.value):
        if (clock.value):
            print(1, 1)
        else:
            print(0, 1)
    else:
        if (clock.value):
            print(1, 0)
        else:
            print(0, 0)