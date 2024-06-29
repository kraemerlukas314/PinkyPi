### CODE FOR LEFT HALF ###

import board
import digitalio
import time

clock = digitalio.DigitalInOut(board.GP4)
clock.direction = digitalio.Direction.OUTPUT

data = digitalio.DigitalInOut(board.GP5)
data.direction = digitalio.Direction.OUTPUT

trigger_pin = digitalio.DigitalInOut(board.GP2)
trigger_pin.direction = digitalio.Direction.INPUT
trigger_pin.pull = digitalio.Pull.UP

led_pin = digitalio.DigitalInOut(board.GP25)
led_pin.direction = digitalio.Direction.OUTPUT

freq = 1000 # communication frequency in hz

# function to send any number to the other Pico
def send_data(number, freq):
    for i in range(number):
        bit = (number >> i) & 0x01
        clock.value = True
        data.value = bit
        time.sleep(1/freq)
        clock.value = False
      
while True:
    while trigger_pin.value:
        pass
    send_data(5, freq)
