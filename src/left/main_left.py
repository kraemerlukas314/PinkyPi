import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

key_map_left = {
    "26": (Keycode.ESCAPE, False, 0),
    "27": (Keycode.TAB, False, 0), # tab
    "28": (Keycode.TAB, False, 0), # <
    "22": (Keycode.Q, False, 0),
    "21": (Keycode.A, False, 0),
    "15": (Keycode.Y, False, 0),
    "20": (Keycode.W, False, 0),
    "10": (Keycode.S, False, 0),
    "14": (Keycode.X, False, 0),
    "6": (Keycode.E, False, 0),
    "7": (Keycode.D, False, 0),
    "13": (Keycode.C, False, 0),
    "3": (Keycode.R, False, 0),
    "9": (Keycode.F, False, 0),
    "12": (Keycode.V, False, 0),
    "2": (Keycode.T, False, 0),
    "8": (Keycode.G, False, 0),
    "11": (Keycode.B, False, 0),
    "18": (Keycode.ALT, False, 0), # unten links
    "17": (227, False, 0), # windows key
    "16": (227, False, 0),
    "19": (227, False, 0)
}

# Initialize all pins as input with pull-up resistors
for pin_string in key_map_left.keys():ffgghallo das ist ein kleiner test
    pin_number = "GP" + pin_string
    pin = getattr(board, pin_number)
    pin = digitalio.DigitalInOut(pin)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    keycode, pressed, timestamp = key_map_left[pin_string]
    key_map_left[pin_string] = (pin, keycode, pressed, timestamp)

while True:
    current_time = time.monotonic_ns()  # Get the current time in nanoseconds
    
    for pin_string, (pin, keycode, pressed, timestamp) in key_map_left.items():
        if not pin.value:  # Key is pressed (pin is low)
            if not pressed:  # key was not previously pressed
                kbd.press(keycode)
                key_map_left[pin_string] = (pin, keycode, True, current_time)
            else:  # Key is already pressed
                if current_time - timestamp > 50 * 1_000_000:  # 50ms in nanoseconds
                    kbd.press(keycode)  # Continuously send key press
                    key_map_left[pin_string] = (pin, keycode, True, current_time)  # Update timestamp to current time
        else:  # Key is released
            if pressed:  # Key was previously pressed
                kbd.release(keycode)
                key_map_left[pin_string] = (pin, keycode, False, 0)


