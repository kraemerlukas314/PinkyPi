import board
import digitalio
import time

clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.INPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.INPUT

freq = 1000000000 # communication frequency in hz
# function to receive data from the other Pico
def receive_data(freq):
    received_number = 0
    for i in range(5):
        while not clock_pin.value:
            pass
        time.sleep(1/freq*0.25)
        bit = data_pin.value
        received_number |= (bit << i)
        time.sleep(1/freq*0.5)
    return received_number

while True:
    if clock_pin.value:
        data = receive_data(freq)
        print("Data:", data)
    
