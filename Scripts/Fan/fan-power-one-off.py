#!/usr/bin/env python
import time
import requests, json
import subprocess

def FanPowerOne():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c FanPower", shell=True)
	time.sleep(0.1)
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c FanPower", shell=True)
	time.sleep(0.1)
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c FanPower", shell=True)
	time.sleep(0.1)

def hue():
	payload = json.dumps({"state":{"flag":False}})
	a = requests.put('http://XX.X.X.X/api/XXXXXXXXXXXX-XXXXXXXXXX-XXXXXXXXXXXXXXXX/sensors/42', data=payload, headers={'content-type':'application/json'})
	print a.text

if __name__ == '__main__':
	try:
		fanPowerOne()
		hue()
	except requests.exceptions.RequestException as e:
		print e