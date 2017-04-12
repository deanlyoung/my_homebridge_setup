#!/usr/bin/env python
import grequests
import PCF8591 as ADC
import RPi.GPIO as GPIO
import LCD1602
import RPi_I2C_driver
import time

BtnPin = 23

mylcd = RPi_I2C_driver.lcd()

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'
event = 'sound'

isPressed = False
isOn = False

url = sound_maker_url = base + event + '/with/key/' + key

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(BtnPin, GPIO.RISING, callback=buttonPress, bouncetime=300)
	ADC.setup(0x48)
	mylcd.backlight(0)

def exception_handler(request, exception):
	print "Request failed"

def buttonPress(channel):
	global isPressed
	global isOn
	while 1:
		if GPIO.input(BtnPin):
				isPressed = True
		elif isPressed:
				isOn = not isOn
				if isOn == True and isPressed == True:
					mylcd.backlight(1)
					# print "ON"
				else:
					mylcd.backlight(0)
					# print "OFF"
				isPressed = False
		time.sleep(0.1)

def loop():
	global isPressed
	global isOn
	global urls
	while 1:
		voiceValue = ADC.read(0)
		if voiceValue:
			voiceChar = str(voiceValue)
			# print voiceChar + ' dB'
			if isPressed == True and isOn == True:
				LCD1602.init(0x27, 1)
				LCD1602.write(0, 0, voiceChar + ' dB')
			if voiceValue < 80:
				# print "Trigger!"
				if isPressed == True and isOn == True:
					LCD1602.init(0x27, 1)
					LCD1602.write(0, 0, voiceChar + ' dB')
					LCD1602.write(0, 1, 'Trigger!')
				sound_payload = {}
				sound_payload['value1'] = voiceValue
				reqs = (grequests.get(u, data=sound_payload) for u in url)
				resp = grequests.map(reqs, exception_handler=exception_handler)
		time.sleep(0.2)

def destroy():
	mylcd.backlight(0)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()