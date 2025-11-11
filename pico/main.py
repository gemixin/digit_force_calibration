"""
Streams Grove FSR (A0→GP26) voltage readings over USB.
"""

import machine
from machine import ADC, Pin
import time
import uos

# Grove Shield: A0 is connected to GP26 (ADC0), A1 → GP27 (ADC1), A2 → GP28 (ADC2)
fsr = ADC(Pin(26))  # GP26 = ADC0

# Setup USB serial communication
uart = machine.UART(0, baudrate=115200)

# Stream FSR voltage readings continuously
while True:
    value = fsr.read_u16()  # 16-bit value (0–65535)
    voltage = (value / 65535) * 3.3  # convert to voltage (assuming 3.3V ref)
    print(voltage)
    time.sleep(0.033) # ~33 ms per sample = 30 Hz
    