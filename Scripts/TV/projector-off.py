#!/usr/bin/env python
import time
import requests, json
import subprocess

def projector():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c Projector -d LivingRoom", shell=True)
	time.sleep(0.1)

def hue():
	payload = json.dumps({"state":{"flag":False}})
	b = requests.put('http://XX.X.X.X/api/XXX/sensors/36', data=payload, headers={'content-type':'application/json'})
	print b.text

if __name__ == '__main__':
	try:
		projector()
		hue()
	except requests.exceptions.RequestException as e:
		print e