import pcd8544 # 3rd party library to manage PCD8544 display
import pyb
import machine

# Assign STM32F407VG components
# https://www.st.com/resource/en/datasheet/stm32f407vg.pdf
# 3V3 or any Pin => +V        3.3V logic voltage (0=off, 1=on)
# MOSI           => DIN       data flow (Master out, Slave in)
# SCK            => CLK       SPI clock 
# any Pin        => RST       Reset pin (0=reset, 1=normal)
# any Pin        => CE        Chip Enable (0=listen for input, 1=ignore input)
# any Pin        => D/C       Data/Command (0=commands, 1=data)
# GND            => GND

spi = machine.SPI(1) # CLK - PA5, DIN - PA7
spi.init(baudrate=2000000, polarity=0, phase=0) # 
cs = machine.Pin('PC4') # CE
dc = machine.Pin('PC5') # D/C 
rst = machine.Pin('PB1') # RST

# Init LCD display
lcd = pcd8544.PCD8544_FRAMEBUF(spi, cs, dc, rst)
lcd.init()

# Create object representing the USB virtual comm port
obj = pyb.USB_VCP()

while True:
    # Read all available bytes from the serial device
    buf = obj.read() 

    if buf:
        # Turn on LED
        pyb.LED(1).on() 
        
        # Refresh and init LCD display
        lcd = pcd8544.PCD8544_FRAMEBUF(spi, cs, dc, rst) 
        lcd.init()

        # Decode data from the serial device
        text = str(buf.decode()) 

        # Fill the entire FrameBuffer with the specified color
        lcd.fill(0) 

        # Print data from the serial device on the screen
        lcd.text(text, 2, 1, 1)	

        # Write data through SPI
        lcd.show() 

        # Turn off LED
        pyb.LED(1).off() 
