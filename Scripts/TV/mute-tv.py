#!/usr/bin/env python
import time
import requests, json
import subprocess

def receiver():
	subprocess.Popen("python /home/pi/Downloads/BlackBeanControl/BlackBeanControl.py -c MuteTV", shell=True)
	time.sleep(0.1)

if __name__ == '__main__':
	try:
		receiver()
	except requests.exceptions.RequestException as e:
		print e