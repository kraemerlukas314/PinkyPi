import board
import digitalio
import time

clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.OUTPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.OUTPUT

trigger_pin = digitalio.DigitalInOut(board.GP2)
trigger_pin.direction = digitalio.Direction.INPUT
trigger_pin.pull = digitalio.Pull.UP

led_pin = digitalio.DigitalInOut(board.GP25)
led_pin.direction = digitalio.Direction.OUTPUT

freq = 1000000000 # communication frequency in hz
    
# function to send any number to the other Pico
# 5 = 10100
def send_data(number, freq):
    for i in range(5):
        bit = (number >> i) & 0x01
        clock_pin.value = True
        data_pin.value = bit
        time.sleep(1/freq*0.5)
        clock_pin.value = False
        time.sleep(1/freq*0.5)
        
while True:
    while trigger_pin.value:
        pass
    send_data(27, freq)
    time.sleep(0.5)

