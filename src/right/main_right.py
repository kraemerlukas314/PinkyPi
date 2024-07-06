import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

key_map_right = {
    # PIN: (Keycode to press, already Pressed?, timestamp when it was pressed in ns)
    "28": (Keycode.Z, False, 0),
    "21": (Keycode.H, False, 0),
    "17": (Keycode.N, False, 0),
    "27": (Keycode.U, False, 0),
    "19": (Keycode.J, False, 0),
    "16": (Keycode.M, False, 0),
    "26": (Keycode.I, False, 0),
    "20": (Keycode.K, False, 0),
    "18": (54, False, 0),
    "22": (Keycode.O, False, 0),
    "7": (Keycode.L, False, 0),
    "6": (55, False, 0),
    "3": (Keycode.P, False, 0),
    "9": (Keycode.O, False, 0),  # Ö
    "15": (Keycode.MINUS, False, 0),
    "2": (Keycode.U, False, 0),  # Ü
    "8": (Keycode.A, False, 0),  # Ä
    "10": (57, False, 0),
    "11": (57, False, 0),  # placeholder
    "13": (Keycode.CONTROL, False, 0),
    "14": (42, False, 0),
    "12": (44, False, 0)
}

# Initialize all pins as input with pull-up resistors
for pin_string in key_map_right.keys():
    pin_number = "GP" + pin_string
    pin = getattr(board, pin_number)
    pin = digitalio.DigitalInOut(pin)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    keycode, pressed, timestamp = key_map_right[pin_string]
    key_map_right[pin_string] = (pin, keycode, pressed, timestamp)

while True:
    current_time = time.monotonic_ns()  # Get the current time in nanoseconds
    
    for pin_string, (pin, keycode, pressed, timestamp) in key_map_right.items():
        if not pin.value:  # Key is pressed (pin is low)
            if not pressed:  # key was not previously pressed
                kbd.press(keycode)
                key_map_right[pin_string] = (pin, keycode, True, current_time)
            else:  # Key is already pressed
                if current_time - timestamp > 50 * 1_000_000:  # 50ms in nanoseconds
                    kbd.press(keycode)  # Continuously send key press
                    key_map_right[pin_string] = (pin, keycode, True, current_time)  # Update timestamp to current time
        else:  # Key is released
            if pressed:  # Key was previously pressed
                kbd.release(keycode)
                key_map_right[pin_string] = (pin, keycode, False, 0)

