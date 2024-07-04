import board
import digitalio
import time

# Setup for GPIO5 as output
gpio5 = digitalio.DigitalInOut(board.GP5)
gpio5.direction = digitalio.Direction.OUTPUT

def send_number(number):
    """
    Send a number by toggling the GPIO5 pin.
    :param number: Number between 0-25
    """
    assert 0 <= number <= 25, "Number must be between 0 and 25"
    
    # Pull GPIO5 high to signal start of transmission
    gpio5.value = True
    time.sleep(0.01)  # Ensure the signal is high for a short duration
    
    # Send the number by toggling the GPIO5 pin
    gpio5.value = False
    for _ in range(number):
        gpio5.value = True
        time.sleep(0.0005)  # 1000 Hz frequency, half period
        gpio5.value = False
        time.sleep(0.0005)  # 1000 Hz frequency, half period
    
    # End of transmission
    gpio5.value = False

while True:
    for i in range(5, 25):
        print("sending:", i)
        send_number(i)
        time.sleep(5)
