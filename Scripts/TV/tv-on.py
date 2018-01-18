#!/usr/bin/env python
import time
import requests, json
import subprocess

def projector():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c Projector -d LivingRoom", shell=True)
	time.sleep(0.5)

def receiver():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c ReceiverOn -d LivingRoom", shell=True)
	time.sleep(0.1)

def hue():
	payload = json.dumps({"state":{"flag":True}})
	a = requests.put('http://XX.X.X.X/api/XXX/sensors/35', data=payload, headers={'content-type':'application/json'})
	print a.text
	time.sleep(0.1)
	b = requests.put('http://XX.X.X.X/api/XXX/sensors/36', data=payload, headers={'content-type':'application/json'})
	print b.text
	time.sleep(0.1)
	c = requests.put('http://XX.X.X.X/api/XXX/sensors/37', data=payload, headers={'content-type':'application/json'})
	print c.text
	time.sleep(0.1)

def appletv():
	d = requests.get('http://XX.X.X.XX:XXXX/login?pairing-guid=XxXXXXXXXXXXXXXXXX')
	print d.text

if __name__ == '__main__':
	try:
		projector()
		receiver()
		hue()
		appletv()
	except requests.exceptions.RequestException as e:
		print e