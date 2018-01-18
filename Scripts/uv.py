#!/usr/bin/env python
import requests
import json

base = 'https://maker.ifttt.com/trigger/'
key = 'XXX'

uv_event = 'current_uv_index'

wundergroundUrl = 'http://api.wunderground.com/api/'
wundergroundApiKey = 'XXX'
lat = 'XX.XXXXXX'
lon = 'XXX.XXXXXX'

def setup():
	print '\n UV Index begins...'

def uv():
	weatherUrl = wundergroundUrl + wundergroundApiKey + '/conditions/q/' + lat + ',' + lon + '.json'
	try:
		uvjdata = requests.get(weatherUrl).json()
		uv_index = uvjdata['current_observation']['UV']
		maker_url = base + uv_event + '/with/key/' + key
		payload = {}
		payload['value1'] = '{0}'.format(uv_index)
		
		try:
			q = requests.get(maker_url, params=payload)
			print q.text
			
			pushover_url = 'https://api.pushover.net/1/glances.json'
			params_p = {}
			params_p['token'] = 'token'
			params_p['user'] = 'user'
			params_p['count'] = '{0:.0}'.format(uv_index)
			try:
				p = requests.post(pushover_url, params_p)
				print p.text
			except requests.exceptions.Timeout as e:
				print e
			except requests.exceptions.ConnectionError as e:
				print e
			except requests.exceptions.RequestException as e:
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
		
		headers = {'Content-Type':'application/json'}
		uv_url = 'http://10.0.1.2/api/XXX/sensors/47/state'
		uv_payload = {}
		uv_payload['status'] = int(round(float(uv_index)))
		try:
			u = requests.put(uv_url, json = uv_payload, headers = headers)
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
		uv()
	except KeyboardInterrupt:
		pass