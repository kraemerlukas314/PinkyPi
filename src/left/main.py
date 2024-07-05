import board
import digitalio
import time

clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.OUTPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.OUTPUT

def send_data(number, freq):
    for i in range(5):
        bit = (number >> i) & 0x01
        clock_pin.value = True
        data_pin.value = bit
        time.sleep(1/freq*0.5)
        clock_pin.value = False
        time.sleep(1/freq*0.5)

# Function to initialize a pin as input with pull-up
def init_pin_pullup(pin_number):
  pin = digitalio.DigitalInOut(getattr(board, f"GP{pin_number}"))
  pin.direction = digitalio.Direction.INPUT
  pin.pull = digitalio.Pull.UP
  return pin

# Initialize all pins in the dictionary as input with pull-ups
pins = {
  26: init_pin_pullup(26),
  27: init_pin_pullup(27),
  28: init_pin_pullup(28),
  22: init_pin_pullup(22),
  21: init_pin_pullup(21),
  15: init_pin_pullup(15),
  20: init_pin_pullup(20),
  10: init_pin_pullup(10),
  14: init_pin_pullup(14),
  6: init_pin_pullup(6),
  7: init_pin_pullup(7),
  13: init_pin_pullup(13),
  3: init_pin_pullup(3),
  9: init_pin_pullup(9),
  12: init_pin_pullup(12),
  2: init_pin_pullup(2),
  8: init_pin_pullup(8),
  11: init_pin_pullup(11),
  18: init_pin_pullup(18),
  17: init_pin_pullup(17),
  16: init_pin_pullup(16),
  19: init_pin_pullup(19),
}

# Previous pin states for comparison
previous_pin_states = {pin_number: False for pin_number in pins}  # Initialize all to False

# Communication frequency (adjust based on your setup)
freq = 100  # Hz

while True:
  # Loop through all pins in the dictionary
  for pin_number, pin in pins.items():
    # Read the current pin value
    current_value = pin.value

    # Check for state change (LOW to HIGH or HIGH to LOW)
    if current_value != previous_pin_states[pin_number]:
        if not current_value:
            send_data(pin_number, freq)
        previous_pin_states[pin_number] = current_value  # Update previous state

  # Add a small delay to avoid excessive loop frequency
  time.sleep(0.01)

