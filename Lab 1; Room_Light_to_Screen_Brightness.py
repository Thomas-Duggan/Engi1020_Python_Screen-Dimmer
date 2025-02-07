# Copyright (c) 2025 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


from engi1020.arduino.api import *


light = float(analog_read(6)) # reads light sensor value of pin A6
brightness = 0.32*light # expression to represent sensor to screen relationship

print("light: ",light) # prints room light reading to terminal
print("brightness: ",brightness) # prints screen brightness to terminal

brightness = int(brightness) # converts brightness float to int value for use in  LCD display, and color modifier
light = int(light) # converts light float to int value for use in LCD display

rgb_lcd_colour(brightness, brightness, brightness) # sets screen to brightness value
rgb_lcd_print(f'Room:{light}',0,0) # prints room brightness value onto screen
rgb_lcd_print(f'Screen:{brightness}',1,0) # prints screen brightness onto screen on the second column