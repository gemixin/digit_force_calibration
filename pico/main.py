"""
Streams Grove FSR (A0→GP26) voltage readings over USB.
Also displays current force level on LED bar light.
"""

import machine
from machine import ADC, Pin
import time
import uos
from my9221 import MY9221

# Grove Shield: LED bar on D16 (DI = GP16, CLK = GP17)
ledbar = MY9221(di=Pin(16), dcki=Pin(17))

# Grove Shield: A0 is connected to GP26 (ADC0), A1 → GP27 (ADC1), A2 → GP28 (ADC2)
fsr = ADC(Pin(26))  # GP26 = ADC0

# Setup USB serial communication
uart = machine.UART(0, baudrate=115200)

# Stream FSR voltage readings continuously
while True:
    value = fsr.read_u16()  # 16-bit value (0–65535)
    voltage = (value / 65535) * 3.3  # convert to voltage (assuming 3.3V ref)
    
    # Set LED bar level according to level 1, 2 and 3 thresholds
    # Force level 2
    if voltage > 0.99 and voltage <= 2.99:
        ledbar.level(2, 0x0F)  # 2 bars at 50% brightness
    # Force level 3
    elif voltage > 2.99:
        ledbar.level(3, 0x0F)  # 3 bars at 50% brightness
    # Force level 1
    else:
        ledbar.level(1, 0x0F)  # 1 bars at 50% brightness
        
    # Print voltage (streams over USB)
    print(voltage)
    time.sleep(0.033) # ~33 ms per sample = 30 Hz
    