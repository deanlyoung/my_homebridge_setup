#!/usr/bin/env python
import requests
import time
import math
import os

ds18b20 = ''

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

event = 'kitchen_temp'

def setup():
	global ds18b20
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1-bus-master1':
			ds18b20 = i

def temperature_reading():
	# global ds18b20
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile= open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temp = temperature / 1000
	temp = temp * 1.8 + 32
	temperature_payload = {}
	temperature_maker_url = base + event + '/with/key/' + key
	temperature_payload['value1'] = '{0:0.1f}'.format(temp)
	try:
		u = requests.get(temperature_maker_url, params=temperature_payload)
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
	try:
		setup()
		temperature_reading()
	except KeyboardInterrupt:
		pass