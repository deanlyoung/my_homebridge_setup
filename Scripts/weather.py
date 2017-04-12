#!/usr/bin/env python
import requests
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

Sensor = 11
humiture = 17

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

event = 'weather'

def setup():
	print '\n Begin weather program...'

def temp_press_hum():
	temp_press_sensor = BMP085.BMP085()
	celsius = temp_press_sensor.read_temperature()                # Read temperature to veriable celsius
	fahrenheit = celsius*1.8+32                                   # Convert celsius to fahrenheit
	pascal = temp_press_sensor.read_pressure()                    # Read pressure to variable pascal
	mmhg = 0.00750147598*pascal                                   # Convert pascal to mmHg
	hum, temperature = DHT.read_retry(Sensor, humiture)           # Read humidity and temperature to variables
	humidity = float(hum)
	weather_maker_url = base + event + '/with/key/' + key
	weather_payload = {}
	weather_payload['value1'] = '{0:0.2f}'.format(mmhg)
	weather_payload['value2'] = '{0:0.2f}'.format(fahrenheit)
	weather_payload['value3'] = '{0:0.1f}'.format(humidity)
	
	try:
		u = requests.get(weather_maker_url, params=weather_payload)
		print u.text
	except requests.exceptions.Timeout as e:
		# timeout
		print e
	except requests.exceptions.ConnectionError as e:
		# connection error
		print e
	except requests.exceptions.RequestException as e:
		# error
		print e

if __name__ == '__main__':
	setup()
	try:
		temp_press_hum()
	except KeyboardInterrupt:
		pass