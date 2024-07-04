import board
import digitalio
import time

# Setup for GPIO5 as input
gpio5 = digitalio.DigitalInOut(board.GP5)
gpio5.direction = digitalio.Direction.INPUT

def received_number():
    """
    Receives the number sent by the left Pico.
    :return: Received number
    """
    # Wait for GPIO5 to go high
    while not gpio5.value:
        time.sleep(0.001)
    
    # Start counting the toggles
    count = 0
    start_time = time.time()
    while time.time() - start_time < 0.05:  # Monitor for 50 milliseconds
        if gpio5.value:
            count += 1
            while gpio5.value:
                pass  # Wait for the pin to go low
    
    return count

# Example usage: receive number
while True:
    if gpio5.value:
        received_num = received_number()
        print("Received number:", received_num)
