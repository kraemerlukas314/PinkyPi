### CODE FOR LEFT HALF ###

import board
import digitalio
import time
import math
clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.OUTPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.OUTPUT

led_pin = digitalio.DigitalInOut(board.GP25)
led_pin.direction = digitalio.Direction.OUTPUT

trigger_pin = digitalio.DigitalInOut(board.GP2)
trigger_pin.direction = digitalio.Direction.INPUT
trigger_pin.pull = digitalio.Pull.UP

freq = 1 # communication frequency in bits/second

# function to send any number to the other Pico
def send_data(number, freq):
    for i in range(required_bits(number)): # loop through every bit
        bit = (number >> i) & 0x01
        print(bit)
        clock_pin.value = True
        led_pin.value = True
        data_pin.value = bit
        time.sleep(1/freq)
        clock_pin.value = False
        led_pin.value = False
    print("---")

# returns number of required bits to send number
# number must be >= 0
def required_bits(number):
    if number < 2:
        return 1
    else:
        return math.ceil(math.log(number + 1) / math.log(2))

while True:
    clock_pin.value = 1
    data_pin.value = 0
    led_pin.value = 1
    time.sleep(5)
    clock_pin.value = 0
    data_pin.value = 1
    led_pin.value = 0
    time.sleep(5)
        
while True:
    for i in range(100):
        while trigger_pin.value:
            pass
        send_data(i, freq)
        time.sleep(0.5)
