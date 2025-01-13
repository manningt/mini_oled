# Displays IP address on OLED display
### on for 4 seconds, off for 3 seconds

crontab -e entry: 
```
@reboot /home/pi/repos/mini_oled/blink-ip.py > /home/pi/logs/blink-ip.log 2>&1
```
remember to: mkdir ~/logs

Requires a venv, with the following installed:
- https://pypi.org/project/luma.core/#files
- https://pypi.org/project/luma.oled/#files

### References
- https://luma-oled.readthedocs.io/en/latest/intro.html
- https://iotexpert.com/debugging-ssd1306-display-problems/
