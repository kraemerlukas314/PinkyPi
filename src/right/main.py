### CODE FOR RIGHT HALF ###

import board
import digitalio
import time

clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.INPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.INPUT

freq = 10 # communication frequency in bits/second

def receive_data(freq):
     # if there is no new clock cycle for 1.5 estimated cycles, communication is probably over
    TIMEOUT = 1.5 * (1 / freq) * 10**9  # in nanoseconds
    communication_end = False
    bits = []
    while not communication_end:
             # wait for half clock cycle to let data line stabilze
            time.sleep(1/freq * 0.5)
            bits.insert(0, data_pin.value)
            print(bits)
            # wait for HL edge (falling)
            while clock_pin.value:
                pass
            hl_edge_timestamp = time.monotonic_ns()
            
            # wait for LH edge (rising) or timeout
            while not clock_pin.value and not communication_end:
                time_passed_since_LH_edge = (time.monotonic_ns() - hl_edge_timestamp) # in ns
                if time_passed_since_LH_edge > TIMEOUT:
                    communication_end = True
    binary_str = ''.join('1' if bit else '0' for bit in bits)
    return int(binary_str, 2)

while True:
    if clock_pin.value:
        print(receive_data(freq))