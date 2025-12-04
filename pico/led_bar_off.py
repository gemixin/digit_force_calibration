"""
Turns all lights off on LED bar light.
"""

from machine import Pin
import time
from my9221 import MY9221

ledbar = MY9221(di=Pin(16), dcki=Pin(17))

ledbar.level(0)