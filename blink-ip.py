#!/home/pi/repos/mini_oled/.venv/bin/python3


'''
displays IP address on OLED display; on for 4 seconds, off for 3 seconds

crontab -e entry: 
   @reboot /home/pi/repos/mini_oled/blink-ip.py > /home/pi/logs/blink-ip.log 2>&1

remember to: mkdir ~/logs

'''

import datetime
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
import os
import re
from time import sleep

DISPLAY_ON_SECONDS = 4
DISPLAY_OFF_SECONDS = 2
have_ip_one_shot = False

try:
   serial = i2c(port=1, address=0x3C)
   device = ssd1306(i2c_port=serial, width=128, height=32, rotate=1)
except:
   print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Error initializing OLED device', flush=True)

while True:
   wlan_if = os.popen('ip addr show wlan0').read()
   match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', wlan_if)
   if match:
      wlan_ip = match.group(1)
      wlan_ip_digits = wlan_ip.split('.')
      if not have_ip_one_shot:
         print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} have IP= {wlan_ip_digits}', flush=True)
         have_ip_one_shot = True
      display_lines = wlan_ip_digits
   else:
      display_lines = ["No", "IP", "Address"]

   with canvas(device) as draw:
      for i, line in enumerate(display_lines):
         draw.text((0, i*12), line, fill="white")

   sleep(DISPLAY_ON_SECONDS)

   with canvas(device) as draw:
      draw.rectangle(device.bounding_box, outline="black", fill="black")

   sleep(DISPLAY_OFF_SECONDS)
