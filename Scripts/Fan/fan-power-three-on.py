#!/usr/bin/env python
import time
import requests, json
import subprocess

def fanPowerThree():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c FanPower -d Bedroom", shell=True)
	time.sleep(0.5)
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c FanOscillateIonizer -d Bedroom", shell=True)
	time.sleep(0.5)
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c FanOscillateIonizer -d Bedroom", shell=True)
	time.sleep(0.1)

def hue():
	payload = json.dumps({"state":{"flag":True}})
	a = requests.put('http://XX.X.X.X/api/XXXXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXXXXXXXX/sensors/44', data=payload, headers={'content-type':'application/json'})
	print a.text

if __name__ == '__main__':
	try:
		fanPowerThree()
		hue()
	except requests.exceptions.RequestException as e:
		print e