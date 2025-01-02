#!/usr/bin/env python3

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import os
import re

serial = i2c(port=1, address=0x3C)
device = ssd1306(i2c_port=serial, width=128, height=32, rotate=1)

# print(f"{device.width=} {device.height=} {device.bounding_box=} {device.mode=} {device.size=}")
#device.width=128 device.height=32 device.bounding_box=(0, 0, 127, 31) device.mode='1' device.size=(128, 32)

'''
T,R--T,L
 |    |
 |    |
 |    |
B,R--B,L

127,0 -- 127,31
   |         |
   |         |
   |         |
0,0   --   0,31
'''

wlan_if = os.popen('ip addr show wlan0').read()
match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', wlan_if)
if match:
   wlan_ip = match.group(1)
   wlan_ip_digits = wlan_ip.split('.')
# print(f"{wlan_ip_digits=}")

with canvas(device) as draw:
   if 0:
      draw.line((41, 0, 127, 0), fill="white") # B,R -> T,R
      # draw.line((127,0, 127,31), fill="white") # T,R -> T,L
      # draw.line((127,31, 0,31), fill="white") # T,L -> B,L
      draw.line((41,0, 41,31), fill="white") # B,L -> B,R    Lines below pix 41 do not show

      # draw.rectangle(device.bounding_box, outline="white", fill="black")

   # test_lines = ["1UUUU", "2UUUU", "3UUUU", "4UUUU"]
   for i, line in enumerate(wlan_ip_digits):
      draw.text((0, i*12), line, fill="white")

finish = input("Hit Enter to close the program")