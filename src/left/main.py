### CODE FOR LEFT HALF ###

import board
import digitalio
import time
import math
clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.OUTPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.OUTPUT

trigger_pin = digitalio.DigitalInOut(board.GP2)
trigger_pin.direction = digitalio.Direction.INPUT
trigger_pin.pull = digitalio.Pull.UP

freq = 1 # communication frequency in bits/second

# function to send any number to the other Pico
def send_data(number, freq):
    for i in range(math.ceil(math.log(8 + 1) / math.log(2))): # loop through every bit
        bit = (number >> i) & 0x01
        clock_pin.value = True
        data_pin.value = bit
        time.sleep(1/freq)
        clock_pin.value = False
      
while True:
    for i in range(100):
        while trigger_pin.value:
            pass
        send_data(i, freq)
        time.sleep(0.5)
