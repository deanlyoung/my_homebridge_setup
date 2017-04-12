#!/usr/bin/env python
import requests
import PCF8591 as ADC
import RPi.GPIO as GPIO
import LCD1602
import time

GPIO.setmode(GPIO.BCM)

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

event = 'sound'

def setup():
	ADC.setup(0x48)
	LCD1602.init(0x27, 1) # init(slave address, background light)

def sound_reading():
	while True:
		voiceValue = ADC.read(0)
		if voiceValue:
			voiceValue = str(voiceValue)
			LCD1602.write(0, 0, voiceValue)
			if voiceValue < 90:
				sound_payload = {}
				sound_maker_url = base + event + '/with/key/' + key
				sound_payload['value1'] = voiceValue
				try:
					u = requests.get(sound_maker_url, params=sound_payload)
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
			time.sleep(0.2)
			LCD1602.clear()

def clear():
	LCD1602.clear()

if __name__ == '__main__':
	try:
		setup()
		sound_reading()
	except KeyboardInterrupt:
		clear()
		pass