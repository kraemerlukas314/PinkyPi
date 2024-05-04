import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import board
import digitalio
import time

kbd = Keyboard(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP28)
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if button.value == 0:
        kbd.send(Keycode.SHIFT, Keycode.A)
        time.sleep(0.1)