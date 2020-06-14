# boot.py -- run on boot-up

import machine
import pyb

# Main script to run after this one
pyb.main('main.py') 

# Act as a serial and a storage device
pyb.usb_mode('VCP+MSC') 

