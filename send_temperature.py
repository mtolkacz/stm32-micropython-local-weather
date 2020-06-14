"""
Author: Michał Tołkacz
Purpose: Get current or random temperature in Poznan and pass to the serial virtual port COM5
"""

import random
import serial
import requests

from settings import APP_ID

CITY = 'Poznan'
COUNTRY = 'pl'
APP_ID = APP_ID
URL = 'https://api.openweathermap.org/data/2.5/weather?q='+CITY+','+COUNTRY+'&appid='+APP_ID


# Return string with temperature or error code and boolean status
def get_temp():
    """
    Free OpenWearherMap API - openweathermap.org
    Example JSON:
    {"coord": {"lon": 16.93, "lat": 52.41},
     "weather": [{"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}], "base": "stations",
     "main": {"temp": 293.47, "feels_like": 291.15, "temp_min": 292.59, "temp_max": 294.15, "pressure": 1012,
              "humidity": 49}, "visibility": 10000, "wind": {"speed": 3.1, "deg": 60}, "clouds": {"all": 5},
     "dt": 1592160533, "sys": {"type": 1, "id": 1710, "country": "PL", "sunrise": 1592101770, "sunset": 1592162151},
     "timezone": 7200, "id": 3088171, "name": "Poznań", "cod": 200}
    """
    url = URL
    loaded_url = requests.get(url)
    status = False
    if loaded_url:
        dict = loaded_url.json()
        try:
            kelvin = float(dict['main']['temp'])
            celsius = round(kelvin - 273.15)
            text = str(celsius) + 'C'
            status = True
        except KeyError:
            text = 'Temperature not found'
    else:
        text = 'Error during opening API'
    return text, status


# Send temperature to the virtual serial port COM5
def send_temp(rand_temp=False):
    try:
        virtual_port = serial.Serial('COM5', 115200)
        print(virtual_port)
        if rand_temp:
            number = random.randrange(15, 30)
            temp = str(number) + 'C'
            status = True
        else:
            temp, status = get_temp()
            if not status:
                print('Fail')
            else:
                print('Success')
        print(temp)
        virtual_port.write(temp.encode('utf8')) if status else None
        virtual_port.close()
    except serial.serialutil.SerialException as e:
        print(e)


def main():
    send_temp(rand_temp=True)


if __name__ == "__main__":
    main()
