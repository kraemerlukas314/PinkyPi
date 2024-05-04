import time
import board
import digitalio

pin_mapping = {
    28: 'Z',
    21: 'H',
    17: 'N',
    27: 'U',
    19: 'j',
    16: 'm',
    26: 'i',
    20: 'k',
    18: ',',
    22: 'o', 
    7: 'l',
    6: '.',
    3: 'p',
    9: 'ö',
    15: '-',
    2: 'ü',
    8: 'ä',
    10: '+',
    11: 'ALT GR',
    13: 'STRG', 
    14: 'BACKSPACE',  
    12: 'SPACE'      
}

for pin, label in pin_mapping.items():
    pin_object = digitalio.DigitalInOut(getattr(board, f"GP{pin}"))
    pin_object.switch_to_input(pull=digitalio.Pull.UP)
    pin_mapping[pin] = {'button': pin_object, 'label': label}
"""
while True: 
    for pin, data in pin_mapping.items():
        print("Pin:", pin, "Label:", data['label'], " Value:", data['button'].value)
    time.sleep(0.1)
"""