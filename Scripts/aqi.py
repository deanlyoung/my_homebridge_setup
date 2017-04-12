#!/usr/bin/env python
import requests
import json

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

aqi_event = 'aqi'

token = 'XXX'

def setup():
	print '\n AQI begins...'

def aqi():
	url = 'http://api.waqi.info/feed/geo:XXX;XXX/?token=' + token
	try:
		wjdata = requests.get(url).json()
		aqi = wjdata['data']['aqi']
		pm25 = wjdata['data']['iaqi']['pm25']['v']
		maker_url = base + aqi_event + '/with/key/' + key
		payload = {}
		payload['value1'] = '{0}'.format(aqi)
		payload['value2'] = '{0}'.format(pm25)
		try:
			q = requests.get(maker_url, params=payload)
			print q.text
		except requests.exceptions.Timeout as e:
			# timeout
			print e
		except requests.exceptions.ConnectionError as e:
			# connection error
			print e
		except requests.exceptions.RequestException as e:
			# error
			print e
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
		aqi()
	except KeyboardInterrupt:
		pass