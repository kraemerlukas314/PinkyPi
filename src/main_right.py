from machine import Pin
import time

pin_mapping = {
    28: 'z',
    21: 'h',
    17: 'n',
    27: 'u',
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

modifier_keys = ['ALT GR', 'STRG']

led = Pin(15, Pin.OUT)

while True:
    for pin_number, key in pin_mapping.items():
        pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        if pin.value() == 0:
            print("Pressed Key:", key)
            if pin_mapping[pin_number] not in modifier_keys:
                i = 0
                while pin.value() == 0:
                    pass
            else:
                print("Pressed mod key")
    
            
            
            
            
            
            