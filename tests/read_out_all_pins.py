import board
import digitalio
import time

pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,
        board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
        board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP23,
        board.GP24, board.GP25, board.GP26, board.GP27, board.GP28]

pin_objs = [digitalio.DigitalInOut(pin) for pin in pins]
for pin in pin_objs:
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

while True:
    for i, pin in enumerate(pin_objs):
        if not pin.value:
            print(f"Pin {i} is connected to GND")
