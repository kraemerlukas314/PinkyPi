import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

clock_pin = digitalio.DigitalInOut(board.GP4)
clock_pin.direction = digitalio.Direction.INPUT

data_pin = digitalio.DigitalInOut(board.GP5)
data_pin.direction = digitalio.Direction.INPUT

freq = 100  # communication frequency in Hz

kbd = Keyboard(usb_hid.devices)

# Function to receive data from the other Pico
def receive_data(freq):
    received_number = 0
    for i in range(5):
        while not clock_pin.value:
            pass
        time.sleep(1 / freq * 0.25)
        bit = data_pin.value
        received_number |= (bit << i)
        time.sleep(1 / freq * 0.5)
    return received_number

key_map_right = {
    "R28": (Keycode.Z, False),
    "R21": (Keycode.H, False),
    "R17": (Keycode.N, False),
    "R27": (Keycode.U, False),
    "R19": (Keycode.J, False),
    "R16": (Keycode.M, False),
    "R26": (Keycode.I, False),
    "R20": (Keycode.K, False),
    "R18": (54, False),
    "R22": (Keycode.O, False),
    "R7": (Keycode.L, False),
    "R6": (55, False),
    "R3": (Keycode.P, False),
    "R9": (Keycode.O, False),  # Ö
    "R15": (Keycode.MINUS, False),
    "R2": (Keycode.U, False),  # Ü
    "R8": (Keycode.A, False),  # Ä
    "R10": (57, False),
    "R11": (57, False),  # placeholder
    "R13": (Keycode.CONTROL, False),
    "R14": (42, False),
    "R12": (44, False)
}

key_map_left = {
    "L26": (Keycode.ESCAPE, False),
    "L27": (Keycode.TAB, False), # tab
    "L28": (Keycode.TAB, False), # <
    "L22": (Keycode.Q, False),
    "L21": (Keycode.A, False),
    "L15": (Keycode.Y, False),
    "L20": (Keycode.W, False),
    "L10": (Keycode.S, False),
    "L14": (Keycode.X, False),
    "L6": (Keycode.E, False),
    "L7": (Keycode.D, False),
    "L13": (Keycode.C, False),
    "L3": (Keycode.R, False),
    "L9": (Keycode.F, False),
    "L12": (Keycode.V, False),
    "L2": (Keycode.T, False),
    "L8": (Keycode.G, False),
    "L11": (Keycode.B, False),
    "L18": (Keycode.ALT, False), # unten links
    "L17": (227, False), # windows key
    "L16": (227, False),
    "L19": (227, False)
}

# Initialize all pins as input with pull-up resistors
for pin_string in key_map_right.keys():
    pin_number = "GP" + pin_string[1:]
    pin = getattr(board, pin_number)
    pin = digitalio.DigitalInOut(pin)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    key_map_right[pin_string] = (pin, key_map_right[pin_string][0], key_map_right[pin_string][1])

while True:
    if clock_pin.value:
        data = receive_data(freq)
        print(data)

    for pin_string, (pin, keycode, pressed) in key_map_right.items():
        if not pin.value:  # Pin is active low
            if not pressed:
                print(f"Pin {pin_string} pressed, keycode: {keycode}")
                kbd.press(keycode)
                key_map_right[pin_string] = (pin, keycode, True)
        else:
            if pressed:
                print(f"Pin {pin_string} released, keycode: {keycode}")
                kbd.release(keycode)
                key_map_right[pin_string] = (pin, keycode, False)
    """
    if (data_pin.value):
        if (clock_pin.value):
            print(1, 1)
        else:
            print(0, 1)
    else:
        if (clock_pin.value):
            print(1, 0)
        else:
            print(0, 0)
    time.sleep(0.1)
    """
    
