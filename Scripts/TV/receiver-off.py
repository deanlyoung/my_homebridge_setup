#!/usr/bin/env python
import time
import requests, json
import subprocess

def receiver():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c ReceiverOff", shell=True)
	time.sleep(0.1)

def hue():
	payload = json.dumps({"state":{"flag":False}})
	a = requests.put('http://XX.X.X.X/api/XXX/sensors/35', data=payload, headers={'content-type':'application/json'})
	print a.text

if __name__ == '__main__':
	try:
		receiver()
		hue()
	except requests.exceptions.RequestException as e:
		print e