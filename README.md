**Project purpose**<br>
Display local weather in Poznan, PL on the PCD8544 LCD Display

**Microcontroller**<br>
STM32F4Discovery

**Steps**
1. Get latest DFU file for board:
http://micropython.org/download/stm32/ <br><br>
Used for this project:<br>
http://micropython.org/resources/firmware/STM32F4DISC-20191220-v1.12.dfu 

2. Deploy DFU file through DfuSe USB:<br>
https://www.st.com/en/development-tools/stsw-stm32080.html

3. Create free account on OpenWeather - https://openweathermap.org/
4. Write API ID, country and city to send_temperature.py
5. Copy and paste files from F:\ to STM32
6. Run send_temperature.py